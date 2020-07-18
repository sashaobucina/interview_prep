from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    # 207: There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
    which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

    Cycle detection algorithm based off of DFS w/ graph coloring.

    Time complexity: O(|E| + |V|)
    Space compexity: O(|E| + |V|)
    """
    graph = {}
    for u, v in prerequisites:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

    visited = {}

    def dfs(u):
        if u in visited:
            return visited[u]

        visited[u] = False

        for v in graph.get(u, []):
            if not dfs(v):
                return False

        visited[u] = True
        return True

    for node in graph:
        if node not in visited:
            if not dfs(node):
                return False

    return True


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    # 210: There are a total of n courses you have to take, labeled from 0 to n-1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
    which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, return the ordering of courses 
    you should take to finish all courses.

    There may be multiple correct orders, you just need to return one of them. If it is impossible to 
    finish all courses, return an empty array.

    NOTE: Topological sort inspired algorithm

    Time complexity: O(n)
    Space complexity: O(n)
    """
    order = []
    courses = set(range(numCourses))
    cond_courses = set()

    graph = {}
    for u, v in prerequisites:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        cond_courses.add(u)
        cond_courses.add(v)

    order = []
    visited = {}

    def dfs(u):
        if u in visited:
            return visited[u]

        visited[u] = False

        for v in graph.get(u, []):
            if not dfs(v):
                return False

        visited[u] = True
        order.append(u)

        return True

    for node in graph:
        if node not in visited:
            if not dfs(node):
                return []

    return order + list(courses.difference(cond_courses))


if __name__ == "__main__":
    # course schedule I
    prerequisites = [(1, 0)]
    assert canFinish(2, prerequisites)

    prerequisites = [(1, 0), (2, 0), (3, 1), (3, 2)]
    assert canFinish(4, prerequisites)

    prerequisites = [(1, 0), (0, 1)]
    assert not canFinish(2, prerequisites)

    # course schedule II
    prerequisites = [(1, 0)]
    assert findOrder(2, prerequisites) == [0, 1]

    prerequisites = [(1, 0), (2, 0), (3, 1), (3, 2)]
    assert findOrder(4, prerequisites) == [0, 1, 2, 3]

    prerequisites = prerequisites = [(1, 0), (0, 1)]
    assert findOrder(2, prerequisites) == []

    print("Passed all tests!")
