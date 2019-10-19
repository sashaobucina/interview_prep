"""
Find all the connections that if disconnected, would lead to a disjoint graph / topology
"""
def criticalConnection(numOfServers, numOfConnections, connections):
    adj_list = buildAdjList(connections, numOfServers)

    res = []
    for i, connection in enumerate(connections):
        if check_disconnected(adj_list, connection, numOfServers):
          res.append(connection)
    return res


def check_disconnected(adj_list, connection, numOfServers):
    # remove connection
    serv1, serv2 = connection
    adj_list[serv1].remove(serv2)
    adj_list[serv2].remove(serv1)
    
    # test if graph connected
    res = is_connected(adj_list, numOfServers)
    
    # add connection back
    adj_list[serv1].append(serv2)
    adj_list[serv2].append(serv1)

    # return connectivity status
    return not res
    
    
def is_connected(adj_list, numOfServers):
    visited = [False] * (numOfServers + 1)
    
    dfs(adj_list, visited, 1)
    
    for i in range(1, numOfServers + 1):
        if not visited[i]:
            return False
    return True
    
    
def dfs(adj_list, visited, node):
    visited[node] = True
    
    for i in range(len(adj_list[node])):
        if not visited[adj_list[node][i]]:
            dfs(adj_list, visited, adj_list[node][i])
    
def buildAdjList(connections, numOfServers):
    adj_list = [[] for i in range(0, numOfServers + 1)]
    for connection in connections:
        serv1, serv2 = connection
        adj_list[serv1].append(serv2)
        adj_list[serv2].append(serv1)
    return adj_list
    

if __name__ == "__main__":
  connections = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [2, 8], [2, 6], [1, 9]]
  numServers = 9
  numConn = 10
  print(criticalConnection(numServers, numConn, connections))     # expected: [[1, 2], [1, 9]]

