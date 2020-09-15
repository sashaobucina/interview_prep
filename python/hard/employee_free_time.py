from typing import List


def employee_free_time(schedule: List[List[List[int]]]) -> List[List[int]]:
    """
    # 759: We are given a list schedule of employees, which represents the working time for each employee.

    Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

    Return the list of finite intervals representing common, positive-length free time for all employees, 
    also in sorted order.

    (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. 
    For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).

    Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
    """
    OPEN, CLOSE = 0, 1

    events = []
    for emp in schedule:
        for start, end in emp:
            events.append((start, OPEN))
            events.append((end, CLOSE))

    events.sort()

    free = []
    balance, prev = 0, None
    for time, cond in events:
        if balance == 0 and prev is not None:
            free.append([prev, time])

        balance += 1 if cond == OPEN else -1
        prev = time

    return free


if __name__ == "__main__":
    schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    assert employee_free_time(schedule) == [[3, 4]]

    schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
    assert employee_free_time(schedule) == [[5, 6], [7, 9]]

    print("Passed all tests!")
