"""
Given a collection of intervals, merge all overlapping intervals.
"""
def mergeIntervals(intervals: list) -> list:
  intervals.sort(key=lambda interval: interval[0])
  merged = []

  for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
      merged.append(interval)
    else:
      merged[-1][1] = max(merged[-1][1], interval[1])

  return merged

if __name__ == "__main__":
  intervals = [[1,3],[2,6],[8,10],[15,18],[2,9]]
  print(mergeIntervals(intervals))