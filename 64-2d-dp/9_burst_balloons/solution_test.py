from .solution import max_coins


def test_example_1():
    assert max_coins([3, 1, 5, 8]) == 167


def test_example_2():
    assert max_coins([1, 5]) == 10
