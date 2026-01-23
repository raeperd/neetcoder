from .solution import ListNode, reverseKGroup


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


def test_reverse_k_group_1():
    head = array_to_list([1, 2, 3, 4, 5])
    result = reverseKGroup(head, 2)
    assert list_to_array(result) == [2, 1, 4, 3, 5]


def test_reverse_k_group_2():
    head = array_to_list([1, 2, 3, 4, 5])
    result = reverseKGroup(head, 3)
    assert list_to_array(result) == [3, 2, 1, 4, 5]
