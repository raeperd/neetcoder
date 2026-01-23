from .solution import Node, copyRandomList


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


def list_to_data(head):
    if not head:
        return []
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    result = []
    for node in nodes:
        random_idx = None
        if node.random:
            random_idx = nodes.index(node.random)
        result.append([node.val, random_idx])
    return result


def test_copy_random_list_1():
    head = create_random_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    result = copyRandomList(head)
    assert list_to_data(result) == [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]


def test_copy_random_list_2():
    head = create_random_list([[1, 1], [2, 1]])
    result = copyRandomList(head)
    assert list_to_data(result) == [[1, 1], [2, 1]]


def test_copy_random_list_3():
    head = create_random_list([[3, None], [3, 0], [3, None]])
    result = copyRandomList(head)
    assert list_to_data(result) == [[3, None], [3, 0], [3, None]]
