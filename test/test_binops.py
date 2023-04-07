"""Test script for testing binary operators."""

import pytest
from ops.binary import AddOperator


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
