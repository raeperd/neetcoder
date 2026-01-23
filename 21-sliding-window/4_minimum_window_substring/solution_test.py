import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ],
)
def test_minWindow(s, t, expected):
    assert Solution().minWindow(s, t) == expected
