import sys
"""
Given a list of tuples representing points, find two points that would create a bisection between the points.

Precondition: The number of points is even.
"""
def pointBisection(points: list) -> list:
  leftMost =  [sys.maxsize, 0]
  for i in range(len(points)):
    if points[i][0] < leftMost[0]:
      leftMost = points[i]

  slopes = []
  for i in range(len(points)):
    if leftMost != points[i]:
      slopes.append((getSlope(leftMost, points[i]), points[i]))
  sorted(slopes, key= lambda x: x[0])

  return [leftMost, slopes[len(slopes) // 2][1]]

def getSlope(a: tuple, b: tuple) -> int:
  return (a[1] - b[1]) / (a[0] - b[0])

if __name__ == "__main__":
  arr = [(1, 1), (4, 0), (2, 2), (3, 5)]
  print(pointBisection(arr))