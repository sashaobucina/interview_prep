class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
  if (l1 is None):
    return l2
  if (l2 is None):
    return l1

  if (l1.val > l2.val):
    head = l1
    l1 = l1.next
  else:
    head = l2
    l2 = l2.next

  current = head
  while (l1 is not None or l2 is not None):
    if (l1 is None):
      current.next = l2
      return head
    elif (l2 is None):
      current.next = l1
      return head

    if (l1.val < l2.val):
      current.next = l1.val
      current = current.next
      l1 = l1.next
    else:
      current.next = l2.val
      current = current.next
      l2 = l2.next
  current.next = None
  return head

if __name__ == "__main__":
  print()