"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains 
the most water.

NOTE: You may not slant the container and n is at least 2.
"""
def maxArea(heights: list) -> int:
  maxArea, l, r = 0, 0, len(heights) - 1

  while l < r:
    maxArea = max(maxArea, min(heights[l], heights[r]) * (r - l))
    if heights[l] < heights[r]:
      l += 1
    else:
      r -= 1

  return maxArea

if __name__ == "__main__":
  heights = [1,8,6,2,5,4,8,3,7]
  print(maxArea(heights))