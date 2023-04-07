"""Module containing all available binary operators."""

from abc import ABC
from ops.base import BaseOperator
from modules import core


class BinaryOperator(BaseOperator, ABC):
    """Acts as a base class for all binary operators."""
    @property
    def arity(self) -> int:
        """The number of operands this operator requires."""
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
        if not isinstance(operands[0], float):
            raise TypeError(f"Wrong operand type, expected {float}, got {type(operands[0])}")
        return operands[0] + operands[1]


class SubtractOperator(BinaryOperator):
    """Operator for performing binary subtraction."""
    @property
    def symbol(self) -> str:
        """The symbol for this operator."""
        return "-"

    def eval(self, *operands: float) -> float:
        """Evaluates the operation using several operands.

        Args:
            operands (tuple): The operands provided in this operation.

        Returns:
            float: The value of the operation result.
        """
        if len(operands) != self.arity:
            raise ValueError(f"Wrong operand count, expected {self.arity}, got {len(operands)}")
        if not isinstance(operands[0], float):
            raise TypeError(f"Wrong operand type, expected {float}, got {type(operands[0])}")
        return operands[0] - operands[1]


class MultiplyOperator(BinaryOperator):
    """Operator for performing binary multiplication."""
    @property
    def symbol(self) -> str:
        """The symbol for this operator."""
        return "*"

    def eval(self, *operands: float) -> float:
        """Evaluates the operation using several operands.

        Args:
            operands (tuple): The operands provided in this operation.

        Returns:
            float: The value of the operation result.
        """
        if len(operands) != self.arity:
            raise ValueError(f"Wrong operand count, expected {self.arity}, got {len(operands)}")
        if not isinstance(operands[0], float):
            raise TypeError(f"Wrong operand type, expected {float}, got {type(operands[0])}")
        return operands[0] * operands[1]


class DivideOperator(BinaryOperator):
    """Operator for performing binary division."""
    @property
    def symbol(self) -> str:
        """The symbol for this operator."""
        return "/"

    def eval(self, *operands: float) -> float:
        """Evaluates the operation using several operands.

        Args:
            operands (tuple): The operands provided in this operation.

        Returns:
            float: The value of the operation result.
        """
        if len(operands) != self.arity:
            raise ValueError(f"Wrong operand count, expected {self.arity}, got {len(operands)}")
        if not isinstance(operands[0], float):
            raise TypeError(f"Wrong operand type, expected {float}, got {type(operands[0])}")
        return operands[0] / operands[1]


core.add_op(AddOperator())
core.add_op(SubtractOperator())
core.add_op(MultiplyOperator())
core.add_op(DivideOperator())
