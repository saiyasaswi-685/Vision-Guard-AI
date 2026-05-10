import boto3
import os
import csv

from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()


LOG_FILE = Path("s3_logs.csv")


class S3Uploader:

    def __init__(self):

        self.bucket_name = "helmet-alert-images"

        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv(
                "AWS_ACCESS_KEY"
            ),
            aws_secret_access_key=os.getenv(
                "AWS_SECRET_KEY"
            ),
            region_name="us-east-1"
        )

    def upload_file(
        self,
        file_path
    ):

        file_path = Path(file_path)

        self.s3.upload_file(
            str(file_path),
            self.bucket_name,
            file_path.name,
            ExtraArgs={
                "ContentType": "image/jpeg"
            }
        )

        file_url = (
            f"https://{self.bucket_name}.s3.amazonaws.com/{file_path.name}"
        )

        self.log_s3_upload(
            file_path.name,
            file_url
        )

        return file_url

    def log_s3_upload(
        self,
        image_name,
        s3_url
    ):

        file_exists = LOG_FILE.exists()

        with open(
            LOG_FILE,
            mode="a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            if not file_exists:

                writer.writerow([
                    "timestamp",
                    "image_name",
                    "s3_url"
                ])

            writer.writerow([
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                image_name,
                s3_url
            ])