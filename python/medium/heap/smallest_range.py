import heapq
import sys

MIN_INT = -sys.maxsize - 1
MAX_INT = sys.maxsize

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
Given M sorted lists of variable length, efficiently compute the smallest range that 
includes at least one element from each list

SOLUTION: When one list is exhausted, the last minimum needs to be included in the range,
and adding elements from other non-exhausted lists will only drive up the difference.
"""
def find_minimum_range(lists: list) -> tuple:
  heap = []
  high = MIN_INT
  p = (0, MAX_INT)

  for i, list in enumerate(lists):
    heapq.heappush(heap, Node(list[0], i, 0))
    high = max(high, lists[i][0])

  while True:
    top = heapq.heappop(heap)

    low = top.val
    list_num = top.list_num
    ind = top.index

    if high - low < p[1] - p[0]:
      p = (low, high)

    if ind == len(lists[list_num]) - 1:
      return p

    heapq.heappush(heap, Node(lists[list_num][ind + 1], list_num, ind + 1))
    high = max(high, lists[list_num][ind + 1])

if __name__ == "__main__":
  lists = [
    [3, 6, 8, 10, 15],
    [1, 5, 12],
    [4, 8, 16, 17],
    [2, 6]
  ]
  print(find_minimum_range(lists))    # expected: (4, 6)``