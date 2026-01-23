from .solution import find_kth_largest


def test_example_1():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


def test_example_2():
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
