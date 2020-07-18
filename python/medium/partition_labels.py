from typing import List


def partition_labels(S: str) -> List[int]:
    """
    # 763: A string S of lowercase English letters is given. 

    We want to partition this string into as many parts as possible so that each letter appears in at
    most one part, and return a list of integers representing the size of these parts.
    """
    res = []

    start = end = 0
    last_ch = {ch: i for i, ch in enumerate(S)}

    for i in range(len(S)):
        end = max(end, last_ch[S[i]])
        if i == end:
            res.append((end - start) + 1)
            start = i + 1

    return res


if __name__ == "__main__":
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]

    print("Passed all tests!")