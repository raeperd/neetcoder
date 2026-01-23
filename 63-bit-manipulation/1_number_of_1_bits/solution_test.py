from .solution import Solution


def test_example_1():
    assert Solution().hammingWeight(11) == 3


def test_example_2():
    assert Solution().hammingWeight(128) == 1


def test_example_3():
    assert Solution().hammingWeight(2147483645) == 30
