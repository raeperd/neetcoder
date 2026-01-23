import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ],
)
def test_lengthOfLongestSubstring(s, expected):
    assert Solution().lengthOfLongestSubstring(s) == expected
