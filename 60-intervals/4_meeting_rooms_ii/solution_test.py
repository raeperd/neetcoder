import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
    ],
)
def test_min_meeting_rooms(intervals: list[list[int]], expected: int):
    assert Solution().minMeetingRooms(intervals) == expected
