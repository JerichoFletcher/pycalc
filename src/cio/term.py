"""IO component to read from and write to the main IO stream, which defaults to the terminal."""

from colorama import Fore

__line_number: list[int] = [1]
COLOR_TEXT    = Fore.RESET
COLOR_OUT     = Fore.GREEN
COLOR_IN      = Fore.YELLOW
COLOR_ERR     = Fore.RED

def write( obj: object) -> None:
    """Writes a line to the terminal.

    Args:
        obj (object): The object to write.
    """
    print(COLOR_OUT + f"[{__adv_line()}] {obj}" + COLOR_TEXT)


def read( prompt: str = "") -> str:
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
    __line_number[0] += 1
    return __line_number[0] - 1
