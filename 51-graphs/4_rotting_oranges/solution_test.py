from .solution import Solution


def test_example_1():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert Solution().orangesRotting(grid) == 4


def test_example_2():
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert Solution().orangesRotting(grid) == -1


def test_example_3():
    grid = [[0, 2]]
    assert Solution().orangesRotting(grid) == 0
