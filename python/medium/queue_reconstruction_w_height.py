from typing import List


def reconstruct_queue(people: List[List[int]]) -> List[List[int]]:
    """
    # 406: Suppose you have a random list of people standing in a queue. Each person is described by 
    a pair of integers (h, k), where h is the height of the person and k is the number of people in 
    front of this person who have a height greater than or equal to h. Write an algorithm to 
    reconstruct the queue.
    """
    q = []
    people.sort(key=_lambda)
    for p in people:
        q.insert(p[1], p)
    return q


def _lambda(person):
    return -person[0], person[1]


if __name__ == "__main__":
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    actual = reconstruct_queue(people)
    expected = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    assert actual == expected

    print("Passed all tests!")
