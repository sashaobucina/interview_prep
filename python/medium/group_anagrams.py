from typing import List
from collections import defaultdict


def group_anagrams_by_sort(strs: List[str]) -> List[List[str]]:
    """
    # 49: Given an array of strings, group anagrams together.

    NOTE: Can use categorization by sorted strings; anagrams will have equivalent sorted strings.
    """
    d = defaultdict(list)
    for s in strs:
        d["".join(sorted(s))].append(s)

    return list(d.values())


def group_anagrams_by_count(strs: List[List[int]]) -> List[List[str]]:
    """
    NOTE: Can use categorization by character counts.
    """
    d = defaultdict(list)
    for s in strs:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        d[tuple(counts)].append(s)

    return list(d.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    actual_by_sort = group_anagrams_by_sort(strs)
    actual_by_count = group_anagrams_by_count(strs)
    expected = sorted([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

    assert sorted(actual_by_sort) == sorted(actual_by_count) == expected

    print("Passed all tests!")
