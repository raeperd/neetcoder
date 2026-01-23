import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("(*)", True),
        ("(*))", True),
    ],
)
def test_check_valid_string(s: str, expected: bool):
    assert Solution().checkValidString(s) == expected
