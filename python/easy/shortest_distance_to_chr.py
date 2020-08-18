from typing import List


def shortest_to_char(S: str, C: str) -> List[int]:
    """
    # 821: Given a string S and a character C, return an array of integers representing the shortest 
    distance from the character C in the string.
    """
    ans = []

    prev = -float("inf")
    for i, ch in enumerate(S):
        if ch == C:
            prev = i
        ans.append(i - prev)

    prev = float("inf")
    for i in range(len(S) - 1, -1, -1):
        if S[i] == C:
            prev = i
        ans[i] = min(ans[i], prev - i)

    return ans


if __name__ == "__main__":
    S, C = "loveleetcode", "e"
    assert shortest_to_char(S, C) == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

    print("Passed all tests!")
