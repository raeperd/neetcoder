from .solution import Solution


def test_example_1():
    result = Solution().longestPalindrome("babad")
    assert result in ["bab", "aba"]


def test_example_2():
    assert Solution().longestPalindrome("cbbd") == "bb"
