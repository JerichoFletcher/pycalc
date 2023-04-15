"""Core PyCalc calculator module responsible for managing various components."""

from typing import Callable, Any
from modules import display
from ops.base import OperatorBase

_active: list[bool] = [False]
_reg_ops: dict[str, Any] = {}


def add_op(*operators: OperatorBase) -> int:
    """Registers an operator to the calculator.

    :param operators: The operator to be registered.
    :return: The number of operators registered.
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

    :return: Whether the core program is active or not.
    """
    return _active[0]


def info(print_info: bool = True) -> dict[str, Any]:
    """Displays internal information of the calculator program. Used for debugging purposes.

    :param print_info: Whether information should be written to the terminal.
    :return: A dictionary containing information stored in the core program.
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


def init(initializer: Callable[[], None]) -> None:
    """Initializes the core program.

    :param initializer: A callable initialization function.
    """
    if active():
        return
    _active[0] = True
    initializer()


def run() -> None:
    """Runs the calculator. Will raise an error if the core program has not been initialized yet."""
    if not active():
        raise RuntimeError("Core has not been initialized yet.")

    display.write("Welcome to PyCalc! Input the expression you want to evaluate below, or 'exit' to :")
    _loop()
    display.write("Thank you for using PyCalc!")


def _loop() -> None:
    """Main loop for the calculator module."""
    while True:
        inp = display.read("Expression: ").lower()
        if inp != "exit":
            # Temporary
            display.write(inp)
        else:
            break
