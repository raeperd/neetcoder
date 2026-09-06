import pytest

from .solution import Solution


def test_example_1():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_example_2():
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[0]], [[0]]),
        ([[1, 0, 3]], [[0, 0, 0]]),
        ([[1], [0], [3]], [[0], [0], [0]]),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
        ([[1, 0, 3], [4, 5, 6]], [[0, 0, 0], [4, 0, 6]]),
    ],
)
def test_boundaries_in_place(matrix, expected):
    Solution().setZeroes(matrix)
    assert matrix == expected
