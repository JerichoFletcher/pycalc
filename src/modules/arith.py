"""Arithmetic evaluator module of PyCalc."""

from typing import Any, Optional
from ops.base import OperatorBase, ArithmeticOperatorBase, BracketOperatorBase


def evaluate(line: str, operators: dict[str, Any]) -> float:
    """
    Evaluates the given string based on the given operators.
    :param line: The string to be evaluated.
    :param operators: A dictionary containing all operator characters mapped to an operator object.
    :return: The result of the evaluation.
    """
    if not isinstance(line, str):
        raise TypeError(f"Wrong type of evaluand, expected {str}, got {type(line)}")
    for ops in operators.values():
        if not isinstance(ops, OperatorBase):
            raise TypeError(f"Wrong type of operator, expected {OperatorBase}, got {type(ops)}")

    val_stack: list[float] = []
    ops_stack: list[Any] = []

    ch_pos: int = 1
    number: Optional[float] = None

    for char in line:
        try:
            # Read number
            number = float(char) + (10 * number if number is not None else 0.)
        except ValueError:
            # Token is not a number, push previously read number
            if number is not None:
                val_stack.insert(0, number)
                number = None

            try:
                # Read operator
                read_op = operators[char]

                if isinstance(read_op, ArithmeticOperatorBase):
                    # Handle read arithmetic operator
                    if len(ops_stack) != 0:
                        peek_op = ops_stack[0]
                        while len(ops_stack) > 0 and isinstance(peek_op, ArithmeticOperatorBase) and peek_op.priority > read_op.priority:
                            try:
                                val_1 = val_stack.pop(0)
                                val_2 = val_stack.pop(0)

                                val_stack.insert(0, peek_op.eval(val_2, val_1))

                                ops_stack.pop(0)
                                if len(ops_stack) > 0:
                                    peek_op = ops_stack[0]
                            except IndexError as exc:
                                raise ValueError(f"Invalid token '{char}' at position {ch_pos}") from exc
                    ops_stack.insert(0, read_op)

                elif isinstance(read_op, BracketOperatorBase):
                    # Handle read bracket operator
                    if char == read_op.symbol_l:
                        ops_stack.insert(0, read_op)
                    elif char == read_op.symbol_r:
                        try:
                            peek_op = ops_stack[0]
                            while not isinstance(peek_op, BracketOperatorBase):
                                peek_op = ops_stack[0]
                                if isinstance(peek_op, ArithmeticOperatorBase):
                                    val_1 = val_stack.pop(0)
                                    val_2 = val_stack.pop(0)
                                    val_stack.insert(0, peek_op.eval(val_2, val_1))

                                    ops_stack.pop(0)
                                    peek_op = ops_stack[0]
                            if not isinstance(peek_op, BracketOperatorBase) or peek_op.symbol_l != read_op.symbol_l:
                                raise ValueError(f"Mismatched bracket '{peek_op.symbol_l}' versus '{read_op.symbol_r}'")
                            ops_stack.pop(0)
                        except IndexError as exc:
                            raise ValueError(f"Invalid token '{char}' at position {ch_pos}") from exc

            except KeyError as exc:
                # Invalid token
                raise ValueError(f"Invalid token '{char}' at position {ch_pos}") from exc
        ch_pos += 1

    if number is not None:
        val_stack.insert(0, number)
        number = None

    while len(ops_stack) > 0:
        peek_op = ops_stack[len(ops_stack)-1]
        if isinstance(peek_op, ArithmeticOperatorBase):
            try:
                val_1 = val_stack.pop()
                val_2 = val_stack.pop()
                val_stack.append(peek_op.eval(val_1, val_2))

                ops_stack.pop()
                if len(ops_stack) > 0:
                    peek_op = ops_stack[len(ops_stack)-1]
            except IndexError as exc:
                raise ValueError(f"Invalid string '{line}': not enough operands") from exc
        elif isinstance(peek_op, BracketOperatorBase):
            raise ValueError(f"Invalid string '{line}': unclosed bracket '{peek_op.symbol_l}'")

    if len(val_stack) != 1:
        raise ValueError(f"Invalid string '{line}': not enough operators")

    return val_stack.pop()
