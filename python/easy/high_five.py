import heapq
from typing import List
from collections import defaultdict


def high_five(items: List[List[int]]) -> List[List[int]]:
    """
    # 1086: Given a list of scores of different students, return the average score of each student's 
    top five scores in the order of each student's id.

    Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.

    The average score is calculated using integer division.
    """
    ans = []
    marks = defaultdict(list)

    for _id, mark in items:
        marks[_id].append(mark)

    for _id, v in marks.items():
        avg = sum(heapq.nlargest(5, v)) // 5
        ans.append([_id, avg])

    return ans


if __name__ == "__main__":
    items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [
        2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
    assert high_five(items) == [[1, 87], [2, 88]]

    print("Passed all tests!")
