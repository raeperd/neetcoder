from .solution import unique_paths


def test_example_1():
    assert unique_paths(3, 7) == 28


def test_example_2():
    assert unique_paths(3, 2) == 3
