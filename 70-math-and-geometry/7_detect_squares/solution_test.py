from .solution import DetectSquares


def test_example_1():
    detect_squares = DetectSquares()
    detect_squares.add([3, 10])
    detect_squares.add([11, 2])
    detect_squares.add([3, 2])
    assert detect_squares.count([11, 10]) == 1
    assert detect_squares.count([14, 8]) == 0
    detect_squares.add([11, 2])
    assert detect_squares.count([11, 10]) == 2
