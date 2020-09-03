from typing import List


def strobogrammatic_in_range(low: int, high: int) -> int:
    """
    # 248: A strobogrammatic number is a number that looks the same when rotated 180 degrees 
    (looked at upside down).

    Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.
    """
    def find_num_digits(num: int) -> int:
        cnt = 0
        if num == 0:
            return 1
        while num > 0:
            num //= 10
            cnt += 1
        return cnt
    # find num digits in low & high
    num1 = find_num_digits(int(low))
    num2 = find_num_digits(int(high))

    ans = 0
    for n in range(num1, num2 + 1):
        for num in find_strobogrammatic(n):
            if int(low) <= int(num) <= int(high):
                ans += 1

    return ans


def find_strobogrammatic(n: int) -> List[str]:
    if n == 0:
        return []
    if n == 1:
        return ["0", "1", "8"]

    pairs = [("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")]

    def helper(n):
        if n == 0:
            return [[]]
        elif n == 1:
            return [["0"], ["1"], ["8"]]
        else:
            ans = []
            for mid in helper(n - 2):
                for pair in [("0", "0")] + pairs:
                    ans.append([pair[0]] + mid + [pair[1]])

            return ans

    ans = []
    for mid in helper(n - 2):
        for pair in pairs:
            ans.append("".join([pair[0]] + mid + [pair[1]]))

    return ans


if __name__ == "__main__":
    assert strobogrammatic_in_range("0", "0") == 1
    assert strobogrammatic_in_range("50", "100") == 3
    assert strobogrammatic_in_range("50", "1000") == 15
    assert strobogrammatic_in_range("88", "88") == 1

    print("Passed all tests!")
