import pytest

from .solution import networkDelayTime


@pytest.mark.parametrize(
    "times, n, k, expected",
    [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ],
)
def test_network_delay_time(times: list[list[int]], n: int, k: int, expected: int):
    assert networkDelayTime(times, n, k) == expected
