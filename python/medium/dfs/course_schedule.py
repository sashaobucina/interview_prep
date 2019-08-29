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

"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

NOTE: Topological sort inspired algorithm
"""
def findOrder(numCourses: int, prerequisites: list) -> list:
  graph = createGraph(prerequisites)
  stk = []
  visited = [False] * numCourses
  recStack = [False] * numCourses

  for i in range(numCourses):
    if not visited[i]:
      if topSort(i, graph, visited, recStack, stk):
        return []
  return stk


def topSort(course, graph, visited, recStack, stack):
  visited[course] = True
  recStack[course] = True

  for prereq in graph[course]:
    if not visited[prereq]:
      if topSort(prereq, graph, visited, recStack, stack):
        return True
    elif recStack[prereq]:
      return True

  stack.append(course)
  recStack[course] = False
  return False

if __name__ == "__main__":
  # can finish
  prerequisites1 = [(1, 0)]
  print(canFinish(2, prerequisites1))

  # contains cycle, cant finish
  prerequisites2 = [(1, 0), (0, 1)]
  print(canFinish(2, prerequisites2))

  print(findOrder(2, prerequisites1))

  prerequisites3 = [(1, 0), (2, 0), (3, 1), (3, 2)]
  print(findOrder(4, prerequisites3))

  print(findOrder(2, prerequisites2))