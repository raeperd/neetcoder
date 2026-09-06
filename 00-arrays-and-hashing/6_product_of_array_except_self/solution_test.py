import pytest

from .solution import Solution


def test_example_1():
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_example_2():
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 3], [3, 2]), ([0, 4], [4, 0]), ([0, 0, 3], [0, 0, 0]), ([-1, -2, -3], [6, 3, 2])],
)
def test_boundaries(nums, expected):
    assert Solution().productExceptSelf(nums) == expected
