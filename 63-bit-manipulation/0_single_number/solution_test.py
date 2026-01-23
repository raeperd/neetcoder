from .solution import single_number


def test_example_1():
    assert single_number([2, 2, 1]) == 1


def test_example_2():
    assert single_number([4, 1, 2, 1, 2]) == 4


def test_example_3():
    assert single_number([1]) == 1
