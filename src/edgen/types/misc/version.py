from ..._models import BaseModel

__all__ = ["Version"]


class Version(BaseModel):
    major: int
    minor: int
    patch: int
    build: str = ""
