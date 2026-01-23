from .solution import k_closest


def test_example_1():
    result = k_closest([[1, 3], [-2, 2]], 1)
    assert result == [[-2, 2]]


def test_example_2():
    result = k_closest([[3, 3], [5, -1], [-2, 4]], 2)
    # Either order is acceptable
    assert sorted(result) == sorted([[3, 3], [-2, 4]])
