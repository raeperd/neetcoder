from .solution import last_stone_weight


def test_example_1():
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1


def test_example_2():
    assert last_stone_weight([1]) == 1
