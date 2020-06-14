import heapq
from typing import List
from collections import defaultdict


def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    """
    # 787: There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

    Now given all the cities and flights, together with starting city src and the destination dst, 
    your task is to find the cheapest price from src to dst with up to k stops. 
    If there is no such route, output -1.
    """
    # create weighted DAG (adjacency list)
    graph = defaultdict(dict)
    for start, end, cost in flights:
        graph[start][end] = cost

    # go thru from src and mark each edges cost to get to and distance away from src
    q = []
    heapq.heappush(q, (0, src, K + 1))
    while q:
        cost, curr, stops_left = heapq.heappop(q)

        if curr == dst:
            return cost

        if stops_left > 0:
            for nxt in graph[curr]:
                nxt_cost = graph[curr][nxt]
                heapq.heappush(q, (cost + nxt_cost, nxt, stops_left - 1))

    return -1


def find_cheapest_price_bf(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    """
    Using Bellman Ford algorithm to solve.
    """
    inf = 1e9
    costs = [inf for _ in range(n)]
    costs[src] = 0

    for i in range(K + 1):
        tmp = list(costs)
        for start, end, cost in flights:
            tmp[end] = min(tmp[end], costs[start] + cost)
        costs = tmp

    return -1 if costs[dst] >= inf else costs[dst]


if __name__ == "__main__":
    flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2],
               [0, 4, 10], [3, 1, 1], [1, 4, 3]]
    assert find_cheapest_price(5, flights, src=2, dst=1, K=1) == -1
    assert find_cheapest_price_bf(5, flights, src=2, dst=1, K=1) == -1

    print("Passed all tests!")
