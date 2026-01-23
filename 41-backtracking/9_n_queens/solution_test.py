from .solution import solve_n_queens


def test_solve_n_queens_example1():
    n = 4
    result = solve_n_queens(n)
    expected = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    assert sorted(result) == sorted(expected)


def test_solve_n_queens_example2():
    n = 1
    result = solve_n_queens(n)
    expected = [["Q"]]
    assert result == expected
