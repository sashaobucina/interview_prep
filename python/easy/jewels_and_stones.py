from typing import List


def num_jewels_in_stones(J: str, S: str) -> int:
    """
    # 771: You're given strings J representing the types of stones that are jewels, and S representing the stones you have. 
    Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

    The letters in J are guaranteed distinct, and all characters in J and S are letters. 
    Letters are case sensitive, so "a" is considered a different type of stone from "A".
    """
    count = 0
    for jewel in J:
        count += S.count(jewel)

    return count


if __name__ == "__main__":
    J, S = "aA", "aAAbbbb"
    assert num_jewels_in_stones(J, S) == 3

    print("Passed all tests!")
