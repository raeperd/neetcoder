from .solution import Solution


def test_example_1():
    assert Solution().maxCoins([3, 1, 5, 8]) == 167


def test_example_2():
    assert Solution().maxCoins([1, 5]) == 10
