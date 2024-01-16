from __future__ import annotations

import sys
from typing import TYPE_CHECKING, List, Optional, cast
from argparse import ArgumentParser
from typing_extensions import Literal, NamedTuple

from ..._utils import get_client
from ..._models import BaseModel

def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("misc.version.create")

    sub._action_groups.pop()
    sub.set_defaults(func=CLIMiscVersion.create)


