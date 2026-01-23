import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
    ],
)
def test_characterReplacement(s, k, expected):
    assert Solution().characterReplacement(s, k) == expected
