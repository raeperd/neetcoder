from .solution import Solution

INF = 2147483647


def test_example_1():
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    Solution().islandsAndTreasure(rooms)
    expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
    assert rooms == expected


def test_example_2():
    rooms = [[-1]]
    Solution().islandsAndTreasure(rooms)
    assert rooms == [[-1]]


def test_example_3():
    rooms = [[INF]]
    Solution().islandsAndTreasure(rooms)
    assert rooms == [[INF]]


def test_example_4():
    rooms = [[0]]
    Solution().islandsAndTreasure(rooms)
    assert rooms == [[0]]
