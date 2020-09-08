from typing import List
from collections import Counter


def find_anagrams(s: str, p: str) -> List[int]:
    """
    # 438: Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

    Strings consists of lowercase English letters only and the length of both strings s and p will not 
    be larger than 20,100.

    The order of output does not matter.
    """
    def _check(counter):
        return all(v <= 0 for v in counter.values())

    indices = []
    start = end = 0
    count_p = Counter(p)
    for i, ch in enumerate(s):
        if end < len(p):
            if ch in count_p:
                count_p[ch] -= 1
            end += 1
        else:
            if _check(count_p):
                indices.append(start)

            start_ch, end_ch = s[start], s[end]
            if start_ch in count_p:
                count_p[start_ch] += 1
            if end_ch in count_p:
                count_p[end_ch] -= 1

            end += 1
            start += 1

    if _check(count_p):
        indices.append(start)

    return indices


if __name__ == "__main__":
    s, p = "cbaebabacd", "abc"
    assert find_anagrams(s, p) == [0, 6]

    s, p = "abab", "ab"
    assert find_anagrams(s, p) == [0, 1, 2]

    print("Passed all tests!")
