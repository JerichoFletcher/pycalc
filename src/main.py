"""Main program for PyCalc."""

from modules import core
from ops import binary, bracket

if __name__ == '__main__':
    core.start()
    binary.init()
    bracket.init()
    core.info()
