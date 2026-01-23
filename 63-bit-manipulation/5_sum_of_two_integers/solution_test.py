from .solution import Solution


def test_example_1():
    assert Solution().getSum(1, 2) == 3


def test_example_2():
    assert Solution().getSum(2, 3) == 5
