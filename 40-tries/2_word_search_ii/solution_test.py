from .solution import find_words


def test_find_words_example1():
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    result = find_words(board, words)
    assert sorted(result) == sorted(["eat", "oath"])


def test_find_words_example2():
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    result = find_words(board, words)
    assert result == []
