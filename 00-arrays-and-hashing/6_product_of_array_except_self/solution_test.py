from .solution import productExceptSelf


def test_example_1():
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_example_2():
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
