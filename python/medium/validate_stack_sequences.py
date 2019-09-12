"""
Given two sequences pushed and popped with distinct values, return true if and 
only if this could have been the result of a sequence of push and pop operations on 
an initially empty stack.

NOTE: Solution is O(n) time, O(n) space, and greedy
"""
def validate_stack_sequence(pushed: list, popped: list) -> bool:
  n = len(popped)
  i = 0
  stk = []
  for x in pushed:
    stk.append(x)
    while stk and i < n and stk[-1] == popped[i]:
      stk.pop()
      i += 1

  return i == n

if __name__ == "__main__":
  pushed = [1, 2, 3, 4, 5]
  popped = [4, 3, 5, 2, 1]
  print(validate_stack_sequence(pushed, popped))    # expected: True

  popped = [4, 3, 5, 1, 2]
  print(validate_stack_sequence(pushed, popped))    # expected: False