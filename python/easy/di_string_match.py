from typing import List


def di_string_match(S: str) -> List[int]:
    """
    # 942: Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

    Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
        - If S[i] == "I", then A[i] < A[i+1]
        - If S[i] == "D", then A[i] > A[i+1]
    """
    res = []
    N = len(S)

    lo, hi = 0, N
    for i in range(N):
        if S[i] == "I":
            res.append(lo)
            lo += 1
        else:
            res.append(hi)
            hi -= 1

    res.append(lo)
    return res


if __name__ == "__main__":
    assert di_string_match("IDID") == [0, 4, 1, 3, 2]
    assert di_string_match("III") == [0, 1, 2, 3]
    assert di_string_match("DDI") == [3, 2, 0, 1]

    print("Passed all tests!")
