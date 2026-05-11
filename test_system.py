from pathlib import Path


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