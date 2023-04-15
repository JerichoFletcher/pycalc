"""Main program for PyCalc."""

from modules import core
from ops import binary, bracket


def init() -> None:
    """Initializes operators"""
    binary.init()
    bracket.init()


if __name__ == '__main__':
    init()
    core.start()
