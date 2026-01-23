from .solution import generate_parenthesis


def test_generate_parenthesis_example1():
    n = 3
    result = generate_parenthesis(n)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(result) == sorted(expected)


def test_generate_parenthesis_example2():
    n = 1
    result = generate_parenthesis(n)
    expected = ["()"]
    assert result == expected
