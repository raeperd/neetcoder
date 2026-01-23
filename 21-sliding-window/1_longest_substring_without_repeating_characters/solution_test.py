import pytest

from .solution import lengthOfLongestSubstring


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ],
)
def test_lengthOfLongestSubstring(s, expected):
    assert lengthOfLongestSubstring(s) == expected
