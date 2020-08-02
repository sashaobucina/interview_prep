class HashSet:
    """
    # 705: Design a HashSet without using any built-in hash table libraries.

    To be specific, your design should include these functions:
        - add(value): Insert a value into the HashSet. 
        - contains(value) : Return whether the value exists in the HashSet or not.
        - remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

    NOTE: Hash sets use two important concepts: hashing and collision detection.
        - hashing is alleviated by a modulo hash function
        - collisions are handled in this case by seperate chaining in buckets
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_range = 769
        self.buckets = [Bucket() for _ in range(self.key_range)]

    def _hash(self, key) -> int:
        return key % self.key_range

    def add(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].insert(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = self._hash(key)
        return self.buckets[idx].exists(key)


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, val):
        if not self.exists(val):
            new_node = Node(val, self.head.next)
            self.head.next = new_node

    def delete(self, val):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.val == val:
                prev.next = curr.next

            prev = curr
            curr = curr.next

    def exists(self, val):
        curr = self.head.next
        while curr:
            if curr.val == val:
                return True

            curr = curr.next

        return False


if __name__ == "__main__":
    hash_set = HashSet()
    hash_set.add(1)
    hash_set.add(2)
    assert hash_set.contains(1)
    assert not hash_set.contains(3)
    hash_set.add(2)
    assert hash_set.contains(2)
    hash_set.remove(2)
    assert not hash_set.contains(2)

    print("Passed all tests!")
