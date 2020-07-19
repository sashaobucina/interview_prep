from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    # 252: Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
    (si < ei), determine if a person could attend all meetings.
    """
    if not intervals:
        return True

    intervals.sort(key=lambda x: x[0])

    last_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start < last_end:
            return False

        last_end = end

    return True


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert not can_attend_meetings(intervals)

    intervals = [[7, 10], [2, 4]]
    assert can_attend_meetings(intervals)

    print("Passed all tests!")
