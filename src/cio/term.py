"""IO component to read from and write to the main IO stream, which defaults to the terminal."""

_line_number: list = [1]
COLOR_TEXT    = '\033[0m'
COLOR_OUT     = '\033[32m'
COLOR_IN      = '\033[33m'
COLOR_ERR     = '\033[31m'


def write(obj: object) -> None:
    """Writes a line to the terminal.

    Args:
        obj (object): The object to write.
    """
    print(COLOR_OUT + f"[{__adv_line()}] {obj}" + COLOR_TEXT)


def read(prompt: str = "") -> str:
    """Writes a prompt and reads a line from the terminal.

    Args:
        prompt (str, optional): The prompt to write. Defaults to an empty string.

    Returns:
        str: The line read from the terminal.
    """
    return input(COLOR_IN + f"[{__adv_line()}] {prompt}" + COLOR_TEXT)


def __adv_line() -> int:
    """Advances the line counter by a line.

    Returns:
        int: The line number before advancing.
    """
    _line_number[0] += 1
    return _line_number[0] - 1
