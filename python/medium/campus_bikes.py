from typing import List


def assign_bikes(workers: list, bikes: list) -> list:
    """ # 1057: On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. 
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

    Time complexity: O(n^2logn)
    Space complexity: O(n^2)
    """
    def manhattan(p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    M, N = len(workers), len(bikes)
    distances = []

    for i in range(M):
        for j in range(N):
            distances.append((manhattan(workers[i], bikes[j]), i, j))

    distances.sort()

    d = {}
    used_bikes = set()
    for _, worker, bike in distances:
        if bike not in used_bikes and worker not in d:
            d[worker] = bike
            used_bikes.add(bike)

    return [d[k] for k in sorted(d)]


if __name__ == "__main__":
    workers = [[0, 0], [2, 1]]
    bikes = [[1, 2], [3, 3]]
    assert assign_bikes(workers, bikes) == [1, 0]

    workers = [[0, 0], [1, 1], [2, 0]]
    bikes = [[1, 0], [2, 2], [2, 1]]
    assert assign_bikes(workers, bikes) == [0, 2, 1]

    print("Passed all tests!")
