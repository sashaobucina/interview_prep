import random

pick = random.randint(1, 100)

"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
"""
def guessNumber(n: int) -> int:
  l, r = 0 , n
  while l <= r:
    mid = (l + r) // 2
    guessed = guess(mid)
    if guessed == 0:
      return mid
    else:
      if guessed > 0:
        l = mid + 1
      else:
        r = mid - 1

  return -1

def guess(n: int) -> int:
  if pick == n:
    return 0
  elif pick > n:
    return 1
  else:
    return -1

if __name__ == "__main__":
  res = guessNumber(100)
  print("Guessed the number {0} and the pick was {1}".format(res, pick))