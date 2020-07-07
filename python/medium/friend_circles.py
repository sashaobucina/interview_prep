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


def find_circle_num(M: List[List[int]]) -> int:
    """
    # 547: There are N students in a class. Some of them are friends, while some are not.

    Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a 
    direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group 
    of students who are direct or indirect friends.

    Given a N*N matrix M representing the friend relationship between students in the class. 
    If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
    And you have to output the total number of friend circles among all the students.

    NOTE:
        - N is in range [1,200].
        - M[i][i] = 1 for all students.
        - If M[i][j] = 1, then M[j][i] = 1.
    """
    m, n = len(M), len(M[0])

    data = list(range(m))
    dsu = DSU(data)
    for i in range(m):
        for j in range(i + 1, n):
            if M[i][j]:
                dsu.union(i, j)

    return len(set([dsu.find(x) for x in data]))


if __name__ == "__main__":
    M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    assert find_circle_num(M) == 2

    M = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    assert find_circle_num(M) == 1

    print("Passed all tests!")
