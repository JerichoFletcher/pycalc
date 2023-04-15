"""Test script for testing the core program."""

from modules import core
from ops import binary, bracket


def test_unstarted_core_should_be_inactive() -> None:
    """Tests the behavior of core before started."""
    assert not core.active()


def test_start_should_mark_core_as_active() -> None:
    """Tests the behavior of core start."""
    assert not core.active()
    core.start()
    info = core.info(print_info=False)
    assert info["active"]


def test_core_should_register_ops_successfully() -> None:
    """Tests the behavior of core operator registration."""
    op_count = binary.init() + bracket.init()
    info = core.info(print_info=False)
    assert len(info["ops"]) == op_count
