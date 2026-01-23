from .solution import longestConsecutive


def test_example_1():
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4


def test_example_2():
    assert longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_example_3():
    assert longestConsecutive([1, 0, 1, 2]) == 3
