"""PyCalc display component to read from and write to the main IO stream."""

from cio import term

COLOR_RESET = '\033[0m'
COLOR_BLACK = '\033[30m'
COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = '\033[33m'
COLOR_BLUE = '\033[34m'
COLOR_MAGENTA = '\033[35m'
COLOR_CYAN = '\033[36m'
COLOR_WHITE = '\033[37m'


def write(line: str = "", color: str = COLOR_GREEN) -> None:
    """Writes a text to the terminal.

    Args:
        line (str, optional): The text to write.
        color (str, optional): The color to write the line in.
    """
    term.write(line, color=color)


def write_info(line: str = "") -> None:
    """Writes a debug info line to the terminal.

    Args:
        line (str, optional): The text to write.
    """
    term.write(line, color=COLOR_BLUE)


def read(prompt: str = "", color: str = COLOR_YELLOW) -> str:
    """Writes a prompt and reads a line from the terminal.

    Args:
        prompt (str, optional): The prompt to write. Defaults to an empty string.
        color (str, optional): The color to write the prompt in.

    Returns:
        str: The line read from the terminal.
    """
    return term.read(prompt, color)
