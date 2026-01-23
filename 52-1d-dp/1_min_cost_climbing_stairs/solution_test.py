from .solution import Solution


def test_example_1():
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15


def test_example_2():
    assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
