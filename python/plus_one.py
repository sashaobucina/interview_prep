def plus_one_hack(digits: list) -> list:
  num = int("".join(map(str, digits))) + 1
  return [int(digit) for digit in str(num)]

def plus_one(digits: list) -> list:
  idx = len(digits) - 1
  while idx >= 0:
    if digits[idx] + 1 > 9:
      digits[idx] = 0
    else:
      digits[idx] += 1
      return digits
    idx -= 1
  digits.insert(0, 1)
  return digits


if __name__ == "__main__":
  digits = [3, 9, 9]
  print(plus_one(digits))