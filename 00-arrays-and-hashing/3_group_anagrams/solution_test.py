from .solution import groupAnagrams


def test_example_1():
    result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort each group and sort the list of groups for comparison
    result = [sorted(group) for group in result]
    result = sorted(result)
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    expected = sorted(expected)
    assert result == expected


def test_example_2():
    assert groupAnagrams([""]) == [[""]]


def test_example_3():
    assert groupAnagrams(["a"]) == [["a"]]
