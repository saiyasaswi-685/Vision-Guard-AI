from pathlib import Path
from typing import Dict, List, Tuple

import cv2
from ultralytics import YOLO

import config


DetectionResult = Dict[str, object]


class HelmetDetector:
    def __init__(self, model_path: Path, confidence_threshold: float = 0.5) -> None:
        if not model_path.exists():
            raise FileNotFoundError(
                f"Model weights not found at: {model_path}. Train the model first or update config.MODEL_WEIGHTS."
            )

        self.model = YOLO(str(model_path))
        self.confidence_threshold = confidence_threshold

    def detect(self, frame) -> Tuple[List[DetectionResult], object]:
        results = self.model.predict(frame, conf=self.confidence_threshold, verbose=False)
        detections: List[DetectionResult] = []
        annotated_frame = frame.copy()

        for result in results:
            boxes = result.boxes
            names = result.names

            for box in boxes:
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                label = names[class_id]
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

                detections.append(
                    {
                        "label": label,
                        "confidence": confidence,
                        "bbox": (x1, y1, x2, y2),
                    }
                )

                color = self._get_box_color(label)
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)

                label_text = f"{label} {confidence:.2f}"
                cv2.putText(
                    annotated_frame,
                    label_text,
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    color,
                    2,
                )

        return detections, annotated_frame

    @staticmethod
    def _get_box_color(label: str):
        if label == config.NO_HELMET_CLASS_NAME:
            return (0, 0, 255)
        return (0, 255, 0)