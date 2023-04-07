"""Module containing all available binary operators."""

from abc import ABC
from ops.base import BaseOperator
from modules import core


class BinaryOperator(BaseOperator, ABC):
    """Acts as a base class for all operators."""
    @property
    def arity(self) -> int:
        return 2


class AddOperator(BinaryOperator):
    """Operator for performing binary addition."""
    @property
    def symbol(self) -> str:
        """The symbol for this operator."""
        return "+"

    def eval(self, *operands: float) -> float:
        """Evaluates the operation using several operands.

        Args:
            operands (tuple): The operands provided in this operation.

        Returns:
            float: The value of the operation result.
        """
        if len(operands) != self.arity:
            raise ValueError(f"Wrong operand count, expected {self.arity}, got {len(operands)}")
        if operands[0] is not float:
            raise TypeError(f"Wrong operand type, expected {type(float)}, got {type(operands[0])}")
        return operands[0] + operands[1]

