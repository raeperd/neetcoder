import pytest

from .solution import Solution


def is_valid_order(order, numCourses, prerequisites):
    if len(order) != numCourses:
        return False
    if set(order) != set(range(numCourses)):
        return False
    position = {course: i for i, course in enumerate(order)}
    return all(position[prereq] < position[course] for course, prereq in prerequisites)


def test_example_1():
    result = Solution().findOrder(2, [[1, 0]])
    assert is_valid_order(result, 2, [[1, 0]])


def test_example_2():
    result = Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert is_valid_order(result, 4, [[1, 0], [2, 0], [3, 1], [3, 2]])


def test_example_3():
    result = Solution().findOrder(1, [])
    assert result == [0]


@pytest.mark.parametrize("num_courses, prerequisites", [(2, [[1, 0], [0, 1]]), (4, [[1, 0], [2, 1], [0, 2]])])
def test_cycle_has_no_order(num_courses, prerequisites):
    assert Solution().findOrder(num_courses, prerequisites) == []


@pytest.mark.parametrize("num_courses, prerequisites", [(4, []), (6, [[1, 0], [3, 2]])])
def test_disconnected_courses(num_courses, prerequisites):
    result = Solution().findOrder(num_courses, prerequisites)
    assert is_valid_order(result, num_courses, prerequisites)
