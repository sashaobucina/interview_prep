from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    # 56: Given a collection of intervals, merge all overlapping intervals.
    """
    intervals.sort(key=lambda interval: interval[0])
    merged = []

    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert merge_intervals(intervals) == [[1, 6], [8, 10], [15, 18]]

    intervals = [[1, 4], [4, 5]]
    assert merge_intervals(intervals) == [[1, 5]]

    print("Passed all tests!")
