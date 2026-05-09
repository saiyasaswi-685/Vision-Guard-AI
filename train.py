from ultralytics import YOLO

import config


def main() -> None:
    if not config.DATA_YAML_PATH.exists():
        raise FileNotFoundError(
            f"data.yaml not found at: {config.DATA_YAML_PATH}. "
            "Replace the sample file with your Roboflow-exported data.yaml or update config.py."
        )

    model = YOLO(config.PRETRAINED_MODEL)
    model.train(
        data=str(config.DATA_YAML_PATH),
        epochs=config.EPOCHS,
        imgsz=config.IMAGE_SIZE,
        batch=config.BATCH_SIZE,
        project=str(config.TRAIN_PROJECT_DIR),
        name=config.TRAIN_RUN_NAME,
        exist_ok=True,
    )

    print("Training complete.")
    print(f"Best weights should be available at: {config.MODEL_WEIGHTS}")


if __name__ == "__main__":
    main()