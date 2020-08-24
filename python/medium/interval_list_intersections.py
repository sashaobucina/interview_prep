from typing import List


def interval_intersection(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    # 986: Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

    Return the intersection of these two interval lists.

    (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b. 
    The intersection of two closed intervals is a set of real numbers that is either empty, or can be 
    represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
    """
    if not A or not B:
        return []

    a, b = 0, 0
    intersect = []
    len_A, len_B = len(A), len(B)

    while a < len_A and b < len_B:
        a_x, a_y = A[a]
        b_x, b_y = B[b]

        # no interval intersection
        if a_y < b_x:
            a += 1
        elif b_y < a_x:
            b += 1

        # contained interval
        elif a_x >= b_x and a_y <= b_y:
            intersect.append(A[a])
            a += 1
        elif b_x >= a_x and b_y <= a_y:
            intersect.append(B[b])
            b += 1

        # parital contained interval
        elif a_x < b_x and a_y < b_y:
            intersect.append([b_x, a_y])
            a += 1
        elif b_x < a_x and b_y < a_y:
            intersect.append([a_x, b_y])
            b += 1

    return intersect


if __name__ == "__main__":
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    assert interval_intersection(A, B) == [[1, 2], [5, 5], [8, 10], [15, 23],
                                           [24, 24], [25, 25]]

    print("Passed all tests!")
