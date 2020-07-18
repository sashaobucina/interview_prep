from typing import List
from collections import defaultdict, deque


def top_sort(edges: List[List[int]]) -> List[int]:
    """
    Topological sort of incoming edges that represent a directed graph.

    Kahn's algorithm using BFS and concept of incoming edges to construct topologically sorted order.
    """
    vertices = set()
    for u, v in edges:
        vertices.add(u)
        vertices.add(v)

    in_degree = {vertex: 0 for vertex in vertices}

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    order = []
    q = deque([u for u in in_degree if in_degree[u] == 0])
    while q:
        curr = q.pop()
        order.append(curr)

        for node in graph[curr]:
            in_degree[node] -= 1
            if in_degree[node] == 0:
                q.appendleft(node)

    if len(vertices) != len(order):
        return []   # graph provided contains at least one cycle

    return order


def top_sort_dfs(edges: List[List[int]]) -> List[int]:
    """
    Topological sort using DFS and graph coloring.
    """
    order = []
    WHITE, GRAY, BLACK = 0, 1, 2

    def dfs(u: int) -> bool:
        if u in visited:
            if visited[u] == BLACK:
                return True
            if visited[u] == GRAY:
                return False

        visited[u] = GRAY

        no_cycle = True
        for v in graph.get(u, []):
            if not dfs(v):
                return False

        visited[u] = BLACK
        order.append(u)

        return True

    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

    visited = {}
    for node in graph:
        if node not in visited:
            if not dfs(node):
                return []

    return list(reversed(order))


if __name__ == "__main__":
    # regular case
    edges = [(1, 2), (2, 3), (1, 4)]
    assert top_sort(edges) in ([1, 2, 3, 4], [1, 2, 4, 3], [1, 4, 2, 3])
    assert top_sort_dfs(edges) in ([1, 2, 3, 4], [1, 2, 4, 3], [1, 4, 2, 3])

    # cycle present
    edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
    assert top_sort(edges) == top_sort_dfs(edges) == []

    print("Passed all tests!")
