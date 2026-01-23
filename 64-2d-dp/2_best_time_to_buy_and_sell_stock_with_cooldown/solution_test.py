from .solution import Solution


def test_example_1():
    assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3


def test_example_2():
    assert Solution().maxProfit([1]) == 0
