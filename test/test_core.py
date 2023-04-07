"""Test script for testing the core program."""

from modules import core

def test_active() -> None:
    """Tests the behavior of core.active()"""
    assert not core.active()
    core.start()
    assert core.active()
