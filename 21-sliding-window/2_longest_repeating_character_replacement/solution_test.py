import pytest

from .solution import characterReplacement


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
    ],
)
def test_characterReplacement(s, k, expected):
    assert characterReplacement(s, k) == expected
