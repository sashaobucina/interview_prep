from typing import List


def check_straight_line(coordinates: List[List[int]]) -> bool:
    """
    # 1232: You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the 
    # coordinate of a point. Check if these points make a straight line in the XY plane.
    """
    slope = None
    for i in range(1, len(coordinates)):
        x1, y1 = coordinates[i-1]
        x2, y2 = coordinates[i]
        new_slope = (y2-y1)/(x2-x1) if (x1 != x2) else float("inf")

        if slope and slope != new_slope:
            return False

        slope = new_slope

    return True


if __name__ == "__main__":
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    assert check_straight_line(coordinates)

    coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    assert not check_straight_line(coordinates)

    print("Passed all tests!")
