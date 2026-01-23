from .solution import isValid


def test_example_1():
    assert isValid("()") == True


def test_example_2():
    assert isValid("()[]{}") == True


def test_example_3():
    assert isValid("(]") == False


def test_example_4():
    assert isValid("([])") == True


def test_example_5():
    assert isValid("([)]") == False
