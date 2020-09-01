from typing import List
from collections import Counter


def longest_substring(s: List[str], k: int) -> int:
    """
    # 395: Find the length of the longest substring T of a given string (consists of lowercase letters only) 
    such that every character in T appears no less than k times.
    """
    counter = Counter(s)

    longest = 0
    start = 0
    for i, ch in enumerate(s):
        if counter[ch] < k:
            longest = max(longest, longest_substring(s[start:i], k))
            start = i + 1

    return len(s) if start == 0 else max(longest, longest_substring(s[start:], k))


if __name__ == "__main__":
    s = "aaabb"
    assert longest_substring(s, 3) == 3

    s = "ababbc"
    assert longest_substring(s, 2) == 5

    print("Passed all tests!")
