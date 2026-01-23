from typing import Optional

from .solution import Solution, TreeNode


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


def test_is_same_tree_example1():
    p = build_tree([1, 2, 3])
    q = build_tree([1, 2, 3])
    assert Solution().isSameTree(p, q) == True


def test_is_same_tree_example2():
    p = build_tree([1, 2])
    q = build_tree([1, None, 2])
    assert Solution().isSameTree(p, q) == False


def test_is_same_tree_example3():
    p = build_tree([1, 2, 1])
    q = build_tree([1, 1, 2])
    assert Solution().isSameTree(p, q) == False
