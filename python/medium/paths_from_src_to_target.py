from typing import List


def all_paths(graph: List[List[int]]) -> List[List[int]]:
    """
    # 797: Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, 
    and return them in any order.

    The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of 
    all nodes j for which the edge (i, j) exists.
    """
    paths = []
    N = len(graph)

    def dfs(src, path):
        if src == N - 1:
            paths.append(path)

        for neighbor in graph[src]:
            dfs(neighbor, path + [neighbor])

    dfs(0, [0])
    return paths


if __name__ == "__main__":
    """
    The graph looks like this:
    0--->1
    |    |
    v    v
    2--->3

    There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
    """
    graph = [[1, 2], [3], [3], []]
    all_paths(graph) == [[0, 1, 3], [0, 2, 3]]

    print("Passed all tests!")
