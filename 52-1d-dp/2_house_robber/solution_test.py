from .solution import Solution


def test_example_1():
    assert Solution().rob([1, 2, 3, 1]) == 4


def test_example_2():
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
