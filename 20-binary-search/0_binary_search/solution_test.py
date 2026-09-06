import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], 4, -1),
        ([5], 6, -1),
        ([1, 3], 1, 0),
        ([1, 3], 3, 1),
        ([1, 3], 2, -1),
        ([-9, -5, -1, 0, 3], -9, 0),
        ([-9, -5, -1, 0, 3], 3, 4),
    ],
)
def test_search(nums, target, expected):
    assert Solution().search(nums, target) == expected
