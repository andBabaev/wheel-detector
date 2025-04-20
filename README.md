# Wheel Detector

A deep learning-based wheel detection system using YOLOv11/12 architecture. This project aims to accurately detect and localize wheels in images and video streams.

## Description

This project implements a state-of-the-art wheel detection system using the YOLOv11/12 architecture. It's designed to:
- Detect wheels in various conditions and environments
- Process both images and video streams
- Provide real-time detection capabilities
- Support multiple wheel types and orientations

## Dependencies

- Python 3.10+ 

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/wheel-detector.git
cd wheel-detector
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

## Datasets

I used several public datasets:

- [023948023984](https://universe.roboflow.com/yash-khurana-qbt8e/023948023984/dataset/1)
- [bus-qv6ae](https://universe.roboflow.com/seokwoolee/bus-qv6ae/dataset/3)
- [car-components-dataset](https://universe.roboflow.com/sammy/car-components-dataset/dataset/11)
- [car_components_segmentation_2](https://universe.roboflow.com/gaetano/car_components_segmentation_2/dataset/6)
- [car-part-detection-with-damage-part](https://universe.roboflow.com/car-damaged-detection-e66m0/car-part-detection-with-damage-part/dataset/2)
- [eixosdecaminhao](https://universe.roboflow.com/class-h27po/eixosdecaminhao/dataset/2)
- [Vehicle Wheel Detection | Axle Detection](https://www.kaggle.com/datasets/dataclusterlabs/vehicle-wheel-detection)
- [vehicle-wheel-detection](https://universe.roboflow.com/wheels-detection/vehicle-wheel-detection-52a6u/dataset/1)
- [wheel-detector](https://github.com/mshenoda/wheel-detector/tree/main/data)
- [wheels-detection-vuaey](https://universe.roboflow.com/class-oyl7p/wheels-detection-vuaey/dataset/1)

Use `notebooks/01-dataset-preparation.ipynb` for dataset preparation

### Training

To train the model on your custom dataset:

```bash
python train.py
```

Configure parameters in config.yaml according to your needs.

### Results

| Model | mAP50 | mAP50-95 | Precision | Recall |
|-------|-------|----------|-----------|---------|
| [YOLOv11n](https://github.com/andBabaev/wheel-detector/releases/download/v1.0/yolov11n.pt) | 14.6 | 10.4 | 57.9 | 22.0 |
| [YOLOv12n](https://github.com/andBabaev/wheel-detector/releases/download/v1.0/yolov12n.pt) | 24.2 | 7.0 | 41.5 | 15.4 |
| [YOLOv12x](https://github.com/andBabaev/wheel-detector/releases/download/v1.0/yolov12x.pt) | 28.8 | 12.7 | 64.5 | 25.2 |


### Inference

Download models from the [Releases](https://github.com/andBabaev/wheel-detector/releases/tag/v1.0) page

To detect wheels in an image:

```bash
yolo predict \
model=yolov11n.pt \
imgsz=736 \
show line_width=2 show_labels=False conf=0.05 \
source="images"
```

For video processing:

```bash
yolo predict \
model=yolov11n.pt \
imgsz=736 \
show line_width=2 show_labels=False conf=0.05 \
source="your_video.mp4"
```


