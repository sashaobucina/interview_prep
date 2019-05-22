class LinkedListNode:
  def __init__(self, data: int):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def get(self, index: int) -> int:
    count = 0
    curr = self.head
    while (curr):
      if count == index:
        return curr.val
      curr = curr.next
    return -1

  def addAtHead(self, x: int) -> None:
    if self.head is None:
      self.head = LinkedListNode(x)
    else:
      temp = self.head
      self.head = LinkedListNode(x)
      self.head.next = temp
    self.size += 1

  def addAtTail(self, x: int) -> None:
    if (self.head is None):
      self.head = LinkedListNode(x)
    else:
      curr = self.head
      while (curr.next):
        curr = curr.next
      curr.next = LinkedListNode(x)
    self.size += 1

  def addAtIndex(self, x: int, index: int) -> None:
    if (index == 0):
      self.addAtHead(x)
    elif (index == self.size):
      self.addAtTail(x)
    elif (0 < index < self.size):
      count = 0
      prev = None
      curr = self.head
      while curr:
        if count == index:
          node = LinkedListNode(x)
          prev.next = node
          node.next = curr
          self.size += 1
          return
        prev = curr
        curr = curr.next
        count += 1
    else:
      raise IndexError("Index out of bounds")

  def deleteAtIndex(self, index: int) -> None:
    if (0 <= index < self.size):
      count = 0
      curr = self.head
      prev = None
      while curr:
        if count == index:
          if prev:
            prev.next = curr.next
          else:
            self.head = curr.next
          self.size -= 1
          return
        prev = curr
        curr = curr.next
        count += 1
    else:
      raise IndexError("Index out of bounds")

  def __str__(self) -> str:
    if self.head is None:
      return ""
    res = ""
    curr = self.head
    while curr.next:
      res += "{} -> ".format(curr.data)
      curr = curr.next
    res += "{}".format(curr.data)
    return res

if __name__ == "__main__":
  ll = LinkedList()
  ll.addAtTail(1)
  ll.addAtTail(2)
  ll.addAtTail(3)
  ll.addAtTail(4)
  ll.addAtIndex(5, 4)
  ll.deleteAtIndex(0)
  print(ll)