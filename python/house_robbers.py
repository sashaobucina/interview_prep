def rob(arr: list) -> int:
  n = len(arr)
  if n == 0:
    return 0
  if n == 1:
    return arr[0]

  dp = [0] * n
  dp[0] = arr[0]
  dp[1] = max(arr[0], arr[1])
  for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])
  return dp[n-1]

def rob2(arr: list) -> int:
  even = odd = 0
  for i in range(len(arr)):
    if i % 2 == 0:
      even += arr[i]
      even = even if even > odd else odd
    else:
      odd += arr[i]
      odd = odd if odd > even else even

  return max(even, odd)

if __name__ == "__main__":
  arr = [122, 23, 45, 122]
  print(rob(arr))