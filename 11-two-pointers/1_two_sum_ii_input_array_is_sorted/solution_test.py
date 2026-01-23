from .solution import twoSum


def test_example_1():
    assert twoSum([2, 7, 11, 15], 9) == [1, 2]


def test_example_2():
    assert twoSum([2, 3, 4], 6) == [1, 3]


def test_example_3():
    assert twoSum([-1, 0], -1) == [1, 2]
