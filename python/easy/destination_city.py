from typing import List


def dest_city(paths: List[str]) -> str:
    """
    # 1436: You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct 
    path going from cityAi to cityBi. Return the destination city, that is, the city without any path 
    outgoing to another city.

    It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be 
    exactly one destination city.
    """
    seen = set()
    for path in paths:
        seen.add(path[0])

    for path in paths:
        if path[1] not in seen:
            return path[1]

    return ""


if __name__ == "__main__":
    paths = [["London", "New York"], [
        "New York", "Lima"], ["Lima", "Sao Paulo"]]
    assert dest_city(paths) == "Sao Paulo"

    print("Passed all tests!")
