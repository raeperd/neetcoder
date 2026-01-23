import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "gas, cost, expected",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
    ],
)
def test_can_complete_circuit(gas: list[int], cost: list[int], expected: int):
    assert Solution().canCompleteCircuit(gas, cost) == expected
