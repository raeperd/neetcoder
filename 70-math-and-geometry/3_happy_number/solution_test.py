from .solution import is_happy


def test_example_1():
    assert is_happy(19) == True


def test_example_2():
    assert is_happy(2) == False
