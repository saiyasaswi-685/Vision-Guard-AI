from datetime import datetime
from pathlib import Path

import cv2


def save_alert_image(frame, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_dir / f"no_helmet_{timestamp}.jpg"

    success = cv2.imwrite(str(file_path), frame)
    if not success:
        raise RuntimeError(f"Failed to save alert image to: {file_path}")

    return file_path