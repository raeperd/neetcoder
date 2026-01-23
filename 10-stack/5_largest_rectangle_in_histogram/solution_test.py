from .solution import Solution


def test_example_1():
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10


def test_example_2():
    assert Solution().largestRectangleArea([2, 4]) == 4
