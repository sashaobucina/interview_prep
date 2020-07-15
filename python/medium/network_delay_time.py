import heapq
from typing import List
from collections import defaultdict


def network_delay_time(times: List[List[int]], N: int, K: int) -> int:
    """
    # 743: There are N network nodes, labelled 1 to N.

    Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source 
    node, v is the target node, and w is the time it takes for a signal to travel from source to target.

    Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal?
    If it is impossible, return -1.

    NOTE: This sol'n uses Dijkstra's algorithm.
    """
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
        
    dist = {}
    
    pq = [(0, K)]
    while pq:
        d, node = heapq.heappop(pq)

        if node in dist:
            continue
            
        dist[node] = d
            
        for neighbor, d2 in graph[node]:
            if neighbor not in dist:
                heapq.heappush(pq, (d + d2, neighbor))
    
    return max(dist.values()) if len(dist) == N else -1


if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    assert network_delay_time(times, N=4, K=2) == 2

    times = [[1,2,1],[2,3,2],[1,3,2]]
    assert network_delay_time(times, N=3, K=1) == 2

    print("Passed all tests!")