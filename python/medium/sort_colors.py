from typing import List
from collections import defaultdict

RED = 0
WHITE = 1
BLUE = 2


def sort_colors(colors: List[int]) -> None:
    """
    # 75: Given an array with n objects colored red, white or blue, sort them in-place so that 
    objects of the same color are adjacent, with the colors in the order red, white and blue.

    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

    NOTE: You are not suppose to use the library's sort function for this problem.
    """
    # counting sort solution
    d = defaultdict(int)
    for color in colors:
        d[color] += 1

    i, color = RED, 0
    while color <= BLUE:
        if d[color] == 0:
            color += 1
            continue

        colors[i] = color
        d[color] -= 1
        i += 1


def sort_colors_one_pass(colors: List[int]) -> None:
    i = 0
    red, blue = 0, len(colors) - 1

    while i <= blue:
        if colors[i] == RED:
            colors[i], colors[red] = colors[red], colors[i]
            red += 1
            i += 1
        elif colors[i] == BLUE:
            colors[i], colors[blue] = colors[blue], colors[i]
            blue -= 1
        else:
            i += 1


if __name__ == "__main__":
    colors = [2, 0, 2, 1, 1, 0]
    sort_colors(colors)
    assert colors == [0, 0, 1, 1, 2, 2]

    colors = [2, 0, 2, 1, 1, 0]
    sort_colors_one_pass(colors)
    assert colors == [0, 0, 1, 1, 2, 2]

    print("Passed all tests!")
