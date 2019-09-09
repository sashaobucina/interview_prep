"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute 
how much water it is able to trap after raining.
"""
def trap(height: list) -> int:
  stk = []
  ans, curr = 0, 0
  while curr < len(height):
    while len(stk) > 0 and height[curr] > height[stk[-1]]:
      top = stk.pop()
      if len(stk) == 0:
        break
      distance = curr - stk[-1] - 1
      print(stk, height[stk[-1]], height[top])
      bounded_height = min(height[curr] - height[top], height[stk[-1]] - height[top])
      ans += distance * bounded_height

    stk.append(curr)
    curr += 1

  return ans

if __name__ == "__main__":
  height = [4,2,3]
  print(trap(height))   # expected: 1