from .solution import Node, Solution


def build_graph(adj_list):
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def collect_nodes(node, expected_count):
    if node is None:
        assert expected_count == 0
        return {}
    by_value = {}
    visited = set()
    pending = [node]
    while pending:
        current = pending.pop()
        if id(current) in visited:
            continue
        visited.add(id(current))
        assert len(visited) <= expected_count, "Clone contains extra nodes"
        assert current.val not in by_value, "A graph node was copied more than once"
        by_value[current.val] = current
        pending.extend(current.neighbors)
    assert len(by_value) == expected_count
    return by_value


def assert_deep_copy(adj_list):
    original = build_graph(adj_list)
    original_nodes = collect_nodes(original, len(adj_list))
    snapshot = [(node, node.val, list(node.neighbors)) for node in original_nodes.values()]

    cloned = Solution().cloneGraph(original)
    copied_nodes = collect_nodes(cloned, len(adj_list))

    assert {id(node) for node in original_nodes.values()}.isdisjoint(id(node) for node in copied_nodes.values())
    assert set(copied_nodes) == set(original_nodes)
    if original is not None:
        assert cloned.val == original.val
    for val, node in copied_nodes.items():
        assert sorted(neighbor.val for neighbor in node.neighbors) == sorted(adj_list[val - 1])
    for node, val, neighbors in snapshot:
        assert node.val == val
        assert len(node.neighbors) == len(neighbors)
        assert all(actual is expected for actual, expected in zip(node.neighbors, neighbors))


def test_example_1():
    assert_deep_copy([[2, 4], [1, 3], [2, 4], [1, 3]])


def test_example_2():
    assert_deep_copy([[]])


def test_example_3():
    assert_deep_copy([])


def test_two_connected_nodes():
    assert_deep_copy([[2], [1]])


def test_shared_neighbor():
    assert_deep_copy([[2, 3], [1, 3], [1, 2]])
