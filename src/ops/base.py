"""Module containing the base operator class."""

from abc import ABC, abstractmethod


class BaseOperator(ABC):
    """Acts as a base class for all operators."""
    @property
    @abstractmethod
    def symbol(self) -> str:
        """The symbol for this operator."""

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
