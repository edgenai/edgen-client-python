

from typing import Optional

from ..._models import BaseModel
from .function_parameters import FunctionParameters

__all__ = ["FunctionDefinition"]


class FunctionDefinition(BaseModel):
    name: str
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: Optional[str] = None
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Optional[FunctionParameters] = None
    """The parameters the functions accepts, described as a JSON Schema object.
    Omitting `parameters` defines a function with an empty parameter list.
    """
