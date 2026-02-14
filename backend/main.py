import cv2
import sys
import datetime
import time
from collections import deque
from ultralytics import YOLO

from detection.tracker import PersonTracker
from detection.threat_logic import ThreatDetector
from detection.follow_logic import FollowDetector
from alert.sound_alert import play_alert
from alert.authority_alert import send_authority_alert
from database.db import init_db, save_alert
from config import CAMERA_CONFIG

# ---------------- DISPLAY CONFIG ----------------
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

# ---------------- CAMERA SETUP ----------------
CAMERA_ID = sys.argv[1] if len(sys.argv) > 1 else "cam1"

if CAMERA_ID not in CAMERA_CONFIG:
    print("❌ Invalid camera ID")
    exit()

cam = CAMERA_CONFIG[CAMERA_ID]

print("Starting program for:", cam["label"])
init_db()

cap = cv2.VideoCapture(cam["source"])
if not cap.isOpened():
    print("❌ Video not opened")
    exit()
else:
    print("✅ Video opened successfully")

# ---------------- MODEL ----------------
model = YOLO("yolov8n-pose.pt")

FPS = int(cap.get(cv2.CAP_PROP_FPS)) or 25
BUFFER_SECONDS = 12
frame_buffer = deque(maxlen=FPS * BUFFER_SECONDS)

tracker = PersonTracker()
threat_detector = ThreatDetector()
follow_detector = FollowDetector()

# ---------------- ALERT COOLDOWN ----------------
LAST_ALERT_TIME = 0
ALERT_COOLDOWN = 30   # seconds (spam control)

# ---------------- WINDOW ----------------
cv2.namedWindow("AI Surveillance", cv2.WINDOW_NORMAL)
cv2.resizeWindow("AI Surveillance", DISPLAY_WIDTH, DISPLAY_HEIGHT)

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_buffer.append(frame.copy())
    results = model(frame, verbose=False)

    centers = []
    people = []

    for r in results:
        if r.keypoints is not None:
            for person in r.keypoints.xy:
                valid = person[person[:, 0] > 0]
                if len(valid) == 0:
                    continue

                cx = int(valid[:, 0].mean())
                cy = int(valid[:, 1].mean())
                centers.append((cx, cy))

                people.append({
                    "center": (cx, cy),
                    "gender": "female" if cx % 2 == 0 else "male"  # demo logic
                })

                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    tracked = tracker.update(centers)

    interaction_threat = threat_detector.check(tracked, people)
    follow_threat = follow_detector.check(tracked)
    threat = interaction_threat or follow_threat

    now = time.time()

    if threat and (now - LAST_ALERT_TIME > ALERT_COOLDOWN):
        LAST_ALERT_TIME = now

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"evidence_{timestamp}_{CAMERA_ID}.mp4"

        out = cv2.VideoWriter(
            filename,
            cv2.VideoWriter_fourcc(*"mp4v"),
            FPS,
            (frame.shape[1], frame.shape[0])
        )

        for f in frame_buffer:
            out.write(f)
        out.release()

        female_present = any(p["gender"] == "female" for p in people)

        if follow_threat:
            reason = "Suspicious following / chase detected"
            priority = "HIGH"
        elif female_present:
            reason = "Female safety risk detected"
            priority = "HIGH"
        else:
            reason = "Aggressive interaction detected"
            priority = "MEDIUM"

        save_alert(
            camera=CAMERA_ID,
            reason=reason,
            priority=priority,
            evidence=filename,
            time=timestamp
        )

        print("🚨 ALERT:", reason)
        play_alert()

        send_authority_alert(
            reason=reason,
            location=cam["location"],
            priority=priority,
            lat=cam["lat"],
            lng=cam["lng"]
        )

        cv2.rectangle(frame, (10, 10), (620, 60), (0, 0, 255), -1)
        cv2.putText(
            frame,
            cam["label"] + " ⚠️ ALERT",
            (20, 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2
        )

    else:
        cv2.rectangle(frame, (10, 10), (620, 60), (0, 0, 0), -1)
        cv2.putText(
            frame,
            cam["label"],
            (20, 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 255),
            2
        )

    # ---------------- DISPLAY RESIZE ----------------
    h, w, _ = frame.shape
    scale = min(DISPLAY_WIDTH / w, DISPLAY_HEIGHT / h)

    display_frame = cv2.resize(
        frame,
        (int(w * scale), int(h * scale))
    )

    cv2.imshow("AI Surveillance", display_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
