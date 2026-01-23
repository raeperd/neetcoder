import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
    ],
)
def test_jump(nums: list[int], expected: int):
    assert Solution().jump(nums) == expected
