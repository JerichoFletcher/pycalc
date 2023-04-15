"""Module containing all available binary operators."""

from abc import ABC
from ops.base import ArithmeticOperatorBase
import ops.op_vars as var
from modules import core


class BinaryOperator(ArithmeticOperatorBase, ABC):
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

    @property
    def priority(self) -> int:
        """The priority of this operator. Higher priority operators are evaluated first."""
        return var.PRIORITY_ADD_SUB

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

    @property
    def priority(self) -> int:
        """The priority of this operator. Higher priority operators are evaluated first."""
        return var.PRIORITY_ADD_SUB

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

    @property
    def priority(self) -> int:
        """The priority of this operator. Higher priority operators are evaluated first."""
        return var.PRIORITY_MUL_DIV

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

    @property
    def priority(self) -> int:
        """The priority of this operator. Higher priority operators are evaluated first."""
        return var.PRIORITY_MUL_DIV

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


def init() -> int:
    """Initializes all binary operators.

    Returns:
        int: The number of registered operators.
    """
    return core.add_op(
        AddOperator(),
        SubtractOperator(),
        MultiplyOperator(),
        DivideOperator()
    )
