def add_binary_simple(a: str, b: str) -> str:
    """
    This impelmenation uses builtin bin and int functions for easy conversions.
    """
    return bin(int(a, 2) + int(b, 2))[2:]


def add_binary(a: str, b: str) -> str:
    """
    # 67: Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.
    """
    mod, res = 0, []
    max_len = max(len(a), len(b))

    for i in range(1, max_len + 1):
        n1 = int(a[-i]) if i <= len(a) else 0
        n2 = int(b[-i]) if i <= len(b) else 0

        mod, bit = divmod(n1 + n2 + mod, 2)
        res.append(str(bit))

    if mod:
        res.append("1")

    return "".join(reversed(res))


if __name__ == "__main__":
    assert add_binary("1", "11") == add_binary_simple("1", "11") == "100"
    assert add_binary("1010", "1011") == add_binary_simple(
        "1010", "1011") == "10101"

    print("Passed all tests!")
