from .solution import missing_number


def test_example_1():
    assert missing_number([3, 0, 1]) == 2


def test_example_2():
    assert missing_number([0, 1]) == 2


def test_example_3():
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
