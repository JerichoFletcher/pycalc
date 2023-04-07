"""PyCalc display component to read from and write to the main IO stream."""

from cio import term

def write(obj: str) -> None:
    """Writes a text to the terminal.

    Args:
        x (str): The text to write.
    """
    term.write(obj)

def read(prompt: str = "") -> str:
    """Writes a prompt and reads a line from the terminal.

    Args:
        prompt (str, optional): The prompt to write. Defaults to an empty string.

    Returns:
        str: The line read from the terminal.
    """
    return term.read(prompt)
