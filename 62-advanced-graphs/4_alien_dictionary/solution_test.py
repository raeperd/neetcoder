import pytest

from .solution import alienOrder


@pytest.mark.parametrize(
    "words, expected",
    [
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
        (["z", "x"], "zx"),
        (["z", "x", "z"], ""),
    ],
)
def test_alien_order(words: list[str], expected: str):
    assert alienOrder(words) == expected
