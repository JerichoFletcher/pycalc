"""IO component to read from and write to the main IO stream, which defaults to the terminal."""

from colorama import Fore

class Term:
    """A class that wraps various terminal read/write functions."""
    __line_number: int = 1
    color_text    = Fore.RESET
    color_out     = Fore.GREEN
    color_in      = Fore.YELLOW
    color_err     = Fore.RED

    def write(self, obj: object) -> None:
        """Writes a line to the terminal.

        Args:
            obj (object): The object to write.
        """
        print(self.color_out + f"[{self.__adv_line()}] {obj}" + self.color_text)


    def read(self, prompt: str = "") -> str:
        """Writes a prompt and reads a line from the terminal.

        Args:
            prompt (str, optional): The prompt to write. Defaults to an empty string.

        Returns:
            str: The line read from the terminal.
        """
        return input(self.color_in + f"[{self.__adv_line()}] {prompt}" + self.color_text)


    def __adv_line(self) -> int:
        """Advances the line counter by a line.

        Returns:
            int: The line number before advancing.
        """
        self.__line_number += 1
        return self.__line_number - 1


__instance: Term = Term()

def write(obj: object) -> None:
    """Writes a line to the terminal.

    Args:
        obj (object): The object to write.
    """
    __instance.write(obj)


def read(prompt: str = "") -> str:
    """Writes a prompt and reads a line from the terminal.

    Args:
        prompt (str, optional): The prompt to write. Defaults to an empty string.

    Returns:
        str: The line read from the terminal.
    """
    return __instance.read(prompt)
