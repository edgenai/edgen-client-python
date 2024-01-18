

from ..._models import BaseModel

__all__ = ["Transcription"]


class Transcription(BaseModel):
    text: str
