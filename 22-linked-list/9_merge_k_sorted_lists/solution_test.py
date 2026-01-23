from .solution import ListNode, mergeKLists


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


def test_merge_k_sorted_lists_1():
    lists = [
        array_to_list([1, 4, 5]),
        array_to_list([1, 3, 4]),
        array_to_list([2, 6]),
    ]
    result = mergeKLists(lists)
    assert list_to_array(result) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_merge_k_sorted_lists_2():
    lists = []
    result = mergeKLists(lists)
    assert list_to_array(result) == []


def test_merge_k_sorted_lists_3():
    lists = [array_to_list([])]
    result = mergeKLists(lists)
    assert list_to_array(result) == []
