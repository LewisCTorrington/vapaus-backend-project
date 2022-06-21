from typing import Optional


class VapausException(Exception):
    def __init__(self, status_code: int, error_message: str, error_code: Optional[str] = None):
        self.status_code = status_code
        self.error_message = error_message
        self.error_code = error_code or status_code
