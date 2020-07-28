from itertools import permutations


def num_tile_possibilities(tiles: str) -> int:
    """
    # 1079: You have a set of tiles, where each tile has one letter tiles[i] printed on it. 

    Return the number of possible non-empty sequences of letters you can make.
    """
    poss = set()

    def dfs(s: str, l: str):
        poss.add(s)

        for i in range(len(l)):
            dfs(s + l[i], l[:i] + l[i+1:])

    for i in range(len(tiles)):
        dfs(tiles[i], tiles[:i] + tiles[i+1:])

    return len(poss)


if __name__ == "__main__":
    tiles = "ABB"
    assert num_tile_possibilities(tiles) == 8

    tiles = "AAABBC"
    assert num_tile_possibilities(tiles) == 188

    print("Passed all tests!")
