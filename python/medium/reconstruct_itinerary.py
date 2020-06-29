from typing import List
from collections import defaultdict


def find_itinerary(tickets: List[List[int]]) -> List[int]:
    """
    # 332: Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
    reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
    Thus, the itinerary must begin with JFK.

    NOTE:
        - If there are multiple valid itineraries, you should return the itinerary that has the smallest 
            lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller 
            lexical order than ["JFK", "LGB"].
        - All airports are represented by three capital letters (IATA code).
        - You may assume all tickets form at least one valid itinerary.
        - One must use all the tickets once and only once.
    """
    itinerary = []
    N = len(tickets)

    # build graph for traversal
    conns = defaultdict(dict)
    for src, dst in tickets:
        if not dst in conns[src]:
            conns[src][dst] = 1
        else:
            conns[src][dst] += 1

    def _dfs(src, num_visited, res):
        if num_visited == N:
            itinerary.append(res)
            return True

        dsts = sorted(list(conns[src].keys()))
        for dst in dsts:
            if conns[src][dst] > 0:
                conns[src][dst] -= 1
                if _dfs(dst, num_visited + 1, res + [dst]):
                    return True
                conns[src][dst] += 1

        return False

    _dfs("JFK", 0, ["JFK"])
    return itinerary[0]


if __name__ == "__main__":
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    assert find_itinerary(tickets) == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
        "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    assert find_itinerary(tickets) == [
        "JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]

    print("Passed all tests!")
