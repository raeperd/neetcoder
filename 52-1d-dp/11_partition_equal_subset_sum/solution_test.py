from .solution import can_partition


def test_example_1():
    assert can_partition([1, 5, 11, 5]) == True


def test_example_2():
    assert can_partition([1, 2, 3, 5]) == False
