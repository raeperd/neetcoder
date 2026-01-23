from .solution import Solution


def test_example_1():
    assert Solution().isMatch("aa", "a") == False


def test_example_2():
    assert Solution().isMatch("aa", "a*") == True


def test_example_3():
    assert Solution().isMatch("ab", ".*") == True
