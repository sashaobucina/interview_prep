import heapq

class Node:
  def __init__(self, val, list_num, index=0):
    self.val = val
    self.list_num = list_num
    self.index = index

  def _is_valid_operand(self, other):
    return (hasattr(other, "val") and hasattr(other, "list_num") and hasattr(other, "index"))

  def __eq__(self, other):
    if not self._is_valid_operand(other):
      return NotImplemented
    return (self.val == other.val)

  def __lt__(self, other):
    if not self._is_valid_operand(other):
      return NotImplemented
    return (self.val < other.val)

  def __str__(self) -> str:
    return "{0} ".format(self.val)

"""
Given M sorted lists of variable length, return them in sorted order
"""
def merge_m_sorted_lists(lists: list) -> list:
  res = []
  heap = []
  for i, list in enumerate(lists):
    if len(list) > 0:
      heapq.heappush(heap, Node(list[0], i, 0))

  while len(heap) > 0:
    minNode = heapq.heappop(heap)
    res.append(minNode.val)

    if minNode.index + 1 < len(lists[minNode.list_num]):
      minNode.index = minNode.index + 1
      minNode.val = lists[minNode.list_num][minNode.index]
      heapq.heappush(heap, minNode)

  return res

class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    res = []
    curr = self
    while curr:
      res.append("{0} -> ".format(curr.val))
      curr = curr.next
    return "".join(res)

  def add_next(self, next):
    self.next = next

def merge_m_sorted_linked_lists(lists: list):
  heap = []
  refs = [ll for ll in lists]

  for i in range(len(lists)):
    heapq.heappush(heap, Node(lists[i].val, i))

  curr, head = None, None
  while len(heap) > 0:
    top = heapq.heappop(heap)

    if not head:
      head = ListNode(top.val)
      curr = head
    else:
      curr.next = ListNode(top.val)
      curr = curr.next

    if refs[top.list_num].next:
      refs[top.list_num] = refs[top.list_num].next
      top.val = refs[top.list_num].val
      heapq.heappush(heap, top)

  return head

if __name__ == "__main__":
  lists = [[1, 2, 3, 9], [4, 6, 8], [5]]
  print(merge_m_sorted_lists(lists))

  a3 = ListNode(5)
  a2 = ListNode(2, a3)
  a1 = ListNode(1, a2)

  b2 = ListNode(7)
  b1 = ListNode(4, b2)

  c4 = ListNode(19)
  c3 = ListNode(8, c4)
  c2 = ListNode(6, c3)
  c1 = ListNode(0, c2)

  lists = [a1, b1, c1]
  print(merge_m_sorted_linked_lists(lists))