from .solution import carFleet


def test_example_1():
    assert carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3


def test_example_2():
    assert carFleet(10, [3], [3]) == 1


def test_example_3():
    assert carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
