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
      bounded_height = min(height[curr] - height[top], height[stk[-1]] - height[top])
      ans += distance * bounded_height

    stk.append(curr)
    curr += 1

  return ans

def trap_dp(height: list) -> int:
  ans, n = 0, len(height)
  left_max, right_max = [-1 for i in range(n)], [-1 for i in range(n)]
  if not height:
    return ans

  left_max[0] = height[0]
  for i in range(1, n):
    left_max[i] = max(height[i], left_max[i-1])

  right_max[n-1] = height[n-1]
  for i in range(n - 2, -1, -1):
    right_max[i] = max(height[i], right_max[i+1])

  for i in range(1, n - 1):
    ans += min(left_max[i] - height[i], right_max[i] - height[i])
  return ans

if __name__ == "__main__":
  height = [4,2,3]
  print(trap(height))   # expected: 1

  height2 = [0,1,0,2,1,0,1,3,2,1,2,1]
  print(trap_dp(height2))   # expected: 6