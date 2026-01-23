from typing import Optional

from .solution import TreeNode, is_valid_bst


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


def test_is_valid_bst_example1():
    root = build_tree([2, 1, 3])
    assert is_valid_bst(root) == True


def test_is_valid_bst_example2():
    root = build_tree([5, 1, 4, None, None, 3, 6])
    assert is_valid_bst(root) == False
