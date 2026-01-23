import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("eccbbbbdec", [10]),
    ],
)
def test_partition_labels(s: str, expected: list[int]):
    assert Solution().partitionLabels(s) == expected
