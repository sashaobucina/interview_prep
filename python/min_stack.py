class MinStackNode:
    def __init__(self, val: int, min: int):
        self.val = val
        self.min = min

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        return isinstance(other, MinStackNode) and self.val == other.val and \
            self.min == other.min


class MinStack:
    """
    # 155: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Methods:
    - push(x) -- Push element x onto stack.
    - pop() -- Removes the element on top of the stack.
    - top() -- Get the top element.
    - getMin() -- Retrieve the minimum element in the stack
    """

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if (self.min is None or x < self.min):
            self.min = x
        self.stack.append(MinStackNode(x, self.min))

    def pop(self) -> None:
        if (len(self.stack) > 0):
            node = self.stack.pop()
            if (node.val is self.min):
                self.min = self.stack[-1].min if self.stack else None

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min


if __name__ == "__main__":
    stk = MinStack()
    stk.push(2)
    stk.push(0)
    stk.push(3)
    stk.push(0)
    assert stk.getMin() == 0
    stk.pop()
    assert stk.getMin() == 0
    assert stk.top() == MinStackNode(3, 0)
    assert stk.getMin() == 0
    stk.pop()
    assert stk.getMin() == 0

    print("Passed all tests!")
