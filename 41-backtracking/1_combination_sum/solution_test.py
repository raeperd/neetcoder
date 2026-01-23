from .solution import Solution


def test_combination_sum_example1():
    candidates = [2, 3, 6, 7]
    target = 7
    result = Solution().combinationSum(candidates, target)
    expected = [[2, 2, 3], [7]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


def test_combination_sum_example2():
    candidates = [2, 3, 5]
    target = 8
    result = Solution().combinationSum(candidates, target)
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


def test_combination_sum_example3():
    candidates = [2]
    target = 1
    result = Solution().combinationSum(candidates, target)
    assert result == []
