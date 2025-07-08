"""Send emails with attachments."""
import smtplib
from email.message import EmailMessage
from pathlib import Path
from typing import Iterable


def send_email(subject: str, body: str, to: str, attachments: Iterable[Path], smtp_server: str, username: str, password: str) -> None:
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = username
    msg["To"] = to
    msg.set_content(body)

    for path in attachments:
        with open(path, "rb") as f:
            data = f.read()
        msg.add_attachment(data, maintype="application", subtype="octet-stream", filename=path.name)

    with smtplib.SMTP(smtp_server) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
