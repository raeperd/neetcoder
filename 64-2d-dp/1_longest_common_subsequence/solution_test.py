from .solution import Solution


def test_example_1():
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3


def test_example_2():
    assert Solution().longestCommonSubsequence("abc", "abc") == 3


def test_example_3():
    assert Solution().longestCommonSubsequence("abc", "def") == 0
