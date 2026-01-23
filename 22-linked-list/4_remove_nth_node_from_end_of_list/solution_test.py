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


def test_remove_nth_from_end_1():
    head = array_to_list([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(head, 2)
    assert list_to_array(result) == [1, 2, 3, 5]


def test_remove_nth_from_end_2():
    head = array_to_list([1])
    result = Solution().removeNthFromEnd(head, 1)
    assert list_to_array(result) == []


def test_remove_nth_from_end_3():
    head = array_to_list([1, 2])
    result = Solution().removeNthFromEnd(head, 1)
    assert list_to_array(result) == [1]
