from .solution import twoSum


def test_example_1():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_example_2():
    assert twoSum([3, 2, 4], 6) == [1, 2]


def test_example_3():
    assert twoSum([3, 3], 6) == [0, 1]
