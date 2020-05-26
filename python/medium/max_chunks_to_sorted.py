from typing import List
import operator


def max_chunks_to_sorted(lst: List[int]) -> int:
    """
    # 769: Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split 
    # the array into some number of "chunks" (partitions), and individually sort each chunk. 
    # After concatenating them, the result equals the sorted array.

    What is the most number of chunks we could have made?
    """
    if len(lst) == 0:
        raise ValueError("List provided in must be non-empty!")

    chunks = max_in_chunk = 0

    for i in range(len(lst)):
        max_in_chunk = max(max_in_chunk, lst[i])
        if max_in_chunk == i:
            chunks += 1

    return chunks


if __name__ == "__main__":
    lst = [4, 3, 2, 1, 0]
    assert max_chunks_to_sorted(lst) == 1

    lst = [1, 0, 2, 3, 4]
    assert max_chunks_to_sorted(lst) == 4

    lst = [2, 0, 1]
    assert max_chunks_to_sorted(lst) == 1

    lst = [1, 0, 2]
    assert max_chunks_to_sorted(lst) == 2

    print("Passed all tests!")
