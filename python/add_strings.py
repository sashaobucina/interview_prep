def add_strings(num1: str, num2: str) -> str:
    """
    # 415: Given two non-negative integers num1 and num2 represented as string, return the sum of 
    num1 and num2.

    NOTE: You must not use any built-in BigInteger library or convert the inputs to integer directly.
    """
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    _sum = []

    while i >= 0 or j >= 0:
        a = ord(num1[i]) - ord("0") if i >= 0 else 0
        b = ord(num2[j]) - ord("0") if j >= 0 else 0

        _sum.append(str((a + b + carry) % 10))
        carry = (a + b + carry) // 10

        i -= 1
        j -= 1

    if carry:
        _sum.append("1")

    return "".join(reversed(_sum))


if __name__ == "__main__":
    assert add_strings("98", "9") == "107"
    assert add_strings("98", "0") == "98"

    print("Passed all tests!")
