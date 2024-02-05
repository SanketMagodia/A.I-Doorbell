
# AI Doorbell System


## Description

This project implements an intelligent doorbell system utilizing YOLOv5 for object detection. It categorizes visitors and packages between distinct classes (e.g., person, Walmart delivery, parcel, mail) and alerts the homeowner via email or phone.

## Demo

![alt text](https://github.com/SanketMagodia/A.I-Doorbell/blob/master/Screenshot%202023-05-13%20204644.png)

## Key Features

- Real-time object detection using YOLOv5
- Customizable class recognition
- Efficient server-client architecture
- Flexible email/phone notifications

- Open-source framework (YOLOv5, Flask)

## System Architecture

1. **Client:**
   - Captures video frames (OpenCV)
   - Detects motion changes
   - Sends frames to server
2. **Server:**
   - Receives frames
   - Performs object detection (YOLOv5)
   - Classifies detected objects
   - Sends bounding boxes/labels back
3. **Client:**
   - Receives detection results
   - Triggers email/phone alerts





## Prerequisites
- Python 3.x
- OpenCV
- Flask
- YOLOv5 (https://github.com/ultralytics/yolov5)
Ensure you have the required dependencies installed by running

```bash
  pip install -r requirements.txt
```


## Usage/Examples
### 1. Clone the repository
```bash
git clone https://github.com/SanketMagodia/A.I-Doorbell.git
```
### 2. install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the server
in ./API
```bash
python app.py
```
### 3. Run the client on derired edge device
in ./client
```bash
python app.py
```
### Notes
Consider cloud storage, user authentication, and more robust notification mechanisms.
Ensure compliance with privacy and security regulations.

## Contributions
### Contributions are welcome! If you have any suggestions, feature requests, or improvements, feel free to open an issue or submit a pull request.
