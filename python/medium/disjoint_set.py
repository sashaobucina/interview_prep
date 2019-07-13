"""
Disjoint-set Union/Find
"""
def disjointFind(data: list, i: int) -> int:
  if i != data[i]:
    data[i] = disjointFind(data, data[i])
  return data[i]

def union(data: list, i: int, j: int) -> None:
  pi, pj = disjointFind(data, i), disjointFind(data, j)
  if pi != pj:
    data[pi] = pj

def isConnected(data: list, i: int, j: int) -> bool:
  return disjointFind(data, i) == disjointFind(data, j)