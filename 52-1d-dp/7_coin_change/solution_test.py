from .solution import coin_change


def test_example_1():
    assert coin_change([1, 2, 5], 11) == 3


def test_example_2():
    assert coin_change([2], 3) == -1


def test_example_3():
    assert coin_change([1], 0) == 0
