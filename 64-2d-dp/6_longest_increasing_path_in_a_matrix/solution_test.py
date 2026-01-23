from .solution import longest_increasing_path


def test_example_1():
    assert longest_increasing_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4


def test_example_2():
    assert longest_increasing_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4


def test_example_3():
    assert longest_increasing_path([[1]]) == 1
