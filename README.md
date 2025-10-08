# 🚗 Drowsiness Detection System

A real-time computer vision–based system that detects driver drowsiness and triggers alerts to prevent accidents.

---

## 🧠 Overview

Driver fatigue is one of the major causes of road accidents. This **Drowsiness Detection System** monitors the driver’s eyes using a webcam and detects when they start to close for a prolonged period. When drowsiness is detected, the system issues an **audio/visual alert** to wake the driver.

This project combines **OpenCV**, **dlib**, and **facial landmark detection** techniques to identify and monitor eye closure in real time.

---

## ✨ Features

- 👁️ Real-time eye and face detection  
- 💤 Drowsiness detection using Eye Aspect Ratio (EAR)  
- 🔊 Alarm sound when the driver is drowsy  
- 📸 Works with standard webcams  
- ⚙️ Adjustable sensitivity and alert thresholds  

---

## ⚙️ How It Works

1. Captures live video frames from the webcam.  
2. Detects the face and eyes using Haar cascades or facial landmarks.  
3. Calculates the **Eye Aspect Ratio (EAR)** to check if the eyes are closed.  
4. Counts consecutive frames with closed eyes.  
5. If eyes remain closed beyond a threshold, an alarm is triggered.  

---

## 🧩 Requirements

Install the following dependencies before running the project:

- Python 3.x  
- OpenCV  
- dlib  
- imutils  
- numpy  
- playsound (or pygame for audio alerts)

---

🚀 Installation & Setup

1. Clone the repository:

git clone https://github.com/syed-tahir/Drowsiness_system.git
cd Drowsiness_system

2. Install dependencies:

pip install -r requirements.txt

3. Place required model files

(shape_predictor_68_face_landmarks.dat) in the project folder.

---

📂 Project Structure

Drowsiness_system/
├── models/
│   └── shape_predictor_68_face_landmarks.dat
├── assets/
│   └── alarm.wav
├── drowsiness_detection.py
├── utils.py
├── requirements.txt
└── README.md


---

🧪 Results

Detects eye closure accurately in normal lighting.

Triggers audio alert after consecutive frames of eye closure.

Works in real time on standard laptops/webcams.

---

🚧 Limitations

Accuracy may drop in low light or when wearing glasses.

Requires frontal face visibility.

Performance depends on camera resolution and frame rate.

---

🔮 Future Enhancements

Integrate yawn detection and head pose estimation

Deploy on Raspberry Pi or edge devices

Use deep learning models for better accuracy

Add dashboard for driver monitoring analytics.

---

📜 License

This project is licensed under the MIT License – see the LICENSE file for details.


---

👤 Author

Syed Mohammed Tahir

🌐 GitHub Profile : syed-tahir

💬 Open to collaborations & suggestions
