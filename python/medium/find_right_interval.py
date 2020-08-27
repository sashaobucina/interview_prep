from typing import List


def find_right_interval(intervals: List[int]) -> List[int]:
    """
    # 436: Given a set of intervals, for each of the interval i, check if there exists an interval j whose 
    start point is bigger than or equal to the end point of the interval i, which can be called that j 
    is on the "right" of i.

    For any interval i, you need to store the minimum interval j's index, which means that the interval j 
    has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't 
    exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an 
    array.

    NOTE:
        - You may assume the interval's end point is always bigger than its start point.
        - You may assume none of these intervals have the same start point.

    Time complexity: O(n * logn)
    Space complexity: O(n)
    """
    N = len(intervals)
    res = [-1 for _ in range(N)]

    d = {}
    for i, interval in enumerate(intervals):
        start, end = interval
        d[(start, end)] = i

    start_intervals = sorted(intervals, key=lambda x: x[0])
    end_intervals = sorted(intervals, key=lambda x: x[1])

    s = e = 0
    while s < N and e < N:
        start_interval = start_intervals[s]
        end_interval = end_intervals[e]

        if start_interval == end_interval:
            s += 1
            continue

        s_start, s_end = start_interval
        e_start, e_end = end_interval

        if e_end <= s_start:
            start_idx = d[(s_start, s_end)]
            end_idx = d[(e_start, e_end)]
            res[end_idx] = start_idx

            e += 1
        else:
            s += 1

    return res


def find_right_interval_bin_search(intervals: List[int]) -> List[int]:
    """
    This sol'n use binary search instead of a double sort technique.

    Time complexity: O(n * logn)
    Space complexity: O(n)
    """
    def bin_search(target: int) -> List[int]:
        l, r = 0, N - 1
        while l <= r:
            mid = l + (r - l) // 2

            if intervals[mid][0] >= target:
                r = mid - 1
            else:
                l = mid + 1

        return intervals[l] if l < N else [-1, -1]

    N = len(intervals)
    res = [-1 for _ in range(N)]

    d = {}
    for i, interval in enumerate(intervals):
        start, end = interval
        d[(start, end)] = i

    # sort based on start times
    intervals.sort(key=lambda x: x[0])

    for start, end in intervals:

        last_interval = bin_search(target=end)
        last_start, last_end = last_interval

        idx = d[(start, end)]
        if last_interval != [-1, -1]:
            last_idx = d[(last_start, last_end)]
            res[idx] = last_idx

    return res


if __name__ == "__main__":
    intervals = [[1, 2]]
    assert find_right_interval(intervals) == [-1]
    assert find_right_interval_bin_search(intervals) == [-1]

    intervals = [[3, 4], [2, 3], [1, 2]]
    assert find_right_interval(intervals) == [-1, 0, 1]
    assert find_right_interval_bin_search(intervals) == [-1, 0, 1]

    intervals = [[1, 4], [2, 3], [3, 4]]
    assert find_right_interval(intervals) == [-1, 2, -1]
    assert find_right_interval_bin_search(intervals) == [-1, 2, -1]

    intervals = [[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]]
    assert find_right_interval(intervals) == [3, 3, 3, 4, 5, -1]
    assert find_right_interval_bin_search(intervals) == [3, 3, 3, 4, 5, -1]

    print("Passed all tests!")
