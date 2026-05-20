# Real-Time Color Detection using OpenCV

A real-time computer vision project that detects and isolates objects based on color using OpenCV and HSV color space masking. The system processes live webcam/video feed and draws bounding boxes around detected colored objects.

---

## Features

- Real-time video processing using OpenCV
- HSV color space conversion for robust color detection
- Binary masking and thresholding
- Bounding box generation around detected objects
- Lightweight and beginner-friendly computer vision pipeline

---

## Tech Stack

- Python
- OpenCV
- PIL (Python Imaging Library)

---

## Project Workflow

1. Capture live video feed from webcam
2. Convert frames from BGR to HSV color space
3. Apply lower and upper HSV limits
4. Generate binary mask for target color
5. Detect object boundaries
6. Draw bounding boxes on detected regions
7. Display processed output in real time

---

## Code Overview

Main operations used in the project:

```python
hsvimage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsvimage, lowerlimit, upperlimit)
bbox = mask_.getbbox()
```

The system identifies the colored region and creates a rectangle around the detected object.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/color_detection.git
cd color_detection
```

### 2. Install dependencies

```bash
pip install opencv-python pillow numpy
```

### 3. Run the project

```bash
python color_detection.py
```

Press `q` to exit the video stream.

---

## Future Improvements

- Multi-color detection
- Contour-based object tracking
- FPS optimization
- Shape recognition
- Integration with YOLO/Object Detection pipelines

---

## Applications

- Object tracking
- Robotics
- Traffic signal detection
- Industrial automation
- Basic surveillance systems
