from .._models import BaseModel
from typing import List

__all__ = ["EdgenStatus"]

class EdgenStatus(BaseModel):
    active_model: str = ""
    download_ongoing: bool
    download_progress: int
    last_errors: List[str]

