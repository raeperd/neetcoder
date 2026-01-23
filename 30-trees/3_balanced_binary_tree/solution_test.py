from typing import Optional

from .solution import TreeNode, is_balanced


def build_tree(values: list) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def test_is_balanced_example1():
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert is_balanced(root) == True


def test_is_balanced_example2():
    root = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    assert is_balanced(root) == False


def test_is_balanced_example3():
    root = build_tree([])
    assert is_balanced(root) == True
