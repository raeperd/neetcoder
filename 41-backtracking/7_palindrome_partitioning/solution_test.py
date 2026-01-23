from .solution import partition


def test_partition_example1():
    s = "aab"
    result = partition(s)
    expected = [["a", "a", "b"], ["aa", "b"]]
    assert sorted(result) == sorted(expected)


def test_partition_example2():
    s = "a"
    result = partition(s)
    expected = [["a"]]
    assert result == expected
