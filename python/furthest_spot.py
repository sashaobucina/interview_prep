import math

"""
Imagine a bus with a single row, represented by an array. A full spot is singified by "1" and
and an empty seat is signified by a "0". Find the spot that is furthest away from any passengers.
"""
def furthest_spot(arr: list) -> int:
  curr_start = None
  opt_start, opt_end = -1, -1
  i = 0
  while i < len(arr):
    if arr[i] == 0:
      curr_start = i
      j = i + 1
      while (j < len(arr) and arr[j] == 0):
        j += 1
      curr_end = j - 1
      curr_diff = curr_end - curr_start
      if opt_start == -1 or curr_diff > opt_end - opt_start:
        opt_start, opt_end = curr_start, curr_end
    i += 1
  return  -1 if curr_start is None else math.ceil(opt_start + ((opt_end - opt_start) / 2))

if __name__ == "__main__":
  l = [1, 1, 1, 0, 0, 0]
  print(furthest_spot(l))