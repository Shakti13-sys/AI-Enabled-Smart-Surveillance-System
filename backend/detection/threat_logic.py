import math

class ThreatDetector:
    def __init__(self):
        self.counter = 0

    def check(self, tracked_people, people_info):
        if len(tracked_people) < 2:
            self.counter = 0
            return False

        ids = list(tracked_people.keys())
        (x1, y1) = tracked_people[ids[0]]
        (x2, y2) = tracked_people[ids[1]]

        distance = math.hypot(x1 - x2, y1 - y2)

        g1 = people_info[0]["gender"]
        g2 = people_info[1]["gender"]

        female_involved = (g1 == "female" or g2 == "female")

        # 👩 FEMALE PRIORITY
        if female_involved:
            distance_thresh = 160
            frame_thresh = 10
        else:
            distance_thresh = 120
            frame_thresh = 20

        print(f"📏 Distance={int(distance)} | female={female_involved}")

        if distance < distance_thresh:
            self.counter += 1
        else:
            self.counter = 0

        return self.counter >= frame_thresh
