from .solution import Node, Solution


def build_graph(adj_list):
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def graph_to_adj_list(node):
    if not node:
        return []
    visited = {}
    result = []

    def dfs(n):
        if n.val in visited:
            return
        visited[n.val] = n
        while len(result) < n.val:
            result.append([])
        result[n.val - 1] = sorted([neighbor.val for neighbor in n.neighbors])
        for neighbor in n.neighbors:
            dfs(neighbor)

    dfs(node)
    return result


def test_example_1():
    adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original = build_graph(adj_list)
    cloned = Solution().cloneGraph(original)
    assert cloned is not original
    assert graph_to_adj_list(cloned) == adj_list


def test_example_2():
    adj_list = [[]]
    original = build_graph(adj_list)
    cloned = Solution().cloneGraph(original)
    assert cloned is not original
    assert graph_to_adj_list(cloned) == adj_list


def test_example_3():
    assert Solution().cloneGraph(None) is None
