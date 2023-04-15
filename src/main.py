"""Main program for PyCalc."""

from modules import core
from ops import binary, bracket


def init() -> None:
    """Initializes operators and starts the core."""
    binary.init()
    bracket.init()


if __name__ == '__main__':
    core.init(init)
    core.run()
