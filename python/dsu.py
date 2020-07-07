from typing import List


class DSU:
    def __init__(self, data: List[int]):
        self.p = data

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> None:
        self.p[self.find(x)] = self.find(y)

    def are_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    pass