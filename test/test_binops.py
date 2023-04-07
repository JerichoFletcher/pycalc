"""Test script for testing binary operators."""

import pytest
from ops.binary import AddOperator, SubtractOperator, MultiplyOperator, DivideOperator


def test_add() -> None:
    """Tests the behavior of the add operator."""
    operator = AddOperator()
    with pytest.raises(TypeError):
        operator.eval('4', '6')
    with pytest.raises(ValueError):
        operator.eval(1.)
    with pytest.raises(ValueError):
        operator.eval(2., 4., 5.)
    for first_op in range(-100, 100, 1):
        for second_op in range(-100, 100, 1):
            result = operator.eval(float(first_op), float(second_op))
            assert result == first_op + second_op


def test_sub() -> None:
    """Tests the behavior of the subtract operator."""
    operator = SubtractOperator()
    with pytest.raises(TypeError):
        operator.eval('4', '6')
    with pytest.raises(ValueError):
        operator.eval(1.)
    with pytest.raises(ValueError):
        operator.eval(2., 4., 5.)
    for first_op in range(-100, 100, 1):
        for second_op in range(-100, 100, 1):
            result = operator.eval(float(first_op), float(second_op))
            assert result == first_op - second_op


def test_mul() -> None:
    """Tests the behavior of the multiply operator."""
    operator = MultiplyOperator()
    with pytest.raises(TypeError):
        operator.eval('4', '6')
    with pytest.raises(ValueError):
        operator.eval(1.)
    with pytest.raises(ValueError):
        operator.eval(2., 4., 5.)
    for first_op in range(-100, 100, 1):
        for second_op in range(-100, 100, 1):
            result = operator.eval(float(first_op), float(second_op))
            assert result == first_op * second_op


def test_div() -> None:
    """Tests the behavior of the divide operator."""
    operator = DivideOperator()
    with pytest.raises(TypeError):
        operator.eval('4', '6')
    with pytest.raises(ValueError):
        operator.eval(1.)
    with pytest.raises(ValueError):
        operator.eval(2., 4., 5.)
    for first_op in range(-100, 100, 1):
        for second_op in range(-100, 100, 1):
            if second_op == 0.:
                with pytest.raises(ZeroDivisionError):
                    operator.eval(float(first_op), float(second_op))
            else:
                result = operator.eval(float(first_op), float(second_op))
                assert result == first_op / second_op
