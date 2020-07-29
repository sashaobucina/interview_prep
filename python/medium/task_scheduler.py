import heapq
from typing import List
from collections import Counter, deque


def least_interval(tasks: List[int], n: int) -> int:
    """
    # 621: You are given a char array representing tasks CPU need to do. It contains capital letters A to Z 
    where each letter represents a different task. Tasks could be done without the original order of the array.

    Each task is done in one unit of time.
    For each unit of time, the CPU could complete either one task or just be idle.

    However, there is a non-negative integer n that represents the cooldown period between two same tasks 
    (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

    You need to return the least number of units of times that the CPU will take to finish all the given tasks.
    """
    if n == 0:
        return len(tasks)

    # construct max heap, to get most common task first
    count = Counter(tasks)
    priority = [(-freq, item) for item, freq in count.items()]
    heapq.heapify(priority)

    # task queue
    q = deque([None] * n)

    ans = 0
    while count:
        if priority:
            _, curr_task = heapq.heappop(priority)
            q.appendleft(curr_task)

            count[curr_task] -= 1
            if count[curr_task] == 0:
                del count[curr_task]
        else:
            q.appendleft(None)

        # take oldest task and put it back in priority
        task = q.pop()
        if task is not None and task in count:
            heapq.heappush(priority, (-count[task], task))

        ans += 1

    return ans


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    assert least_interval(tasks, 2) == 8

    tasks = ["A", "A", "A", "B", "B", "B"]
    assert least_interval(tasks, 0) == 6

    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    assert least_interval(tasks, 2) == 16

    print("Passed all tests!")
