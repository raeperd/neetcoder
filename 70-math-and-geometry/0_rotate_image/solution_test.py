import pytest

from .solution import Solution


def test_example_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_example_2():
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]


@pytest.mark.parametrize("matrix, expected", [([[1]], [[1]]), ([[1, 2], [3, 4]], [[3, 1], [4, 2]])])
def test_small_matrix_in_place(matrix, expected):
    Solution().rotate(matrix)
    assert matrix == expected
