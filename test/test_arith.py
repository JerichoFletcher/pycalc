"""Test script for testing arithmetic module."""

import pytest, main
from typing import Any
from modules import arith
from ops.base import BracketOperatorBase


def create_op_map() -> dict[str, Any]:
    raw_ops = main.init()
    ops = {}
    for operator in raw_ops:
        if isinstance(operator, BracketOperatorBase):
            ops[operator.symbol_l] = operator
            ops[operator.symbol_r] = operator
        else:
            ops[operator.symbol] = operator
    return ops


def test_valid_strings_should_eval() -> None:
    """Tests the result of evaluating valid strings."""
    ops = create_op_map()
    assert arith.evaluate("1+1", ops) == 2.
    assert arith.evaluate("(2-8)/3*6/(5-3)", ops) == -6.
    assert arith.evaluate("(((1)+1+(1))+1)", ops) == 4.


def test_non_strings_should_error() -> None:
    """Tests the result of evaluating a non-string object."""
    ops = create_op_map()
    with pytest.raises(TypeError):
        arith.evaluate(None, ops)
    with pytest.raises(TypeError):
        arith.evaluate(1, ops)
    with pytest.raises(TypeError):
        arith.evaluate(["1+1", "2"], ops)


def test_invalid_strings_should_error() -> None:
    """Tests the result of evaluating invalid strings."""
    ops = create_op_map()
    with pytest.raises(ValueError):
        arith.evaluate("", ops)
    with pytest.raises(ValueError):
        arith.evaluate("+", ops)
    with pytest.raises(ValueError):
        arith.evaluate("(1+1", ops)
    with pytest.raises(ValueError):
        arith.evaluate("1+1)", ops)
    with pytest.raises(ValueError):
        arith.evaluate("hello", ops)
