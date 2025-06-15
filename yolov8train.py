from ultralytics import YOLO
model=YOLO('yolov8s.pt')
model.train(
    data='data.yaml', 
    epochs=5,
    batch=8,
    name="aircraftdetector"
)  