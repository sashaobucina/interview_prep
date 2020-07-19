class DLinkedNode:
    def __init__(self, val=0, key=0):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:
    """
    # 146: Design and implement a data structure for Least Recently Used (LRU) cache. 

    It should support the following operations: get and put.

        - get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
            otherwise return -1.
        - put(key, value) - Set or insert the value if the key is not already present. When the cache reached 
            its capacity, it should invalidate the least recently used item before inserting a new item.

    The cache is initialized with a positive capacity.

    Follow up:
        - Could you do both operations in O(1) time complexity?
    """

    def __init__(self, capacity):
        self.cache = {}

        self.size = 0
        self.capacity = capacity

        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: DLinkedNode) -> None:
        """ Always add node right after head. """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkedNode) -> None:
        """ Remove existing node from doubly linked list. """
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def _move_to_head(self, node: DLinkedNode) -> None:
        """ Move node from linked list to the head. """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DLinkedNode:
        """ Pop the current tail node. """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move accessed node to head
        self._move_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)

        if not node:
            new_node = DLinkedNode(val=value, key=key)
            self.cache[key] = new_node
            self._add_node(new_node)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = value
            self._move_to_head(node)


if __name__ == "__main__":
    lru = LRUCache(capacity=2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4

    print("Passed all tests!")
