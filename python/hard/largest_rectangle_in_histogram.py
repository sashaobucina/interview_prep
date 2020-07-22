from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    """
    # 84: Given n non-negative integers representing the histogram's bar height where the width of each bar 
    is 1, find the area of largest rectangle in the histogram.

    This sol'n uses a monotonic stack approach!
    """
    max_area = 0
    in_stk = [-1]

    N = len(heights)
    for i in range(N):
        while in_stk[-1] != -1 and heights[in_stk[-1]] > heights[i]:
            max_area = max(
                max_area, heights[in_stk.pop()] * (i - in_stk[-1] - 1))

        in_stk.append(i)

    while in_stk[-1] != -1:
        max_area = max(max_area, heights[in_stk.pop()] * (N - in_stk[-1] - 1))

    return max_area


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    assert largest_rectangle_area(heights) == 10

    print("Passed all tests!")
