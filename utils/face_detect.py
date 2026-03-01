from ultralytics import YOLO
import cv2

model = YOLO("yolov8n-face.pt")


def detect_faces(image):

    results = model(image, conf=0.4)

    boxes = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            boxes.append((x1, y1, x2, y2))

    return boxes