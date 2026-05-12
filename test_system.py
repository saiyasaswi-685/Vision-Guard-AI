from pathlib import Path
from aws.s3_uploader import S3Uploader


def test_captured_alerts_folder():

    folder = Path(
        "captured_alerts"
    )

    assert folder.exists()


def test_log_file_creation():

    log_file = Path(
        "s3_logs.csv"
    )

    assert log_file.exists()


def test_s3_uploader_creation():

    uploader = S3Uploader()

    assert uploader is not None