from collections import deque


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

    def __str__(self):
        return f"{self.val}"


def clone_graph(node):
    """
    # 133: Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

    NOTE: Iterative solution
    """
    if not node:
        return None

    q = deque([node])
    d = {node: Node(node.val)}

    while q:
        curr = q.pop()
        for neighbor in curr.neighbors:
            if neighbor in d:
                d[curr].neighbors.append(d[neighbor])
            else:
                d[neighbor] = Node(neighbor.val)
                d[curr].neighbors.append(d[neighbor])
                q.appendleft(neighbor)

    return d[node]


def clone_graph_rec(node: Node) -> Node:
    """ NOTE: Recursive solution """
    d = {}

    def _clone(node: Node) -> Node:
        if not node:
            return None

        if node not in d:
            d[node] = Node(node)
            d[node].neighbors = [_clone(neighbor) for neighbor in node.neighbors]

        return d[node]

    return _clone(node)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors = [n2]
    n2.neighbors = [n1]

    cloned_n1 = clone_graph(n1)
    assert cloned_n1 is not n1
    assert cloned_n1.val == n1.val

    print("Passed all tests!")
