from collections import Counter


def first_unique_char(s: str) -> int:
    """
    # 387: Given a string, find the first non-repeating character in it and return it's index. 
    # If it doesn't exist, return -1.
    """
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i

    return -1


if __name__ == "__main__":
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("") == -1
    assert first_unique_char("aa") == -1

    print("Passed all tests!")
