# 🛡️ SafeGuard AI  
### AI-Powered Real-Time Suspicious Activity Detection System  

## 📌 Project Overview

**SafeGuard AI** is an AI-powered real-time surveillance system designed to automatically detect suspicious human activities using CCTV video feeds.
Traditional CCTV systems only record incidents for later review. SafeGuard AI transforms surveillance into an **intelligent proactive security system** capable of detecting threats instantly and triggering real-time alerts.
The system analyzes live video streams using deep learning models and immediately notifies security personnel when suspicious activity is detected.

## 🚨 Problem Statement

Current surveillance systems suffer from:

- Passive monitoring
- Delayed incident response
- Human dependency for observation
- Missed prevention opportunities

SafeGuard AI solves this by enabling **real-time automated threat detection and alerting**.

## ⚙️ Key Features

✅ Real-time CCTV video monitoring  
✅ AI-based suspicious activity detection  
✅ YOLOv8 pose detection model  
✅ Instant alert triggering  
✅ WhatsApp notification with location  
✅ Incident logging in database  
✅ Continuous automated monitoring  

## 🧠 Technology Stack

### Backend
- Python
- FastAPI
- OpenCV
- YOLOv8 Pose Detection
- AMD GPU Acceleration

### AI / Machine Learning
- Computer Vision
- Deep Learning
- Human Pose Detection

### Database
- SQLite / Local Database

## 🏗️ Project Structure

SafeGuard-AI/
│
└── AI-Surveillance-backend/
    │
    ├── alert/
    ├── database/
    ├── detection/
    ├── videos/
    │
    ├── app.py
    ├── main.py
    ├── auth.py
    ├── config.py
    ├── yolov8n-pose.pt
```

## 🚀 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Shakti-sys/AI-Enabled-Smart-Surveillance-System.git
```

### 2️⃣ Navigate to Backend
```bash
cd SafeGuard-AI/AI-Surveillance/backend
```

### 3️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 4️⃣ Activate Environment

**Windows**
```bash
venv\Scripts\activate
```

**Linux / Mac**
```bash
source venv/bin/activate
```

### 5️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 6️⃣ Run Application
```bash
python main.py
```

## 🔄 System Workflow

1. CCTV Live Feed Capture  
2. Frame Extraction  
3. YOLO AI Model Processing  
4. Suspicious Activity Detection  
5. Alert Trigger  
6. WhatsApp Notification  
7. Incident Logging  
8. Continuous Monitoring  

## 🎯 Use Cases

- Smart City Surveillance  
- Public Safety Monitoring  
- Campus Security  
- Railway Stations & Airports  
- Shopping Malls  
- Restricted Area Monitoring  

## 🔮 Future Enhancements

- Web Dashboard Integration  
- Multi-camera Support  
- Cloud Deployment  
- Facial Recognition Integration  
- Mobile Monitoring Application  
