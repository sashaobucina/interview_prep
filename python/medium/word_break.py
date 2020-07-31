from typing import List
from collections import deque


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    # 139: Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
    determine if s can be segmented into a space-separated sequence of one or more dictionary words.

    NOTE:
        - The same word in the dictionary may be reused multiple times in the segmentation.
        - You may assume the dictionary does not contain duplicate words.

    Complexity Analysis:
        This solution uses BFS and memoization.
            - Time complexity: O(n^2)
            - Space complexity: O(n)
    """
    N = len(s)

    # convert wordDict into a hash set for quick lookup
    word_set = set(word_dict)

    # keep track of visited indices, no need to do work again
    visited = [False] * N

    q = deque([0])
    while q:
        idx = q.pop()

        if idx > N:
            continue

        if idx == N:
            return True

        if not visited[idx]:
            for word in word_set:
                end_idx = idx + len(word)
                if s[idx:end_idx] in word_set:
                    q.appendleft(end_idx)

        visited[idx] = True

    return False


if __name__ == "__main__":
    s = "leetcode"
    word_dict = ["leet", "code"]
    assert word_break(s, word_dict)

    s = "applepenapple"
    word_dict = ["apple", "pen"]
    assert word_break(s, word_dict)

    s = "catsandog"
    word_dict = ["cats", "dog", "sand", "and", "cat"]
    assert not word_break(s, word_dict)

    print("Passed all tests!")
