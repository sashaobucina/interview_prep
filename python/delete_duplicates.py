class ListNode:
  def __init__(self, x: int):
    self.val = x
    self.next = None

def delete_duplicates(head: ListNode):
  current = head
  previous = None
  while (current != None):
    if (previous is not None and previous.val == current.val):
      previous.next = current.next
    else:
      previous = current
    current = current.next
  return head

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.
"""
def delete_duplicates_distinct(head: ListNode):
  curr = head
  prev = None
  while (curr is not None):
    # duplicate case
    if curr.next is not None and curr.val == curr.next.val:
      curr = curr.next
      while (curr.next is not None and curr.val == curr.next.val):
        curr = curr.next
      curr = curr.next
      if prev is None:
        head = curr
      else:
        prev.next = curr
    # normal case, just iterate over
    else:
        prev = curr
        curr = curr.next
  return head
