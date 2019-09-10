import heapq

"""
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. 
Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, 
we choose the (worker, bike) pair with the shortest Manhattan distance between each other, 
and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the 
same shortest Manhattan distance, we choose the pair with the smallest worker index; 
if there are multiple ways to do that, we choose the pair with the smallest bike index). 
We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is 
Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike 
that the i-th worker is assigned to.

NOTE: O(n^2logn)
"""
def assign_bikes(workers: list, bikes: list) -> list:
  res = [None] * len(workers)
  heap = []
  for i, worker in enumerate(workers):
    for j, bike in enumerate(bikes):
      distance = manhattan_distance(worker, bike)
      heapq.heappush(heap, (distance, i, j))

  assigned_workers = set()
  assigned_bikes = set()
  k = 0
  while k < len(workers):
    _, worker, bike = heapq.heappop(heap)
    if worker not in assigned_workers and bike not in assigned_bikes:
      res[worker] = bike
      assigned_workers.add(worker)
      assigned_bikes.add(bike)
      k += 1

  return res

def manhattan_distance(p1: list, p2: list) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

if __name__ == "__main__":
  workers = [[0,0],[2,1]]
  bikes = [[1,2],[3,3]]
  print(assign_bikes(workers, bikes))   # expected: [1, 0]
  print(manhattan_distance([7, 0], [0, 999]))   # expected: 1006