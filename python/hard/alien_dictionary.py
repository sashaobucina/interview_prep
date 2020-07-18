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


def alien_order_dfs(words: List[str]) -> str:
    """
    This implementaion of alien dictionary uses a DFS topological sort of letters to order lexicographically.
    """
    GRAY, BLACK = 1, 2
    graph = {ch: [] for word in words for ch in word}

    for first, second in zip(words, words[1:]):
        should_continue = False
        for ch1, ch2 in zip(first, second):
            if ch1 != ch2:
                graph[ch1].append(ch2)

                should_continue = True
                break

        if not should_continue and len(second) < len(first):
            return ""

    order = []
    visited = {}

    def dfs(u):
        if u in visited:
            if visited[u] == BLACK:
                return True
            if visited[u] == GRAY:
                return False

        visited[u] = GRAY

        for v in graph.get(u, []):
            if not dfs(v):
                return False

        visited[u] = BLACK
        order.append(u)

        return True

    if not all(dfs(node) for node in graph):
        return ""

    return "".join(reversed(order))


if __name__ == "__main__":
    words = [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]
    assert alien_order(words) == alien_order_dfs(words) == "wertf"

    words = ["z", "x"]
    assert alien_order(words) == alien_order_dfs(words) == "zx"

    words = ["z", "x", "z"]
    assert alien_order(words) == alien_order_dfs(words) == ""

    print("Passed all tests!")
