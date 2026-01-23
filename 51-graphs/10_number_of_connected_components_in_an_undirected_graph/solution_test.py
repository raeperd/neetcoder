from .solution import Solution


def test_example_1():
    assert Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2


def test_example_2():
    assert Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
