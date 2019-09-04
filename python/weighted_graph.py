from collections import defaultdict, deque

inf = float('inf')

class WeightedGraph:

  def __init__(self, vertices=[]):
    self._graph = defaultdict(dict)
    for vertex in vertices:
      self._graph[vertex] = {}

  def add_edge(self, v1, v2, weight, undirected=True):
    self._graph[v1][v2] = weight
    if undirected:
      self._graph[v2][v1] = weight


  def dijkstras(self, source, dest):
    unvisited = set()
    distance = {}
    previous = {}

    for vertex in self._graph:
      distance[vertex] = inf
      previous[vertex] = None
      unvisited.add(vertex)

    distance[source] = 0

    while len(unvisited) > 0:
      current = min(unvisited, key=lambda vertex: distance[vertex])
      print('Currently considering {0} with a distance of {1}'.format(current, distance[current]))
      unvisited.remove(current)

      if distance[current] == inf:
        break

      neighbors = self._graph[current]
      for vertex in neighbors:
        alt = distance[current] + neighbors[vertex]
        if alt < distance[vertex]:
          print('Updating {0} from distance of {1} to {2}'.format(vertex, distance[vertex], alt))
          distance[vertex] = alt
          previous[vertex] = current

    path, end = deque(), dest
    while previous[end] is not None:
      path.appendleft(end)
      end = previous[end]
    if path:
      path.appendleft(end)
    return path, distance[dest]


if __name__ == "__main__":
  vertices = ['a', 'b', 'c', 'd', 'e', 'f']
  edges = [("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
    ("e", "f", 9)]

  g = WeightedGraph(vertices)
  for edge in edges:
    g.add_edge(*edge)

  print(g.dijkstras("a", "e"))

