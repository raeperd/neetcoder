import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
    ],
)
def test_checkInclusion(s1, s2, expected):
    assert Solution().checkInclusion(s1, s2) == expected
