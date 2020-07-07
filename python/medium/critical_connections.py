from typing import Dict, List, Set
from collections import defaultdict


def critical_connections(n: int, connections: List[List[int]]) -> List[List[int]]:
    """
    # 1192: There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections 
    forming a network where connections[i] = [a, b] represents a connection between servers a and b. 
    Any server can reach any other server directly or indirectly through the network.

    A critical connection is a connection that, if removed, will make some server unable to reach some other server.

    Return all critical connections in the network in any order.

    NOTE:
    - 1 <= n <= 10^5
    - n-1 <= connections.length <= 10^5
    - connections[i][0] != connections[i][1]
    - There are no repeated connections

    This sol'n produces TLE!
    """
    # create graph represented thru adjacency list
    network = defaultdict(set)
    for c1, c2 in connections:
        network[c1].add(c2)
        network[c2].add(c1)

    # disconnect a connection, check if network still fully connected
    critical_conns = []
    for conn in connections:
        c1, c2 = conn
        network[c1].remove(c2)
        network[c2].remove(c1)

        # check if connected, if not add to list
        if not _is_connected(n, network):
            critical_conns.append(conn)

        network[c1].add(c2)
        network[c2].add(c1)

    return critical_conns


def _is_connected(n: int, network: Dict[int, Set]) -> bool:
    visited = [False] * (n + 1)
    stk = [1]
    while stk:
        server = stk.pop()
        visited[server] = True

        for conn_server in network[server]:
            if not visited[conn_server]:
                stk.append(conn_server)

    return all(visited[1:])


if __name__ == "__main__":
    n = 9
    connections = [[1, 2], [2, 3], [3, 4], [4, 5], [
        5, 6], [6, 7], [7, 8], [2, 8], [2, 6], [1, 9]]
    expected = [[1, 2], [1, 9]]
    assert critical_connections(n, connections) == [[1, 2], [1, 9]]

    print("Passed all tests!")
