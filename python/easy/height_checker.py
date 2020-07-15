from typing import List


def height_checker(heights: List[int]) -> int:
    """
    # 1051: Students are asked to stand in non-decreasing order of heights for an annual photo.

    Return the minimum number of students that must move in order for all students to be standing in 
    non-decreasing order of height.

    Notice that when a group of students is selected they can reorder in any possible way between 
    themselves and the non selected students remain on their seats.
    """
    target = sorted(heights)

    count = 0
    for i in range(len(heights)):
        if target[i] != heights[i]:
            count += 1

    return count


if __name__ == "__main__":
    heights = [1, 1, 4, 2, 1, 3]
    assert height_checker(heights) == 3

    heights = [5, 1, 2, 3, 4]
    assert height_checker(heights) == 5

    heights = [1, 2, 3, 4, 5]
    assert height_checker(heights) == 0

    print("Passed all tests!")
