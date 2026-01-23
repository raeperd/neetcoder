from .solution import Solution


def test_example_1():
    assert Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True


def test_example_2():
    assert Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
