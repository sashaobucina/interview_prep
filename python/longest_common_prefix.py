import sys


def longest_common_prefix(strs: list) -> str:
    """
    # 14: Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    """
    if not strs or not all(strs):
        return ""

    n = len(min(strs))
    for i in range(n):
        ch = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != ch:
                return strs[0][:i]

    return strs[0][:i+1]


def smallest_len(strs: list) -> int:
    min_len = sys.maxsize
    for i in range(len(strs)):
        if (len(strs[i]) < min_len):
            min_len = len(strs[i])
    return min_len


def is_common_prefix(strs: list, n: int) -> bool:
    str1 = strs[0][0:n]
    for i in range(len(strs)):
        if (not strs[i].startswith(str1)):
            return False
    return True


def lcp_binary_search(strs: list) -> str:
    prefix = ""
    low = 0
    high = smallest_len(strs)
    while (low <= high):
        mid = (low + high) // 2
        if (is_common_prefix(strs, mid)):
            low = mid + 1
        else:
            high = mid - 1
    final_mid = (low + high) // 2
    return strs[0][0:final_mid]


if __name__ == "__main__":
    strs = ["leer", "leet", "lee", "lee", "let"]
    assert longest_common_prefix(strs) == lcp_binary_search(strs) == "le"

    print("Passed all tests!")
