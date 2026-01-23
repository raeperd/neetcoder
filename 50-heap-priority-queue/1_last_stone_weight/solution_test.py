from .solution import Solution


def test_example_1():
    assert Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1


def test_example_2():
    assert Solution().lastStoneWeight([1]) == 1
