import pytest

from .solution import Node, Solution


def create_random_list(data):
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]
    for i, (_, random_idx) in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]
    return nodes[0]


def collect_nodes(head, expected_length):
    nodes = []
    node = head
    for _ in range(expected_length):
        assert node is not None, "List is shorter than expected"
        nodes.append(node)
        node = node.next
    assert node is None, "List is longer than expected or contains a next-pointer cycle"
    return nodes


def assert_deep_copy(data):
    head = create_random_list(data)
    original = collect_nodes(head, len(data))
    snapshot = [(node.val, node.next, node.random) for node in original]

    result = Solution().copyRandomList(head)
    copied = collect_nodes(result, len(data))

    assert {id(node) for node in original}.isdisjoint(id(node) for node in copied)
    for node, (val, random_idx) in zip(copied, data):
        assert node.val == val
        assert node.random is (None if random_idx is None else copied[random_idx])
    for node, (val, next_node, random_node) in zip(original, snapshot):
        assert node.val == val
        assert node.next is next_node
        assert node.random is random_node


def test_copy_random_list_1():
    assert_deep_copy([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])


def test_copy_random_list_2():
    assert_deep_copy([[1, 1], [2, 1]])


def test_copy_random_list_3():
    assert_deep_copy([[3, None], [3, 0], [3, None]])


@pytest.mark.parametrize("data", [[], [[0, None]], [[-1, 0]], [[7, 1], [7, 0]]])
def test_copy_random_list_boundaries(data):
    assert_deep_copy(data)
