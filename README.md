# 🛡️ SafeGuard AI  
### AI-Powered Smart Surveillance & Suspicious Activity Detection System  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/YOLOv8-AI%20Model-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-purple?style=for-the-badge"/>
</p>

## 🚀 Project Overview

**SafeGuard AI** is an intelligent AI-powered surveillance system designed to automatically detect violence, harassment, and suspicious human behavior from CCTV or live video feeds in real time.

Unlike traditional surveillance systems that only record footage, SafeGuard AI actively analyzes human movements using deep learning and computer vision models to detect threats instantly, send alerts to authorities via WhatsApp, and securely store incident evidence for future investigation.

## 🚨 Problem Statement

Traditional CCTV systems suffer from:

- Passive monitoring  
- Delayed incident response  
- Continuous human supervision requirement  
- Lack of real-time threat prevention  

SafeGuard AI transforms surveillance into a **proactive security system** capable of automated real-time threat detection and alerting.

## ✨ Key Features

✅ Real-time CCTV monitoring  
✅ AI-based human pose detection (YOLOv8)  
✅ Suspicious behavior & following detection  
✅ Real-time alert generation  
✅ WhatsApp notifications using Twilio  
✅ Live location sharing  
✅ Automatic incident recording  
✅ Persistent alert logging (SQLite)  
✅ Multi-camera configurable monitoring  
✅ REST API based video analysis  

## 🧠 Technology Stack

### Programming Language
- Python

### Backend
- Flask API

### AI / Machine Learning
- YOLOv8 Pose Detection (Ultralytics)
- Computer Vision
- Deep Learning

### Libraries
- OpenCV
- Twilio API
- python-dotenv

### Database
- SQLite

## 📂 Project Structure

```
SafeGuard-AI/
│
├── README.md
│
└── backend/
    ├── app.py
    ├── main.py
    ├── auth.py
    ├── config.py
    ├── yolov8n-pose.pt
    ├── .env.example
    │
    ├── alert/
    │   ├── authority_alert.py
    │   ├── sound_alert.py
    │   └── alert.wav
    │
    ├── database/
    │   ├── alerts.db
    │   └── db.py
    │
    ├── detection/
    │   ├── threat_logic.py
    │   ├── follow_logic.py
    │   ├── tracker.py
    │   └── yolo_detector.py
    │
    └── videos/
```

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Shakti13-sys/AI-Enabled-Smart-Surveillance-System.git
cd AI-Enabled-Smart-Surveillance-System
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / Mac
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install flask opencv-python ultralytics twilio python-dotenv
```

### 4️⃣ Download YOLOv8 Pose Model

Download **yolov8n-pose.pt** from:  
https://github.com/ultralytics/ultralytics/releases  

Place inside:
```
backend/
```

### 5️⃣ Environment Variables Setup

Create `.env` inside **backend/**

```
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
WHATSAPP_FROM=whatsapp:+14155238886
AUTHORITY_NUMBERS=whatsapp:+91xxxxxxxxxx
```

## ▶️ Usage

### Continuous Surveillance Mode
Run monitoring for configured camera:

```bash
python backend/main.py cam1
```

### API Based Video Detection

Start Flask server:

```bash
python backend/app.py
```

Send detection request:

```bash
curl -X POST http://127.0.0.1:5000/detect \
-H "Content-Type: application/json" \
-H "X-API-KEY: ADMIN-1234" \
-d '{"video":"sample.mp4"}'
```

## 🔄 System Workflow

1. CCTV Feed Capture  
2. Frame Processing  
3. YOLOv8 Pose Detection  
4. Behavioral Analysis  
5. Suspicious Activity Detection  
6. Alert Trigger  
7. WhatsApp Notification  
8. Incident Logging & Storage  

## 🎯 Use Cases

- Smart City Surveillance  
- Women Safety Monitoring  
- Campus Security  
- Airports & Railway Stations  
- Public Transport Monitoring  
- Restricted Area Security  

## 🔮 Future Enhancements

- Web Dashboard Integration  
- Multi-camera Live Monitoring  
- Cloud Deployment  
- Facial Recognition  
- Mobile Application Support  

---
