import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ],
)
def test_erase_overlap_intervals(intervals: list[list[int]], expected: int):
    assert Solution().eraseOverlapIntervals(intervals) == expected
