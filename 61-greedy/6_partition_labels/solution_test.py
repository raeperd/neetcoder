import pytest

from .solution import partitionLabels


@pytest.mark.parametrize(
    "s, expected",
    [
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("eccbbbbdec", [10]),
    ],
)
def test_partition_labels(s: str, expected: list[int]):
    assert partitionLabels(s) == expected
