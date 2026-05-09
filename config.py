from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

# Training settings
DATA_YAML_PATH = BASE_DIR / "data.yaml"
PRETRAINED_MODEL = "yolov8s.pt"
TRAIN_PROJECT_DIR = BASE_DIR / "models"
TRAIN_RUN_NAME = "helmet_train"
MODEL_WEIGHTS = TRAIN_PROJECT_DIR / TRAIN_RUN_NAME / "weights" / "best.pt"
EPOCHS = 50
IMAGE_SIZE = 640
BATCH_SIZE = 8

# Detection settings
VIDEO_SOURCE = 0
CONFIDENCE_THRESHOLD = 0.5
ALERT_COOLDOWN_SECONDS = 2
WINDOW_NAME = "Helmet Detection"

# Output settings
CAPTURED_ALERTS_DIR = BASE_DIR / "captured_alerts"
ALERT_SOUND_FILE = BASE_DIR / "alerts" / "alert.wav"

# Class names expected from the Roboflow dataset
HELMET_CLASS_NAME = "helmet"
NO_HELMET_CLASS_NAME = "no_helmet"