from .solution import can_finish


def test_example_1():
    assert can_finish(2, [[1, 0]]) == True


def test_example_2():
    assert can_finish(2, [[1, 0], [0, 1]]) == False
