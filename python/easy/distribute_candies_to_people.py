from typing import List


def distribute_candies(candies: int, num_people: int) -> List[int]:
    """
    # 1103: We distribute some number of candies, to a row of n = num_people people in the following way:

    We then give 1 candy to the first person, 2 candies to the second person, and so on until we give 
    n candies to the last person.

    Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies 
    to the second person, and so on until we give 2 * n candies to the last person.

    This process repeats (with us giving one more candy each time, and moving to the start of the row 
    after we reach the end) until we run out of candies. The last person will receive all of our 
    remaining candies (not necessarily one more than the previous gift).

    Return an array (of length num_people and sum candies) that represents the final distribution of candies.
    """
    arr = [0] * num_people

    idx, inc = 0, 1
    while candies - inc > 0:
        arr[idx] += inc

        candies -= inc
        inc += 1
        idx = (idx + 1) % num_people

    arr[idx] += candies
    return arr


if __name__ == "__main__":
    assert distribute_candies(7, 4) == [1, 2, 3, 1]
    assert distribute_candies(10, 3) == [5, 2, 3]

    print("Passed all tests!")
