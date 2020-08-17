from typing import List


def distribute_candies(candies: List[int]) -> int:
    """
    # 575: You have n candies, the ith candy is of type candies[i].

    You want to distribute the candies equally between a sister and a brother so that each of them gets 
    n / 2 candies (n is even). The sister loves to collect different types of candies, so you want to give 
    her the maximum number of different types of candies.

    Return the maximum number of different types of candies you can give to the sister.
    """
    s = set()
    for candy in candies:
        s.add(candy)

    return min(len(s), len(candies) // 2)


if __name__ == "__main__":
    candies = [1, 1, 2, 2, 3, 3]
    assert distribute_candies(candies) == 3

    candies = [1, 1, 2, 3]
    assert distribute_candies(candies) == 2

    candies = [1, 1]
    assert distribute_candies(candies) == 1

    candies = [2, 2]
    assert distribute_candies(candies) == 1

    candies = [1, 11]
    assert distribute_candies(candies) == 1

    print("Passed all tests!")
