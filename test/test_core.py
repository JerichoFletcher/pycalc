"""Test script for testing the core program."""

from modules import core
from ops import binary, bracket


def test_init() -> None:
    """Tests the behavior of core initialization"""
    assert not core.active()
    core.start()
    op_count = binary.init() + bracket.init()
    info = core.info(print_info=False)
    assert info["active"]
    assert len(info["ops"]) == op_count
