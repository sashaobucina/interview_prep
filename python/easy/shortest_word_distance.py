from typing import List


def shortest_distance(words: List[str], word1: str, word2: str) -> int:
    """
    # 243: Given a list of words and two words word1 and word2, return the shortest distance between 
    these two words in the list.
    """
    dist = float("inf")

    w1, w2 = -1, -1
    for i, word in enumerate(words):
        if word1 != word and word2 != word:
            continue

        if word1 == word:
            w1 = i
        if word2 == word:
            w2 = i

        if w1 != -1 and w2 != -1:
            dist = min(dist, abs(w1 - w2))

    return dist


if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    assert shortest_distance(words, "practice", "coding") == 3
    assert shortest_distance(words, "makes", "coding") == 1

    print("Passed all tests!")
