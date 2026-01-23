from .solution import ListNode, Solution


def create_cycle_list(arr, pos):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    cycle_node = None
    if pos == 0:
        cycle_node = head
    for i, val in enumerate(arr[1:], 1):
        current.next = ListNode(val)
        current = current.next
        if i == pos:
            cycle_node = current
    if cycle_node:
        current.next = cycle_node
    return head


def test_linked_list_cycle_1():
    head = create_cycle_list([3, 2, 0, -4], 1)
    assert Solution().hasCycle(head) == True


def test_linked_list_cycle_2():
    head = create_cycle_list([1, 2], 0)
    assert Solution().hasCycle(head) == True


def test_linked_list_cycle_3():
    head = create_cycle_list([1], -1)
    assert Solution().hasCycle(head) == False
