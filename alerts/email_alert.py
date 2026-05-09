import smtplib
import os

from email.message import EmailMessage
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv


load_dotenv()


EMAIL_ADDRESS = os.getenv(
    "EMAIL_ADDRESS"
)

EMAIL_PASSWORD = os.getenv(
    "EMAIL_PASSWORD"
)


def send_email_alert(
    image_path,
    s3_url
):

    try:

        message = EmailMessage()

        message["Subject"] = (
            "Helmet Violation Detected"
        )

        message["From"] = EMAIL_ADDRESS

        message["To"] = EMAIL_ADDRESS

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        body = f"""
Helmet Violation Detected

Timestamp:
{timestamp}

Alert:
No Helmet Detected

S3 URL:
{s3_url}
"""

        message.set_content(body)

        image_path = Path(image_path)

        with open(image_path, "rb") as image_file:

            image_data = image_file.read()

            image_name = image_path.name

        message.add_attachment(
            image_data,
            maintype="image",
            subtype="jpeg",
            filename=image_name
        )

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                EMAIL_ADDRESS,
                EMAIL_PASSWORD
            )

            smtp.send_message(
                message
            )

        print(
            "Email alert sent successfully."
        )

    except Exception as error:

        print(
            f"Email Error: {error}"
        )