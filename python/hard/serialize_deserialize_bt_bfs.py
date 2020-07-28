from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        return (type(self) == type(other)) and (self.val == other.val) and (self.left == other.left) and \
            (self.right == other.right)


class Codec:
    """
    # 297: Serialization is the process of converting a data structure or object into a sequence of 
    bits so that it can be stored in a file or memory buffer, or transmitted across a network connection
    link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how 
    your serialization/deserialization algorithm should work. 

    You just need to ensure that a binary tree can be serialized to a string and this string can be 
    deserialized to the original tree structure.
    """

    def serialize(self, root: TreeNode) -> str:
        data = []

        if not root:
            return "[]"

        q = deque([root])
        while q:
            curr = q.pop()

            if not curr:
                data.append(None)
            else:
                data.append(curr.val)
                q.appendleft(curr.left)
                q.appendleft(curr.right)

        while data[-1] == None:
            data.pop()

        return str(data)

    def deserialize(self, data: str) -> TreeNode:
        data = data.strip("][")

        if data == "":
            return None

        vals = []
        for x in data.split(", "):
            try:
                vals.append(int(x))
            except ValueError:
                vals.append(None)

        left = right = False
        root = TreeNode(vals[0])
        q = deque([root])

        i = 1
        curr = root
        while i < len(vals):
            val = vals[i]
            node = TreeNode(val) if val is not None else None

            if left:
                curr.left = node
                if node:
                    q.appendleft(node)

                left = False
                i += 1
            elif right:
                curr.right = node

                if node:
                    q.appendleft(node)

                right = False
                i += 1
            else:
                curr = q.pop()
                left, right = True, True

        return root


if __name__ == "__main__":
    # construct original BT
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, left=n4, right=n5)
    n2 = TreeNode(2)
    n1 = TreeNode(1, left=n2, right=n3)

    # ensure after serialization & deserialization, tree is reconstructed in same way
    codec = Codec()
    assert codec.deserialize(codec.serialize(n1)) == n1
    assert codec.deserialize(codec.serialize(None)) is None

    print("Passed all tests!")
