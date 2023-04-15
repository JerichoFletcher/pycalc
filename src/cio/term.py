"""IO component to read from and write to the main IO stream, which defaults to the terminal."""

_line_number: list[int] = [1]

COLOR_RESET = '\033[0m'


def write(obj: object, color: str = COLOR_RESET) -> None:
    """
    Writes a line to the terminal.
    :param obj: The object to write.
    :param color: The color to write the line in.
    """
    print(f"{color}[{__adv_line()}] {obj}{COLOR_RESET}")


def read(prompt: str = "", color: str = COLOR_RESET) -> str:
    """
    Writes a prompt and reads a line from the terminal.
    :param prompt: The prompt to write. Defaults to an empty string.
    :param color: The color to write the prompt in.
    :return: The line read from the terminal.
    """
    return input(f"{color}[{__adv_line()}] {prompt}{COLOR_RESET}")


def __adv_line() -> int:
    """
    Advances the line counter by a line.
    :return: The line number before advancing.
    """
    _line_number[0] += 1
    return _line_number[0] - 1
