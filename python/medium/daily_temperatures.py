def daily_temperatures(temperatures: list) -> list:
  """
  Given a list of daily temperatures T, return a list such that, for each day in the input, 
  tells you how many days you would have to wait until a warmer temperature. 
  If there is no future day for which this is possible, put 0 instead.

  For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
  your output should be [1, 1, 4, 2, 1, 1, 0, 0].

  Note: The length of temperatures will be in the range [1, 30000]. 
  Each temperature will be an integer in the range [30, 100].
  """
  ans = [0] * len(temperatures)
  stk = []

  for i in range(len(temperatures) - 1, -1, -1):
    while stk and temperatures[i] >= temperatures[stk[-1]]:
      stk.pop()
    if stk:
      ans[i] = stk[-1] - i
    stk.append(i)

  return ans

def checkEqual(L1, L2):
  return len(L1) == len(L2) and sorted(L1) == sorted(L2)

if __name__ == "__main__":
  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
  output = daily_temperatures(temperatures)
  print(output)
  expected = [1, 1, 4, 2, 1, 1, 0, 0]
  if not checkEqual(output, expected):
    print("Expected output to be {0}, but got {1}".format(expected, output))