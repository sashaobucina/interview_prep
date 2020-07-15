from typing import Any, List
from itertools import combinations
from collections import defaultdict


def most_visited_pattern(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    """
    # 1152: We are given some website visits: the user with name username[i] visited the website website[i] 
    at time timestamp[i].

    A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits. 
    (The websites in a 3-sequence are not necessarily distinct.)

    Find the 3-sequence visited by the largest number of users. If there is more than one solution,
    return the lexicographically smallest such 3-sequence.
    """
    # get user data and sort based of timestamps
    data = list(zip(username, timestamp, website))
    data.sort(key=lambda x: x[1])

    # extract all websites visited by users
    visited = defaultdict(list)
    for user, _, site in data:
        visited[user].append(site)

    # get all combinations of length 3 for each user, and keep track of frequencies for 3-sequences
    freq = defaultdict(int)
    for user, sites in visited.items():
        combos = set(combinations(sites, 3))
        # OR
        combos = _combinations(sites, 3)
        combos = set([tuple(combo) for combo in combos])

        three_seqs = set()
        for combo in combos:
            three_seqs.add(",".join(combo))

        for three_seq in three_seqs:
            freq[three_seq] += 1

    # extract most frequent 3-sequence
    _max = max(freq.values())
    results = [k for k, v in freq.items() if v == _max]

    # get lexicographically smallest answer, if more than one 3-sequence is most frequent
    if len(results) == 0:
        return results[0].split(",")

    return sorted(results)[0].split(",")


def _combinations(l: List[Any], n: int) -> List[List[Any]]:
    """
    Equivalent to itertools.combinations function.
    """
    if n == 0:
        return [[]]

    res = []
    for i in range(len(l)):
        el, rem_l = l[i], l[i+1:]

        for combo in _combinations(rem_l, n-1):
            res.append([el] + combo)

    return res


if __name__ == "__main__":
    username = ["joe", "joe", "joe", "james", "james",
                "james", "james", "mary", "mary", "mary"]
    website = ["home", "about", "career", "home", "cart",
               "maps", "home", "home", "about", "career"]
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert most_visited_pattern(username, timestamp, website) == [
        "home", "about", "career"]

    print("Passed all tests!")
