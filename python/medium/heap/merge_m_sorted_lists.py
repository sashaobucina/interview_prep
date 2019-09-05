import heapq

class Node:
  def __init__(self, val, list_num, index):
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

if __name__ == "__main__":
  lists = [[1, 2, 3, 9], [4, 6, 8], [5]]
  print(merge_m_sorted_lists(lists))