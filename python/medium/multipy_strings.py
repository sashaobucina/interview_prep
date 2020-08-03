def multipy_strings(num1: str, num2: str) -> str:
    """
    # 43: Given two non-negative integers num1 and num2 represented as strings, return the product of 
    num1 and num2, also represented as a string.
    """
    if num1 == "0" or num2 == "0":
        return "0"
    if num1 == "1":
        return num2
    if num2 == "1":
        return num1

    nums, zeros = [], 0
    for i in range(len(num2) - 1, -1, -1):
        carry = 0
        num = ["0"] * zeros

        for j in range(len(num1) - 1, -1, -1):
            prod = (int(num2[i]) * int(num1[j])) + carry

            num.append(str(prod % 10))
            carry = prod // 10

        if carry:
            num.append(str(carry))

        nums.append("".join(num[::-1]))
        zeros += 1

    if len(nums) > 1:
        while len(nums) > 1:
            n1, n2 = nums.pop(), nums.pop()
            nums.append(add(n1, n2))

    return nums[0]


def add(num1: str, num2: str) -> str:
    _sum = []
    carry = 0

    i, j = len(num1) - 1, len(num2) - 1
    while i >= 0 or j >= 0:
        a = ord(num1[i]) - ord("0") if i >= 0 else 0
        b = ord(num2[j]) - ord("0") if j >= 0 else 0

        _sum.append(str((a + b + carry) % 10))
        carry = (a + b + carry) // 10

        i -= 1
        j -= 1

    if carry:
        _sum.append("1")

    return "".join(_sum[::-1])


if __name__ == "__main__":
    assert multipy_strings("2", "3") == "6"
    assert multipy_strings("123", "456") == "56088"

    print("Passed all tests!")
