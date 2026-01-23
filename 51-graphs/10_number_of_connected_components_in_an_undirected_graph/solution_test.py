from .solution import count_components


def test_example_1():
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2


def test_example_2():
    assert count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
