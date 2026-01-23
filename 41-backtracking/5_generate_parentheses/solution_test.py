from .solution import Solution


def test_generate_parenthesis_example1():
    n = 3
    result = Solution().generateParenthesis(n)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(result) == sorted(expected)


def test_generate_parenthesis_example2():
    n = 1
    result = Solution().generateParenthesis(n)
    expected = ["()"]
    assert result == expected
