"""
Implement the following operations of a stack using queues.

  - push(x) -- Push element x onto stack.
  - pop() -- Removes the element on top of the stack.
  - top() -- Get the top element.
  - empty() -- Return whether the stack is empty.
"""
class MyStack:

  def __init__(self):
    self.q = []

  def push(self, x: int) -> None:
    self.q.append(x)
    size = len(self.q)
    while size > 1:
      self.q.append(self.q.pop(0))
      size -= 1


  def pop(self) -> int:
    return self.q.pop(0)


  def top(self) -> int:
    if not self.isEmpty():
      return self.q[0]
    raise IndexError("Stack is empty!")


  def isEmpty(self) -> bool:
    return len(self.q) == 0

if __name__ == "__main__":
  stk = MyStack()
  stk.push(3)
  print(stk.top())
  print(stk.pop())
  print(stk.isEmpty())
