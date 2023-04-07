"""Core PyCalc calculator module responsible for managing various components."""

from modules import display
from ops.base import BaseOperator

_has_started: list = [False]
_reg_ops: dict = {}


def add_op(op: BaseOperator) -> None:
    """Registers an operator to the calculator.

    Args:
        op (BaseOperator): The operator to be registered.
    """
    _reg_ops[op.symbol] = op


def active() -> bool:
    """Returns whether the core program is active or not.

    Returns:
        bool: Whether the core program is active or not.
    """
    return _has_started[0]


def start() -> None:
    """Entry point for the calculator module."""
    if _has_started[0]:
        return
    _has_started[0] = True
    _reg_ops.clear()
    display.write("Welcome to PyCalc!")
