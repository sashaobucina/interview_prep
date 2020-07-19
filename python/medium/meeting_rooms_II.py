import heapq
from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    # 253: Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
    (si < ei), find the minimum number of conference rooms required.

    This implementation uses a heap (priority queue).

    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    free_rooms = []
    heapq.heappush(free_rooms, intervals[0][1])

    for start, end in intervals[1:]:
        if free_rooms[0] <= start:
            heapq.heappop(free_rooms)

        heapq.heappush(free_rooms, end)

    return len(free_rooms)


def min_meeting_rooms_greedy(intervals: List[List[int]]) -> int:
    """
    This implementation sorts by start and end times, and uses a 2 ptr approach (chronological ordering).

    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    if not intervals:
        return 0

    used_rooms = 0

    # sort start and end times individually
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])

    start_ptr = end_ptr = 0
    while start_ptr < len(intervals):
        # if meeting ended by time of new meeting start time, free up room and update end time
        if start_times[start_ptr] >= end_times[end_ptr]:
            used_rooms -= 1
            end_ptr += 1

        # a room is always used irrespective of it got freed up, go to next start time of meeting
        used_rooms += 1
        start_ptr += 1

    return used_rooms


if __name__ == "__main__":
    intervals = [[9, 10], [4, 9], [4, 17]]
    assert min_meeting_rooms(intervals) == 2
    assert min_meeting_rooms_greedy(intervals) == 2

    intervals = [[0, 30], [5, 10], [15, 20]]
    assert min_meeting_rooms(intervals) == 2
    assert min_meeting_rooms_greedy(intervals) == 2

    intervals = [[7, 10], [2, 4]]
    assert min_meeting_rooms(intervals) == 1
    assert min_meeting_rooms_greedy(intervals) == 1

    print("Passed all tests!")
