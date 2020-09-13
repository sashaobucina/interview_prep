from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    # 57: Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

    You may assume that the intervals were initially sorted according to their start times.
    """
    def _merge(merge_start, idx):
        merge_end = new_end
        while idx < N:
            start, end = intervals[idx]
            if new_end < start:
                idx -= 1
                break
            if new_end < end:
                merge_end = end
                break

            idx += 1

        return [merge_start, merge_end], idx

    new_start, new_end = new_interval

    # check if new at start or end, w/ no overlap
    if not intervals:
        return [new_interval]
    if new_end < intervals[0][0]:
        return [new_interval] + intervals
    if new_start > intervals[-1][1]:
        return intervals + [new_interval]

    i, res = 0, []
    N = len(intervals)
    while i < N:
        start, end = intervals[i]

        if new_start <= end:
            new_interval, i = _merge(min(start, new_start), i)
            res.append(new_interval)
            break

        res.append(intervals[i])
        i += 1

    res += intervals[i + 1:]
    return res


if __name__ == "__main__":
    intervals = [[1, 3], [6, 9]]
    expected = [[1, 5], [6, 9]]
    assert insert(intervals, [2, 5]) == expected

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    expected = [[1, 2], [3, 10], [12, 16]]
    assert insert(intervals, [4, 8]) == expected

    print("Passed all tests!")
