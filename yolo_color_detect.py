import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

# 색깔 범위 (HSV)
COLOR_RANGES = {
    "red":    [(0, 100, 100), (10, 255, 255)],
    "blue":   [(100, 100, 100), (130, 255, 255)],
    "green":  [(40, 100, 100), (80, 255, 255)],
    "yellow": [(20, 100, 100), (35, 255, 255)],
}

def detect_color(frame, color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lo, hi = COLOR_RANGES[color]
    mask = cv2.inRange(hsv, np.array(lo), np.array(hi))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key=cv2.contourArea)
        if cv2.contourArea(c) > 500:
            x, y, w, h = cv2.boundingRect(c)
            return (x + w//2, y + h//2)
    return None

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    for color in ["red", "blue", "green", "yellow"]:
        pos = detect_color(frame, color)
        if pos:
            cv2.circle(frame, pos, 10, (255,255,255), -1)
            cv2.putText(frame, color, pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    cv2.imshow("YOLO Color Detect", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()