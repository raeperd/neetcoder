import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    ],
)
def test_findMin(nums, expected):
    assert Solution().findMin(nums) == expected
