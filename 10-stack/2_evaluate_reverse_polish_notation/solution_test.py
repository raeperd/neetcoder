from .solution import evalRPN


def test_example_1():
    assert evalRPN(["2", "1", "+", "3", "*"]) == 9


def test_example_2():
    assert evalRPN(["4", "13", "5", "/", "+"]) == 6


def test_example_3():
    assert evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
