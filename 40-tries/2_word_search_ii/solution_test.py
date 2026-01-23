from .solution import Solution


def test_find_words_example1():
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    result = Solution().findWords(board, words)
    assert sorted(result) == sorted(["eat", "oath"])


def test_find_words_example2():
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    result = Solution().findWords(board, words)
    assert result == []
