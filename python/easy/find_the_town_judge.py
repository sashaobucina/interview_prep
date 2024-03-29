from typing import List
from collections import defaultdict


def find_judge(N: int, trust: List[List[int]]) -> int:
    """
    # 997: In a town, there are N people labelled from 1 to N.  There is a rumor that one of these 
    people is secretly the town judge.

    If the town judge exists, then:
        - The town judge trusts nobody.
        - Everybody (except for the town judge) trusts the town judge.
        - There is exactly one person that satisfies properties 1 and 2.
        - You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled 
            a trusts the person labelled b.

    If the town judge exists and can be identified, return the label of the town judge. 
    Otherwise, return -1.

    Constraints:
        - 1 <= N <= 1000
        - 0 <= trust.length <= 10^4
        - trust[i].length == 2
        - trust[i] are all different
        - trust[i][0] != trust[i][1]
        - 1 <= trust[i][0], trust[i][1] <= N
    """
    if N == 1:
        return 1

    d = defaultdict(int)
    trusters = set()

    for a, b in trust:
        d[b] += 1
        trusters.add(a)

    count, judge = 0, -1
    for trustee in d:
        if (d[trustee] == N - 1) and (trustee not in trusters):
            count += 1
            judge = trustee

    return judge if count == 1 else -1


if __name__ == "__main__":
    N, trust = 2, [[1, 2]]
    assert find_judge(N, trust) == 2

    N, trust = 3, [[1, 3], [2, 3]]
    assert find_judge(N, trust) == 3

    N, trust = 3, [[1, 3], [2, 3], [3, 1]]
    assert find_judge(N, trust) == -1

    N, trust = 3, [[1, 2], [2, 3]]
    assert find_judge(N, trust) == -1

    print("Passed all tests!")
