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


def test_merge_two_sorted_lists_1():
    list1 = array_to_list([1, 2, 4])
    list2 = array_to_list([1, 3, 4])
    result = Solution().mergeTwoLists(list1, list2)
    assert list_to_array(result) == [1, 1, 2, 3, 4, 4]


def test_merge_two_sorted_lists_2():
    list1 = array_to_list([])
    list2 = array_to_list([])
    result = Solution().mergeTwoLists(list1, list2)
    assert list_to_array(result) == []


def test_merge_two_sorted_lists_3():
    list1 = array_to_list([])
    list2 = array_to_list([0])
    result = Solution().mergeTwoLists(list1, list2)
    assert list_to_array(result) == [0]
