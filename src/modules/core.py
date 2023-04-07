"""Core PyCalc calculator module responsible for managing various components."""

from modules import display

__has_started = [False]

def active() -> bool:
    """Returns whether the core program is active or not.

    Returns:
        bool: Whether the core program is active or not.
    """
    return __has_started[0]


def start() -> None:
    """Entry point for the calculator module."""
    if __has_started[0]:
        return
    __has_started[0] = True
    display.write("Welcome to PyCalc!")
