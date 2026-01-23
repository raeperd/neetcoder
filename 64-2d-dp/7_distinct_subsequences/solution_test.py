from .solution import num_distinct


def test_example_1():
    assert num_distinct("rabbbit", "rabbit") == 3


def test_example_2():
    assert num_distinct("babgbag", "bag") == 5
