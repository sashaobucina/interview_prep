import heapq
from typing import List
from collections import Counter


def top_k_frequent(words: List[str], k: int) -> List[str]:
    """
    # 692: Given a non-empty list of words, return the k most frequent elements.

    Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency,
    then the word with the lower alphabetical order comes first.
    """
    count = Counter(words)

    # Using sorting
    candidates = list(count.keys())
    candidates.sort(key=lambda w: (-count[w], w))

    # Using heap
    hq = [(-freq, w) for w, freq in count.items()]
    heapq.heapify(hq)
    return [heapq.heappop(hq)[1] for _ in range(k)]


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    assert top_k_frequent(words, 2) == ["i", "love"]

    words = [
        "the", "day", "is", "sunny", "the",
        "the", "the", "sunny", "is", "is"
    ]
    assert top_k_frequent(words, 4) == ["the", "is", "sunny", "day"]

    print("Passed all tests!")
