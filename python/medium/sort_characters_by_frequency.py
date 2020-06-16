import heapq


def frequency_sort(s: str) -> str:
    """
    #451 : Given a string, sort it in decreasing order based on the frequency of characters.
    """
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = [-1, ch]
        else:
            d[ch][0] -= 1

    res = []
    heap = list(d.values())
    heapq.heapify(heap)
    while heap:
        cnt, ch = heapq.heappop(heap)
        res += [ch] * (-cnt)

    return "".join(res)


if __name__ == "__main__":
    s = "tree"
    assert frequency_sort(s) == "eert"

    s = "cccaaa"
    assert frequency_sort(s) == "aaaccc"

    s = "Aabb"
    assert frequency_sort(s) == "bbAa"

    print("Passed all tests!")