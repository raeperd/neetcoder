from .solution import Solution


def test_example_1():
    assert Solution().isHappy(19) == True


def test_example_2():
    assert Solution().isHappy(2) == False
