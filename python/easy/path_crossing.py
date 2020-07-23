def is_path_crossing(path: str) -> bool:
    """
    # 1496: Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one 
    unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane 
    and walk on the path specified by path.

    Return True if the path crosses itself at any point, that is, if at any time you are on a location 
    you've previously visited. Return False otherwise.
    """
    loc = (0, 0)
    visited = {loc}

    for direction in path:
        if direction == "N":
            loc = (loc[0], loc[1] + 1)
        elif direction == "W":
            loc = (loc[0] - 1, loc[1])
        elif direction == "S":
            loc = (loc[0], loc[1] - 1)
        else:
            loc = (loc[0] + 1, loc[1])

        if loc in visited:
            return True

        visited.add(loc)

    return False


if __name__ == "__main__":
    assert not is_path_crossing("NES")
    assert is_path_crossing("NESWW")

    print("Passed all tests!")
