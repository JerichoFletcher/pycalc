"""Test script for testing binary operators."""

from ops.binary import AddOperator
import pytest


def test_add() -> None:
    """Tests the behavior of the add operator."""
    op = AddOperator()
    res = op.eval(2, 3)
    assert res == 5
    res = op.eval(6, -18)
    assert res == -12
    with pytest.raises(TypeError):
        op.eval('4', '6')
    with pytest.raises(ValueError):
        op.eval(1)
    with pytest.raises(ValueError):
        op.eval(2, 4)
    res = op.eval(0, 0)
    assert res == 0
