"""Module containing the base operator class."""

from abc import ABC, abstractmethod


class OperatorBase(ABC):
    """Acts as a base class for all symbolic operators."""
    @property
    @abstractmethod
    def symbol(self) -> str:
        """The symbol for this operator."""


class ArithmeticOperatorBase(OperatorBase, ABC):
    """Acts as a base class for all arithmetic operators."""
    @property
    @abstractmethod
    def arity(self) -> int:
        """The number of operands this operator requires."""

    @abstractmethod
    def eval(self, operands: list) -> float:
        """Evaluates the operation using several operands.

        Args:
            operands: The operands provided in this operation.

        Returns:
            float: The value of the operation result.
        """

    def __repr__(self) -> str:
        """Returns a string representation of the arithmetic operator."""
        return self.symbol


class BracketOperatorBase(OperatorBase, ABC):
    """Acts as a base class for all bracket operators."""
    @property
    def symbol_l(self) -> str:
        """The symbol for the left bracket."""
        return self.symbol

    @property
    @abstractmethod
    def symbol_r(self) -> str:
        """The symbol for the right bracket."""

    def __repr__(self) -> str:
        """Returns a string representation of the bracket operator."""
        return self.symbol_l + self.symbol_r
