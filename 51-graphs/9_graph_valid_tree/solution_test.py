from .solution import valid_tree


def test_example_1():
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True


def test_example_2():
    assert valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
