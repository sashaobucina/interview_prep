from collections import defaultdict

"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

NOTE: DFS cycle detection inspired algorithm
"""
def canFinish(numCourses: int, prerequisites: list) -> bool:
  graph = createGraph(prerequisites)
  visited = [False] * numCourses
  recStack = [False] * numCourses

  for i in range(numCourses):
    if not visited[i]:
      if hasCycle(i, graph, visited, recStack):
        return False
  return True

def hasCycle(course, graph, visited, recStack):
  visited[course] = True
  recStack[course] = True

  for i in graph[course]:
    if not visited[i]:
      if hasCycle(i, graph, visited, recStack):
        return True
    elif recStack[i]:
      return True

  recStack[course] = False
  return False

def createGraph(prerequisites):
  graph = defaultdict(set)
  for a, b in prerequisites:
    graph[a].add(b)
  return graph

if __name__ == "__main__":
  # can finish
  prerequisites1 = [(1, 0)]
  print(canFinish(2, prerequisites1))

  # contains cycle, cant finish
  prerequisites2 = [(1, 0), (0, 1)]
  print(canFinish(2, prerequisites2))