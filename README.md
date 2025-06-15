

```markdown
# Aircraft Detection using YOLOv8 and the MADD Dataset

This repository contains a full pipeline for detecting military aircraft in aerial images using the MADD (Military Aircraft Detection Dataset). The solution is built with Ultralytics YOLOv8 and includes dataset structuring, training configuration, and model deployment scripts.

## Features

- Custom training on the MADD dataset  
- YOLOv8s-based detection (with optional support for other YOLOv8 variants)  
- Automated folder structure setup for image-label alignment  
- Ready-to-use inference script  
- Lightweight and modular code  

## Folder Structure

```

madd-aircraft-detection/
├── dataset/
│   ├── images/
│   │   └── train/
│   └── labels/
│       └── train/
├── yolov8train.py
├── folderstructure.py
├── data.yaml
├── runs/                 # (optional: for logs and checkpoints)
└── README.md

````

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/madd-aircraft-detection.git
cd madd-aircraft-detection
````

### 2. Install Dependencies

```bash
pip install ultralytics
```

### 3. Prepare the Dataset

Update the `source_images_root` and `source_labels` in `folderstructure.py` to point to your local dataset folders.

Then run:

```bash
python folderstructure.py
```

This organizes all images and labels into the correct YOLOv8 format.

## Training

To train the model on the prepared dataset:

```bash
python yolov8train.py
```

By default, this uses `yolov8s.pt`, 5 epochs, and a batch size of 8. You can adjust these parameters inside the script.

## Inference

Once training is complete, you can run inference using Ultralytics YOLOv8 CLI or a custom script:

```python
from ultralytics import YOLO

model = YOLO('runs/detect/aircraftdetector/weights/best.pt')
results = model('path/to/test/image.jpg')
results.show()
```

## Acknowledgements

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* MADD: Military Aircraft Detection Dataset

## License

This project is licensed under the MIT License.


