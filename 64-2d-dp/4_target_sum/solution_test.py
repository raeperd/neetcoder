from .solution import find_target_sum_ways


def test_example_1():
    assert find_target_sum_ways([1, 1, 1, 1, 1], 3) == 5


def test_example_2():
    assert find_target_sum_ways([1], 1) == 1
