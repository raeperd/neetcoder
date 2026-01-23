from .solution import ListNode, Solution


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def test_reorder_list_1():
    head = array_to_list([1, 2, 3, 4])
    Solution().reorderList(head)
    assert list_to_array(head) == [1, 4, 2, 3]


def test_reorder_list_2():
    head = array_to_list([1, 2, 3, 4, 5])
    Solution().reorderList(head)
    assert list_to_array(head) == [1, 5, 2, 4, 3]
