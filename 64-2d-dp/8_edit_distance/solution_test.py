from .solution import min_distance


def test_example_1():
    assert min_distance("horse", "ros") == 3


def test_example_2():
    assert min_distance("intention", "execution") == 5
