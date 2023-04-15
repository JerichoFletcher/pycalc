"""PyCalc display component to read from and write to the main IO stream."""

from colorama import Fore
from cio import term


def write(line: str = "", color: str = Fore.GREEN) -> None:
    """
    Writes a text to the terminal.
    :param line: The text to write.
    :param color: The color to write the line in.
    """
    term.write(line, color=color)


def write_info(line: str = "") -> None:
    """
    Writes a debug info line to the terminal.
    :param line: The text to write.
    """
    term.write(line, color=Fore.BLUE)


def write_error(line: str = "") -> None:
    """
    Writes an error message line to the terminal.
    :param line: The text to write.
    """
    term.write(line, color=Fore.RED)


def read(prompt: str = "", color: str = Fore.YELLOW) -> str:
    """
    Writes a prompt and reads a line from the terminal.
    :param prompt: The prompt to write. Defaults to an empty string.
    :param color: The color to write the prompt in.
    :return: The line read from the terminal.
    """
    return term.read(prompt, color)
