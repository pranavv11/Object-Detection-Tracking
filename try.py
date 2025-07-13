from ultralytics import YOLO

model = YOLO("Models/`yolov8_best.pt")
print(model.names) 