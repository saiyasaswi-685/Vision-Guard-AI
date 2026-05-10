# Vision Guard AI – Real-Time Helmet Detection and Cloud Monitoring System

An AI-powered Real-Time Helmet Detection and Smart Monitoring System developed using Python, YOLOv8, OpenCV, Roboflow, AWS S3, Gmail SMTP, and Streamlit. The system monitors live video streams using a webcam or DroidCam-connected mobile camera and automatically detects helmet and no-helmet violations in real time.

Whenever a helmet violation is detected, the system:

* Generates an instant voice alert
* Captures the violation image
* Uploads the image to AWS S3 cloud storage
* Generates a public S3 image URL
* Sends an automated email notification to the admin
* Maintains CSV-based violation logs
* Displays monitoring information through a Streamlit dashboard

---

# Features

* Real-time helmet detection using YOLOv8
* Multi-person detection support
* Helmet and no-helmet classification
* Live webcam / DroidCam monitoring
* Voice alerts for violations
* Automatic violation image capture
* AWS S3 cloud image upload
* Public S3 image URL generation
* Gmail SMTP email notifications
* Timestamp-based violation logging
* Streamlit monitoring dashboard
* CSV-based log management
* Bounding box and confidence score display
* Modular and scalable project structure
* Secure `.env` credential management

---

# Technologies Used

* Python
* YOLOv8
* OpenCV
* Roboflow
* Ultralytics
* NumPy
* boto3
* AWS S3
* Gmail SMTP
* pyttsx3 / pygame
* Streamlit
* pandas
* dotenv

---

# Project Structure

```text
Vision-Guard-AI/
│
├── alerts/
│   ├── sound_alert.py
│   └── email_alert.py
│
├── aws/
│   └── s3_uploader.py
│
├── detection/
│   └── helmet_detector.py
│
├── utils/
│   ├── image_saver.py
│   └── s3_logger.py
│
├── captured_alerts/
│
├── models/
│
├── dashboard.py
├── main.py
├── train.py
├── config.py
├── data.yaml
├── s3_logs.csv
├── requirements.txt
├── .env.example
└── README.md
```

---

# System Workflow

1. Capture live video from webcam or DroidCam
2. Process video frames using OpenCV
3. Detect helmet / no-helmet using YOLOv8
4. Generate voice alert for violations
5. Capture violation image with timestamp
6. Upload image to AWS S3
7. Generate S3 image URL
8. Send email notification to admin
9. Save logs in CSV format
10. Display monitoring dashboard using Streamlit

---

# Installation Guide

## 1. Clone Repository

```bash
git clone https://github.com/saiyasaswi-685/Vision-Guard-AI.git

cd Vision-Guard-AI
```

---

# 2. Install Required Packages

```bash
pip install ultralytics
pip install opencv-python
pip install numpy
pip install boto3
pip install python-dotenv
pip install pandas
pip install streamlit
pip install pygame
pip install pyttsx3
```

OR

```bash
pip install -r requirements.txt
```

---

# 3. Prepare Dataset

Export dataset from Roboflow in YOLOv8 format.

Replace `data.yaml` with your dataset configuration.

Required classes:

```yaml
names:
  0: helmet
  1: no_helmet
```

---

# 4. Train YOLOv8 Model

```bash
python train.py
```

After training, model weights will be generated at:

```text
models/helmet_train/weights/best.pt
```

---

# 5. Configure Environment Variables

Create a file named:

```text
.env
```

Add the following credentials:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password

AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_KEY=your_aws_secret_key
```

---

# 6. Configure Video Source

Inside `config.py`:

## Webcam

```python
VIDEO_SOURCE = 0
```

## DroidCam / IP Camera

```python
VIDEO_SOURCE = "http://192.168.1.100:4747/video"
```

---

# 7. Run Real-Time Detection

```bash
python main.py
```

Press:

```text
q
```

to quit the application.

---

# 8. Run Streamlit Dashboard

```bash
streamlit run dashboard.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

# Dashboard Features

* Total violation count
* Latest captured image
* System status monitoring
* Violation timestamps
* S3 image URLs
* CSV log visualization
* Real-time monitoring interface

---

# AWS S3 Integration

The system automatically:

* Uploads captured violation images to AWS S3
* Generates public image URLs
* Stores image evidence securely in cloud storage

Example S3 URL:

```text
https://your-bucket-name.s3.amazonaws.com/image.jpg
```

---

# Gmail SMTP Integration

The system sends automated email alerts containing:

* Violation timestamp
* Alert message
* Attached violation image
* AWS S3 image URL

SMTP Server Used:

```text
smtp.gmail.com
```

Port:

```text
465
```

---

# Detection Features

* Real-time helmet detection
* Multi-person detection
* Confidence score display
* Bounding box visualization
* Violation image capture
* Voice alerts
* Automated monitoring

---

# Error Handling Included

* Camera connection failure
* Missing YOLO model weights
* Missing dataset configuration
* AWS S3 upload failure
* SMTP email sending failure
* Frame read failure
* Image save failure
* Sound playback failure

---

# Security Features

* Secure credential management using `.env`
* No hardcoded AWS keys
* No hardcoded SMTP passwords
* GitHub-safe project structure

---

# Future Enhancements

* Database integration
* Advanced analytics dashboard
* Vehicle number plate recognition
* Mobile application support
* Cloud automation
* AI-based safety analytics
* Web-based live monitoring

---

# Project Type

AI-Based Real-Time Helmet Detection and Cloud Monitoring System

---

# Developed Using

* Python
* YOLOv8
* OpenCV
* AWS S3
* Gmail SMTP
* Streamlit
* Roboflow
* Ultralytics

---

# License

This project is developed for educational and research purposes.
