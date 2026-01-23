import pytest

from .solution import findDuplicate


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([3, 3, 3, 3, 3], 3),
    ],
)
def test_findDuplicate(nums, expected):
    assert findDuplicate(nums) == expected
