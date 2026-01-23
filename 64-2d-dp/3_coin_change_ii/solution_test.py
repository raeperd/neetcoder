from .solution import change


def test_example_1():
    assert change(5, [1, 2, 5]) == 4


def test_example_2():
    assert change(3, [2]) == 0


def test_example_3():
    assert change(10, [10]) == 1
