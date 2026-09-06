import pytest

from .solution import Solution


def test_example_1():
    assert Solution().containsDuplicate([1, 2, 3, 1]) == True


def test_example_2():
    assert Solution().containsDuplicate([1, 2, 3, 4]) == False


def test_example_3():
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True


@pytest.mark.parametrize("nums, expected", [([0], False), ([-1, 0, -1], True), ([-1, 0, 1], False)])
def test_boundaries(nums, expected):
    assert Solution().containsDuplicate(nums) == expected


def test_large_input_with_duplicate_at_end():
    nums = list(range(10_000))
    assert Solution().containsDuplicate(nums) == False
    nums.append(0)
    assert Solution().containsDuplicate(nums) == True
