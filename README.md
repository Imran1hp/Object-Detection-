# 🧠🎯 Real-Time Object Detection with OpenCV

Welcome to the **Real-Time Object Detection** project! This repository contains two exciting computer vision projects:

1. 😃 **Face & Eye Detection** using Haar cascades
2. 💛 **Yellow Object Detection** using HSV color masking

Both applications use **OpenCV**, **NumPy**, and **Pillow** to demonstrate real-time video processing with your webcam.

---

## 📁 Project Files


├── eyes_face_detector.py        # Detects faces and eyes in real-time
├── yellow_object_detector.py    # Detects yellow-colored objects using HSV masking
├── utlis.py                     # Helper function to get HSV color limits
├── requirement.txt              # List of required Python packages
└── README.md                    # This file!
🛠️ Requirements
Install dependencies using:

bash
Copy code
pip install -r requirement.txt
📦 Required Packages:

text
Copy code
opencv-python
numpy
pillow
👁️😃 Face & Eye Detection (eyes_face_detector.py)
This script:

Uses Haar cascades to detect faces and eyes

Draws rectangles over detected features

Opens a webcam feed

Press q to quit

✅ How to Run
bash
Copy code
python eyes_face_detector.py
🟦 Face detection → Blue box
🟩 Eye detection → Green box

💛 Yellow Object Detection (yellow_object_detector.py)
This script:

Detects yellow color using HSV color space

Uses Pillow to get bounding boxes around yellow objects

Draws rectangles over detected yellow areas

Press q to quit

✅ How to Run
bash
Copy code
python yellow_object_detector.py
🟨 Yellow objects → Green bounding box

🧠 Utility Script (utlis.py)
The get_limits(color) function helps compute HSV boundaries for BGR colors. It supports easy color-based masking.

python
Copy code
lowerLimit, upperLimit = get_limits((0, 255, 255))  # Yellow
💡 Possible Improvements
Add GUI for switching between detection modes

Save output to video or image files

Extend color detection to support multiple colors

Integrate face landmark or object tracking models

🧑‍💻 Author
Made with 🐍 Python and ❤️ Passion for Computer Vision.

