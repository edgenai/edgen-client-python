from .._exceptions import EdgenError

INSTRUCTIONS = """

Edgen error:

    missing `{library}`

This feature requires additional dependencies:

    $ pip install edgen[{extra}]

"""


def format_instructions(*, library: str, extra: str) -> str:
    return INSTRUCTIONS.format(library=library, extra=extra)


class MissingDependencyError(EdgenError):
    pass
