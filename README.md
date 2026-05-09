# Helmet Detection System

Simple helmet detection project using Python, OpenCV, YOLOv8, and a Roboflow-exported dataset.

## Project structure

```text
helmet-detection-system/
|-- alerts/
|   |-- sound_alert.py
|-- captured_alerts/
|-- detection/
|   |-- helmet_detector.py
|-- models/
|-- utils/
|   |-- image_saver.py
|-- config.py
|-- data.yaml
|-- main.py
|-- requirements.txt
|-- train.py
```

## 1. Install packages

```bash
pip install -r requirements.txt
```

## 2. Prepare dataset

Export your dataset from Roboflow in YOLO format.

Then do one of these:

1. Replace the sample `data.yaml` in the project root with the Roboflow `data.yaml`.
2. Or keep the Roboflow dataset somewhere else and update `DATA_YAML_PATH` in `config.py`.

Make sure your dataset has these classes:

```yaml
names:
  0: helmet
  1: no_helmet
```

## 3. Train the model

```bash
python train.py
```

After training, the best model is expected at:

```text
models/helmet_train/weights/best.pt
```

## 4. Run real-time detection

```bash
python main.py
```

Press `q` to quit.

## Video source options

- Webcam: keep `VIDEO_SOURCE = 0` in `config.py`
- IP camera: set `VIDEO_SOURCE` to your stream URL, for example:

```python
VIDEO_SOURCE = "http://192.168.1.100:8080/video"
```

## Detection behavior

- Detects `helmet` and `no_helmet`
- Draws rectangle boxes around detected head regions
- Supports multiple people in the same frame
- Saves an image when `no_helmet` is detected
- Plays an alert sound
- Uses a 2-second cooldown to avoid repeated alerts

## Error handling included

- Missing `data.yaml`
- Missing trained model weights
- Camera open failure
- Frame read failure
- Image save failure
- Sound playback failure

## Notes

- If you want a custom sound, place `alert.wav` inside the `alerts` folder.
- On Windows, the project falls back to a simple beep if `alert.wav` is missing.
- This project works best when your dataset labels only the head or helmet area.