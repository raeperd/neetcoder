from .solution import max_profit


def test_example_1():
    assert max_profit([1, 2, 3, 0, 2]) == 3


def test_example_2():
    assert max_profit([1]) == 0
