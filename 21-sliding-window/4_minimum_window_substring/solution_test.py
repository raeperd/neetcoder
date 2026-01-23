import pytest

from .solution import minWindow


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ],
)
def test_minWindow(s, t, expected):
    assert minWindow(s, t) == expected
