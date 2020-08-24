class MyQueue:
    """
    # 232: Implement the following operations of a queue using stacks.
        - push(x) -- Push element x to the back of queue.
        - pop() -- Removes the element from in front of queue.
        - peek() -- Get the front element.
        - empty() -- Return whether the queue is empty.
    """

    def __init__(self):
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)

    for i in range(1, 4):
        assert q.pop() == i

    print("Passed all tests!")
