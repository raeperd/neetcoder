import pytest

from .solution import mergeTriplets


@pytest.mark.parametrize(
    "triplets, target, expected",
    [
        ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], True),
        ([[3, 4, 5], [4, 5, 6]], [3, 2, 5], False),
        ([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5], True),
    ],
)
def test_merge_triplets(triplets: list[list[int]], target: list[int], expected: bool):
    assert mergeTriplets(triplets, target) == expected
