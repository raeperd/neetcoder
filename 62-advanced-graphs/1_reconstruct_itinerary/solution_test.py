import pytest

from .solution import findItinerary


@pytest.mark.parametrize(
    "tickets, expected",
    [
        ([["MU", "LHR"], ["JFK", "MU"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MU", "LHR", "SFO", "SJC"]),
        (
            [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        ),
    ],
)
def test_find_itinerary(tickets: list[list[str]], expected: list[str]):
    assert findItinerary(tickets) == expected
