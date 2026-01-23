from .solution import get_sum


def test_example_1():
    assert get_sum(1, 2) == 3


def test_example_2():
    assert get_sum(2, 3) == 5
