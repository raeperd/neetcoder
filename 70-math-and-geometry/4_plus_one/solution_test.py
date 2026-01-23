from .solution import plus_one


def test_example_1():
    assert plus_one([1, 2, 3]) == [1, 2, 4]


def test_example_2():
    assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]


def test_example_3():
    assert plus_one([9]) == [1, 0]
