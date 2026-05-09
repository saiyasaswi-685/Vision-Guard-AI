import time
import cv2

import config

from alerts.sound_alert import SoundAlert
from alerts.email_alert import send_email_alert
from detection.helmet_detector import HelmetDetector
from utils.image_saver import save_alert_image
from aws.s3_uploader import S3Uploader


def open_video_source(source):

    if isinstance(source, str) and source.isdigit():
        source = int(source)

    capture = cv2.VideoCapture(source)

    if not capture.isOpened():
        raise RuntimeError(
            f"Unable to open video source: {source}"
        )

    return capture


def main():

    capture = None

    try:

        detector = HelmetDetector(
            model_path=config.MODEL_WEIGHTS,
            confidence_threshold=config.CONFIDENCE_THRESHOLD
        )

        sound_alert = SoundAlert()

        s3_uploader = S3Uploader()

        capture = open_video_source(
            config.VIDEO_SOURCE
        )

        last_alert_time = 0

        while True:

            success, frame = capture.read()

            if not success:

                print(
                    "Failed to read frame from camera."
                )

                break

            detections, annotated_frame = detector.detect(
                frame
            )

            has_no_helmet = False

            for detection in detections:

                label = detection["label"]

                if label == config.NO_HELMET_CLASS_NAME:

                    has_no_helmet = True

            current_time = time.time()

            if has_no_helmet:

                if (
                    current_time - last_alert_time
                    >= config.ALERT_COOLDOWN_SECONDS
                ):

                    saved_path = save_alert_image(
                        annotated_frame,
                        config.CAPTURED_ALERTS_DIR
                    )

                    print(
                        f"Saved image: {saved_path}"
                    )

                    s3_url = s3_uploader.upload_file(
                        saved_path
                    )

                    print(
                        f"Uploaded to S3: {s3_url}"
                    )

                    send_email_alert(
                        saved_path,
                        s3_url
                    )

                    sound_alert.play()

                    last_alert_time = current_time

            cv2.imshow(
                config.WINDOW_NAME,
                annotated_frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):

                break

    except Exception as error:

        print(error)

    finally:

        if capture is not None:

            capture.release()

        cv2.destroyAllWindows()


if __name__ == "__main__":

    main()