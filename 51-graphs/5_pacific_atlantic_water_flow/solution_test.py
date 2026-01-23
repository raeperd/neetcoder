from .solution import Solution


def test_example_1():
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    result = Solution().pacificAtlantic(heights)
    expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert sorted(result) == sorted(expected)


def test_example_2():
    heights = [[1]]
    result = Solution().pacificAtlantic(heights)
    assert result == [[0, 0]]
