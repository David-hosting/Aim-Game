from dataclasses import dataclass
from email.mime.message import MIMEMessage
import string

#@dataclass
class UnknownButton(Exception):
    """When Pressed undefinded button (somehow)"""
    def __init__(self, message : string) -> None:
        self.message = message
        super().__init__(self.message)
    # message : str
    # super().__init__(message)
