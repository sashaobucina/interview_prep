from typing import List
from collections import deque, defaultdict


def alien_order(words: List[str]) -> str:
    """
    # 269: There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. 

    You receive a list of non-empty words from the dictionary, where words are sorted lexicographically 
    by the rules of this new language. 

    Derive the order of letters in this language.
    """
    graph = defaultdict(set)
    indegrees = {ch: 0 for word in words for ch in word}

    for first, second in zip(words, words[1:]):
        should_continue = False
        for ch1, ch2 in zip(first, second):
            if ch1 != ch2:
                if ch2 not in graph[ch1]:
                    graph[ch1].add(ch2)
                    indegrees[ch2] += 1

                should_continue = True
                break
                
        if not should_continue and len(second) < len(first):
            return ""

    order = []
    q = deque([ch for ch in indegrees if indegrees[ch] == 0])
    while q:
        ch = q.pop()
        order.append(ch)

        for ch2 in graph[ch]:
            indegrees[ch2] -= 1
            if indegrees[ch2] == 0:
                q.appendleft(ch2)

    if len(order) == len(indegrees):
        return "".join(order)

    return ""


if __name__ == "__main__":
    words = [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]
    assert alien_order(words) == "wertf"

    words = ["z", "x"]
    assert alien_order(words) == "zx"

    words = ["z", "x", "z"]
    assert alien_order(words) == ""

    print("Passed all tests!")
