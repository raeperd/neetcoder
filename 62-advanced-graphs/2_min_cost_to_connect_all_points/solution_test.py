import pytest

from .solution import minCostConnectPoints


@pytest.mark.parametrize(
    "points, expected",
    [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
    ],
)
def test_min_cost_connect_points(points: list[list[int]], expected: int):
    assert minCostConnectPoints(points) == expected
