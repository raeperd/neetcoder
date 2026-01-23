import pytest

from .solution import checkInclusion


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
    ],
)
def test_checkInclusion(s1, s2, expected):
    assert checkInclusion(s1, s2) == expected
