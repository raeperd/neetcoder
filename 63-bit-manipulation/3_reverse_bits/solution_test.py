from .solution import Solution


def test_example_1():
    assert Solution().reverseBits(43261596) == 964176192


def test_example_2():
    assert Solution().reverseBits(2147483644) == 1073741822
