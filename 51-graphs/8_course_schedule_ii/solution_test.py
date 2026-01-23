from .solution import Solution


def is_valid_order(order, numCourses, prerequisites):
    if len(order) != numCourses:
        return False
    if set(order) != set(range(numCourses)):
        return False
    position = {course: i for i, course in enumerate(order)}
    return all(position[prereq] <= position[course] for course, prereq in prerequisites)


def test_example_1():
    result = Solution().findOrder(2, [[1, 0]])
    assert is_valid_order(result, 2, [[1, 0]])


def test_example_2():
    result = Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert is_valid_order(result, 4, [[1, 0], [2, 0], [3, 1], [3, 2]])


def test_example_3():
    result = Solution().findOrder(1, [])
    assert result == [0]
