from collections import defaultdict

class Graph:
  def __init__(self, connections, directed=False):
    self.graph = defaultdict(set)
    self.directed = directed
    self.addConnections(connections)

  def addConnections(self, connections):
    for node1, node2 in connections:
      self.add(node1, node2)

  def add(self, node1, node2):
    self.graph[node1].add(node2)

    if not self.directed:
      self.graph[node2].add(node1)
    elif node2 not in self.graph:
      self.graph[node2] = set()

  def remove(self, node):
    for n, cxns in self.graph.iteritems():
      try:
        cxns.remove(node)
      except KeyError:
        pass

    try:
      del self.graph[node]
    except KeyError:
      pass

  def isConnected(self, node1, node2):
    return node1 in self.graph and node2 in self.graph[node1]

  def findPath(self, node1, node2, path=[]):
    # may not be the shortest
    path = path + [node1]
    if node1 == node2:
      return path
    if node1 not in self.graph:
      return None
    for node in self.graph[node1]:
      if node not in path:
        new_path = self.findPath(node, node2, path)
        if new_path:
          return new_path
    return None

  def __str__(self):
    return '{}({})'.format(self.__class__.__name__, dict(self.graph))

  def topSortUtil(self, currNode, visited, stack):
    visited[currNode] = True

    for node in self.graph[currNode]:
      if not visited[node]:
        self.topSortUtil(node, visited, stack)

    stack.insert(0, currNode)


  def topologicalSort(self):
    visited = {key: False for (key, value) in self.graph.items()}
    stk = []

    for node, connections in self.graph.items():
      if not visited[node]:
        self.topSortUtil(node, visited, stk)

    return stk

  def hasCycleUtil(self, currNode, visited, recStack):
    visited[currNode], recStack[currNode] == True, True

    for node in self.graph[currNode]:
      if visited[node] == False:
        if self.hasCycleUtil(node, visited, recStack):
          return True
        elif recStack[node]:
          return True

    recStack[currNode] = False
    return False

  def hasCycle(self):
    visited = {key: False for (key, value) in self.graph.items()}
    recStack = {key: False for (key, value) in self.graph.items()}

    for node, connections in self.graph.items():
      if not visited[node]:
        if self.hasCycleUtil(node, visited, recStack):
          return True

    return False

  def dfs(self, start):
    visited = {key: False for (key, value) in self.graph.items()}
    stk = [start]

    while len(stk) > 0:
      s = stk.pop()

      if not visited[s]:
        print(s, end=' ')
        visited[s] = True

      for node in self.graph[s]:
        if not visited[node]:
          stk.append(node)


if __name__ == "__main__":
  connections1 = [('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C'), ('B', 'A')]
  g1 = Graph(connections1, directed=True)
  print(g1)

  print("\nFollowing is a Topological Sort of the given graph:")
  print(g1.topologicalSort())

  print("\nFollowing is whether given directed graph has a cycle:")
  print(g1.hasCycle())

  g2 = Graph(connections1, directed=False)
  g2.dfs('B')