from .solution import Solution


def test_example_1():
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == True


def test_example_2():
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") == False


def test_example_3():
    assert Solution().isInterleave("", "", "") == True
