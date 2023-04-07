"""IO component to read from and write to the main IO stream, which defaults to the terminal."""

from colorama import Fore as __Fore

__line_number: int = 1
__TEXT_COLOR    = __Fore.RESET
__OUT_COLOR     = __Fore.GREEN
__IN_COLOR      = __Fore.YELLOW
__ERR_COLOR     = __Fore.RED

def write(obj: object) -> None:
    """Writes a line to the terminal.

    Args:
        obj (object): The object to write.
    """
    print(__OUT_COLOR + f"[{__adv_line()}] {obj}" + __TEXT_COLOR)


def read(prompt: str = "") -> str:
    """Writes a prompt and reads a line from the terminal.

    Args:
        prompt (str, optional): The prompt to write. Defaults to an empty string.

    Returns:
        str: The line read from the terminal.
    """
    return input(__IN_COLOR + f"[{__adv_line()}] {prompt}" + __TEXT_COLOR)


def __adv_line() -> int:
    """Advances the line counter by a line.

    Returns:
        int: The line number before advancing.
    """
    global __line_number
    
    __line_number += 1
    return __line_number - 1
