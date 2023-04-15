"""Main program for PyCalc."""

from modules import core
from ops import binary, bracket


def init() -> None:
    """Initializes operators and starts the core."""
    binary.init()
    bracket.init()

    core.start()


if __name__ == '__main__':
    init()
    core.loop()
