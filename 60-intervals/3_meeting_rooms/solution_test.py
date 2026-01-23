import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[7, 10], [2, 4]], True),
    ],
)
def test_can_attend_meetings(intervals: list[list[int]], expected: bool):
    assert Solution().canAttendMeetings(intervals) == expected
