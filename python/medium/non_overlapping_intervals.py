from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    # 435: Given a collection of intervals, find the minimum number of intervals you need to remove to make 
    the rest of the intervals non-overlapping.
    """
    if not intervals:
        return 0

    intervals.sort()

    removals = 0
    start, end = intervals[0]
    for i in range(1, len(intervals)):
        new_start, new_end = intervals[i]

        if end > new_start:
            removals += 1

            overlap = end - new_start
            if overlap < (new_end - new_start):
                continue

        start, end = new_start, new_end

    return removals


if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    assert erase_overlap_intervals(intervals) == 1

    intervals = [[1,2],[1,2],[1,2]]
    assert erase_overlap_intervals(intervals) == 2

    intervals = [[1,2],[2,3]]
    assert erase_overlap_intervals(intervals) == 0

    print("Passed all tests!")