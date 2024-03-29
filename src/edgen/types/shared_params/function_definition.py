

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...types import shared_params

__all__ = ["FunctionDefinition"]


class FunctionDefinition(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: shared_params.FunctionParameters
    """The parameters the functions accepts, described as a JSON Schema object.

    Omitting `parameters` defines a function with an empty parameter list.
    """
