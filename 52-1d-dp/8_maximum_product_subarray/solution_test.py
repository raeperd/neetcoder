from .solution import max_product


def test_example_1():
    assert max_product([2, 3, -2, 4]) == 6


def test_example_2():
    assert max_product([-2, 0, -1]) == 0
