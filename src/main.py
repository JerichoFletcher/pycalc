"""Main program for PyCalc."""

from typing import Any
from modules import core
from ops import binary, bracket


def init() -> list[Any]:
    """
    Collects all operators and returns a list.
    :return: A list containing all operators to be registered.
    """
    return binary.init() + bracket.init()


if __name__ == '__main__':
    core.init(init)
    core.run()
