# Gesture-Based Music Controller

Control your music player using **hand gestures** detected through your webcam!  
This project uses **MediaPipe** and **OpenCV** to recognize hand movements and control songs — all hands-free.  

---

## Project Overview

This Python project allows you to **control your music** without touching your keyboard or mouse.  
By using your webcam, it tracks your **hand gestures** in real time and performs music actions such as play, pause, next, or previous.

### What It Does
- **Play / Pause** music using your **left hand**  
- **Next song** using your **right hand (index finger and thumb pinch)**  
- **Previous song** using your **left hand (middle finger and thumb pinch)**  
- Works with `.wav` files for playback  

---

## Technologies Used

- **Python 3.8+**  
- **OpenCV** – to capture video from your webcam  
- **MediaPipe** – to detect and track your hand gestures  
- **SimpleAudio** – to play `.wav` music files  

---

## Installation & Setup

Follow these steps to run the Gesture Music Controller on your system:

### 1️. Clone or Download the Project
If you’re using Git: 
bash
git clone https://github.com/Dev-atharvak/Gesture-music-controller.git
cd Gesture-music-controller

If you downloaded the ZIP, extract it and open the folder.

### 2️. Install Required Libraries

Open your terminal or command prompt in the project folder and run:
pip install opencv-python mediapipe simpleaudio

### 3️. Add Songs

Place all your .wav music files inside the **songs** folder.

Example:
```text
gesture_music_controller/
│
├── gesture_controller.py
├── requirements.txt
├── README.md
└── songs/
    ├── song1.wav
    ├── song2.wav
    └── song3.wav
```

---

### How to Run

Run this command in your terminal:
python gesture_controller.py

Then perform the gestures below:

Hand	Gesture	Action
- left	Thumb + Index together	**Play / Pause**
- right Thumb + Index together	 **Next Song**
- right Thumb + Middle together **Previous Song**

Press Q on your keyboard anytime to quit.

---

### Usage Tips

- Use in a well-lit environment (light on your face & hands)
- Prefer a plain background for best hand tracking accuracy
- Keep your hand around 30–50 cm from the webcam
- Avoid moving too fast — hold your gesture for 0.5–1 second
- Only .wav songs are supported (convert .mp3 if needed)

---

### Folder Structure
```text
gesture_music_controller/
│
├── gesture_controller.py
├── requirements.txt
├── README.md
└── songs/
    ├── song1.wav
    └── song2.wav
```

---

### What I Learned

Real-time gesture tracking using MediaPipe Hands
Integrating OpenCV for video feed and frame processing
Playing .wav audio files with SimpleAudio
Understanding how to combine AI, vision, and creativity in Python

### Future Improvements

- Add volume control using finger distance
- Support .mp3 playback (via pygame or playsound)
- Add a small GUI with playlist view
- Improve gesture stability and speed detection

---

### License

This project is open-source and free to use for educational and personal learning purposes.
Feel free to fork and improve it!

---

## Author

**dev-atharvak (Atharva Kukade)**
Full Stack Developer | AI & Embedded Systems Enthusiast | GitHub: devbysour (https://github.com/dev-atharvak)

## FOUNDER: AkTechh Solution
### About AkTechh Solution

*AkTechh Solution* is a student-led technology initiative focused on developing innovative software, IoT, embedded systems, automation, and academic engineering projects. Our goal is to create practical, affordable, and real-world technology solutions while helping students learn, build, and showcase engineering projects with modern tools and technologies.

---

"When music meets motion, code becomes art.” 
