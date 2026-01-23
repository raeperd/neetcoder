from .solution import Solution


def test_example_1():
    assert Solution().canFinish(2, [[1, 0]]) == True


def test_example_2():
    assert Solution().canFinish(2, [[1, 0], [0, 1]]) == False
