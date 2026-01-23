import pytest

from .solution import checkValidString


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("(*)", True),
        ("(*))", True),
    ],
)
def test_check_valid_string(s: str, expected: bool):
    assert checkValidString(s) == expected
