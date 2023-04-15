"""Module containing all available bracket operators."""

from typing import Any
from ops.base import BracketOperatorBase


class BracketOperator(BracketOperatorBase):
    """Class for defining bracket operators."""
    def __init__(self, symbol_l: str, symbol_r: str) -> None:
        """Initializes a bracket operator instance.

        Args:
            symbol_l (str): The left bracket symbol.
            symbol_r (str): The right bracket symbol.
        """
        self.__symbol_l = symbol_l
        self.__symbol_r = symbol_r

    @property
    def symbol(self) -> str:
        """The symbol for this operator."""
        return self.__symbol_l

    @property
    def symbol_r(self) -> str:
        """The symbol for the right bracket."""
        return self.__symbol_r


def init() -> list[Any]:
    """Initializes all bracket operators.

    Returns:
        int: The number of registered operators.
    """
    return [
        BracketOperator("(", ")")
    ]
