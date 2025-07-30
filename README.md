# 👁️🧠 Eyes and Face Detector using OpenCV

A real-time computer vision project that uses OpenCV to detect **faces** and **eyes** via your webcam. Built with Python, this project demonstrates how to apply Haar Cascade Classifiers for object detection!

---

## 🚀 Features

- 🎥 Real-time webcam feed
- 😃 Face detection using Haar cascades
- 👀 Eye detection within detected faces
- 🧰 Easy-to-read modular code
- ⌨️ Quit the stream with a single key press (`q`)

---

## 🛠️ Requirements

Install the dependencies from `requirement.txt`:

```bash
pip install -r requirement.txt
Contents of requirement.txt:

text
Copy code
opencv-python
numpy
pillow
📁 Project Structure
plaintext
Copy code
├── eyes_face_detector.py  # Main script for real-time detection
├── utlis.py               # Helper function for color limit conversion (HSV)
├── requirement.txt        # Required packages
└── README.md              # You're reading it!
🧪 How It Works
Face Detection: Uses haarcascade_frontalface_default.xml to locate faces in frames.

Eye Detection: Uses haarcascade_eye.xml to locate eyes inside detected face regions.

Drawing Boxes: Detected features are marked using colored rectangles (blue for face, green for eyes).

Helper (utlis.py): Contains a function to compute HSV limits for color filtering (not used in the main script but reusable).

▶️ Usage
Run the following command in your terminal:

bash
Copy code
python eyes_face_detector.py
A window will open with your webcam feed showing face and eye detection.

Press q to quit the program.

📸 Preview
(Add screenshots or a demo GIF here if available)

✨ Future Improvements
Add screenshot capture feature 📷

Save detected faces for training models

Use deep learning models for improved accuracy (e.g. DNN or MTCNN)

👨‍💻 Author
Made with ❤️ using OpenCV & Python