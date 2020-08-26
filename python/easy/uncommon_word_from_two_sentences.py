from typing import List
from collections import Counter


def uncommon_from_sentences(A: str, B: str) -> List[str]:
    """
    # 884: We are given two sentences A and B.  (A sentence is a string of space separated words.
    Each word consists only of lowercase letters.)

    A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

    Return a list of all uncommon words. 

    You may return the list in any order.
    """
    ans = []
    count_a = Counter(A.split())
    count_b = Counter(B.split())

    for word, count in count_a.items():
        if count == 1 and word not in count_b:
            ans.append(word)
    for word, count in count_b.items():
        if count == 1 and word not in count_a:
            ans.append(word)

    return ans


if __name__ == "__main__":
    A, B = "this apple is sweet", "this apple is sour"
    assert uncommon_from_sentences(A, B) == ["sweet", "sour"]

    A, B = "apple apple", "banana"
    assert uncommon_from_sentences(A, B) == ["banana"]

    print("Passed all tests!")
