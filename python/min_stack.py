import sys

class MinStackNode:
  def __init__(self, val: int, min: int):
    self.val = val
    self.min = min

class MinStack:

  def __init__(self):
    self.stackList = []
    self.minElement = None

  def push(self, x: int) -> None:
    if (self.minElement is None or x < self.minElement):
      self.minElement = x
    self.stackList.append(MinStackNode(x, self.minElement))

  def pop(self) -> None:
    if (len(self.stackList) > 0):
      node = self.stackList.pop()
      if (node.val is self.minElement):
        if (len(self.stackList) != 0):
          self.minElement = self.stackList[len(self.stackList)-1].min
        else:
          self.minElement = None

  def top(self) -> int:
    size = len(self.stackList)
    return self.stackList[size-1] if size > 0 else None

  def getMin(self) -> int:
    return self.minElement

if __name__ == "__main__":
  stk = MinStack()
  stk.push(2)
  stk.push(0)
  stk.push(3)
  stk.push(0)
  print(stk.getMin())
  stk.pop()
  print(stk.getMin())
  stk.top()
  print(stk.getMin())
  stk.pop()
  print(stk.getMin())