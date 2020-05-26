class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self):
        def _str(node):
            if not node:
                return "None"
            return f"{node.val} -- {_str(node.next)}"

        return _str(self)


def flatten(head):
    """
    430: You are given a doubly linked list which in addition to the next and previous pointers, 
    it could have a child pointer, which may or may not point to a separate doubly 
    linked list. These child lists may have one or more children of their own, and so on, 
    to produce a multilevel data structure.

    Flatten the list so that all the nodes appear in a single-level, doubly linked list. 
    You are given the head of the first level of the list.
    """
    def _flatten(prev, curr):
        if not curr:
            return None

        last, next = curr, curr.next
        if curr.child:
            curr.next = _flatten(curr, curr.child)
            # go to the last node from children, now the new start node
            while last.next:
                last = last.next

        curr.prev = prev
        curr.child = None
        last.next = _flatten(last, next)
        return curr

    return _flatten(None, head)


if __name__ == "__main__":
    # create multilevel, doubly linked list
    # 1 -- 2 -- None
    # |
    # 3 -- None
    n1 = Node(1, None, None, None)
    n2 = Node(2, n1, None, None)
    n3 = Node(3, None, None, None)
    n1.next = n2
    n1.child = n3

    print(flatten(n1))  # Expected: 1 -- 3 -- 2 -- None
