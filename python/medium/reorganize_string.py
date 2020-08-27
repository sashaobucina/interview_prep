from typing import List
from collections import Counter
from heapq import heappop, heappush


def reorganize_string(S: str) -> str:
    """
    # 767: Given a string S, check if the letters can be rearranged so that two characters that are adjacent 
    to each other are not the same.

    If possible, output any possible result.  If not possible, return the empty string.
    """
    res = []
    N = len(S)

    pq = []
    for ch, count in Counter(S).items():
        if count > (N + 1) // 2:
            return ""
        heappush(pq, (-count, ch))

    while len(pq) >= 2:
        count1, ch1 = heappop(pq)
        count2, ch2 = heappop(pq)
        res += [ch1, ch2]

        if count1 < -1:
            heappush(pq, (count1 + 1, ch1))
        if count2 < -1:
            heappush(pq, (count2 + 1, ch2))

    if pq:
        res.append(pq.pop()[1])

    return "".join(res)


if __name__ == "__main__":
    S = "aab"
    assert reorganize_string(S) == "aba"

    S = "aaab"
    assert reorganize_string(S) == ""

    print("Passed all tests!")
