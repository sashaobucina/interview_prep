from typing import List


def num_rescue_boats(people: List[int], limit: int) -> int:
    """
    # 881: The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

    Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

    Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)
    """
    boats = 0
    people.sort()

    lo, hi = 0, len(people) - 1
    while lo <= hi:
        if people[lo] + people[hi] > limit:
            boats += 1
            hi -= 1
        else:
            boats += 1
            lo += 1
            hi -= 1

    return boats


if __name__ == "__main__":
    people = [1, 2]
    assert num_rescue_boats(people, 3) == 1

    people = [3, 2, 2, 1]
    assert num_rescue_boats(people, 3) == 3

    people = [3, 5, 3, 4]
    assert num_rescue_boats(people, 5) == 4

    print("Passed all tests")
