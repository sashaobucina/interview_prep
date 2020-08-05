from collections import deque


def license_key_formatting(S: str, K: int) -> str:
    """
    # 482: You are given a license key represented as a string S which consists only alphanumeric character 
    and dashes. The string is separated into N+1 groups by N dashes.

    Given a number K, we would want to reformat the strings such that each group contains exactly K 
    characters, except for the first group which could be shorter than K, but still must contain at 
    least one character.

    Furthermore, there must be a dash inserted between two groups and all lowercase letters should be 
    converted to uppercase.

    Given a non-empty string S and a number K, format the string according to the rules described above.
    """
    S = S.replace("-", "").upper()
    N = len(S)

    i = N
    ans = deque([])
    while i > 0:
        if (i - K) <= 0:
            while i > 0:
                ans.appendleft(S[i - 1])
                i -= 1
        else:
            for j in range(K):
                ans.appendleft(S[i - j - 1])
            ans.appendleft("-")

            i -= K

    return "".join(ans)


if __name__ == "__main__":
    assert license_key_formatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"
    assert license_key_formatting("2-5g-3-J", 2) == "2-5G-3J"

    print("Passed all tests!")
