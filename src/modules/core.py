"""Core PyCalc calculator module responsible for managing various components."""

from modules import display
from ops.base import OperatorBase

_active: list = [False]
_reg_ops: dict = {}


def add_op(*operators: OperatorBase) -> int:
    """Registers an operator to the calculator.

    Args:
        operators (BaseArithmeticOperator): The operator to be registered.
    Returns:
        int: The number of operators registered.
    """
    for operator in operators:
        if not isinstance(operator, OperatorBase):
            raise TypeError(
                f"Wrong operator base type, expected {OperatorBase}, found {type(operator)}"
            )
        _reg_ops[operator.symbol] = operator
    return len(operators)


def active() -> bool:
    """Returns whether the core program is active or not.

    Returns:
        bool: Whether the core program is active or not.
    """
    return _active[0]


def info(print_info: bool = True) -> dict:
    """Displays internal information of the calculator program. Used for debugging purposes.

    Args:
        print_info (bool, optional): Whether information should be written to the terminal.
    """
    if print_info:
        display.write_info("Information for PyCalc:")
        display.write_info(f"  Active: {active()}")
        display.write_info(f"  Registered operators: {len(_reg_ops)}")
        if len(_reg_ops) > 0:
            display.write_info(f"    {' '.join([str(operator) for operator in _reg_ops.values()])}")
    return {
        "active": active(),
        "ops": _reg_ops.copy()
    }


def start() -> None:
    """Entry point for the calculator module."""
    if _active[0]:
        return
    _active[0] = True
    display.write("Welcome to PyCalc!")
