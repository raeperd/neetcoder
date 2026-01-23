import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "hand, groupSize, expected",
    [
        ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True),
        ([1, 2, 3, 4, 5], 4, False),
    ],
)
def test_is_n_straight_hand(hand: list[int], groupSize: int, expected: bool):
    assert Solution().isNStraightHand(hand, groupSize) == expected
