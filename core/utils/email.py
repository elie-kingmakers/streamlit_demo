import smtplib
import ssl
from pathlib import Path
from typing import List, Optional, Union

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(
    serverAddress: str,
    port: int,
    sender: str,
    password: str,
    recipients: List[str],
    messageSubject: str,
    messageText: str,
    attachmentFiles: Optional[List[Union[str, Path]]] = None,
):
    message = MIMEMultipart("alternative")
    message["Subject"] = messageSubject
    message["From"] = sender
    message["To"] = ",".join(recipients)

    message.attach(MIMEText(messageText, "plain"))

    if attachmentFiles is not None and len(attachmentFiles) != 0:
        for file in attachmentFiles:
            with open(file, "rb") as fileData:
                attachment = MIMEApplication(fileData.read())
                attachment.add_header("Content-Disposition", "attachment", filename=Path(file).name)
                message.attach(attachment)

    context = ssl.create_default_context()

    with smtplib.SMTP(serverAddress, port) as server:
        server.starttls(context=context)
        server.login(sender, password)
        server.sendmail(sender, recipients, message.as_string())
