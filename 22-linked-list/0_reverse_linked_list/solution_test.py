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


def test_reverse_linked_list_1():
    head = array_to_list([1, 2, 3, 4, 5])
    result = Solution().reverseList(head)
    assert list_to_array(result) == [5, 4, 3, 2, 1]


def test_reverse_linked_list_2():
    head = array_to_list([1, 2])
    result = Solution().reverseList(head)
    assert list_to_array(result) == [2, 1]


def test_reverse_linked_list_empty():
    head = array_to_list([])
    result = Solution().reverseList(head)
    assert list_to_array(result) == []
