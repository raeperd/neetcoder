from .solution import ListNode, addTwoNumbers


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


def test_add_two_numbers_1():
    l1 = array_to_list([2, 4, 3])
    l2 = array_to_list([5, 6, 4])
    result = addTwoNumbers(l1, l2)
    assert list_to_array(result) == [7, 0, 8]


def test_add_two_numbers_2():
    l1 = array_to_list([0])
    l2 = array_to_list([0])
    result = addTwoNumbers(l1, l2)
    assert list_to_array(result) == [0]


def test_add_two_numbers_3():
    l1 = array_to_list([9, 9, 9, 9, 9, 9, 9])
    l2 = array_to_list([9, 9, 9, 9])
    result = addTwoNumbers(l1, l2)
    assert list_to_array(result) == [8, 9, 9, 9, 0, 0, 0, 1]
