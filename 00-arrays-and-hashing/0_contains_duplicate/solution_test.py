from .solution import containsDuplicate


def test_example_1():
    assert containsDuplicate([1, 2, 3, 1]) == True


def test_example_2():
    assert containsDuplicate([1, 2, 3, 4]) == False


def test_example_3():
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
