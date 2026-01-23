from .solution import Solution


def test_example_1():
    assert Solution().countBits(2) == [0, 1, 1]


def test_example_2():
    assert Solution().countBits(5) == [0, 1, 1, 2, 1, 2]
