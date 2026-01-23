from .solution import least_interval


def test_example_1():
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8


def test_example_2():
    assert least_interval(["A", "C", "A", "B", "D", "B"], 1) == 6


def test_example_3():
    assert least_interval(["A", "A", "A", "B", "B", "B"], 3) == 10
