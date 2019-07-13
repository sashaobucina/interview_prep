"""
Disjoint-set Union/Find with path compression
"""
def disjointFind(data: list, i: int) -> int:
  if i != data[i]:
    data[i] = disjointFind(data, data[i])
  return data[i]

def union(data: list, i: int, j: int) -> None:
  pi, pj = disjointFind(data, i), disjointFind(data, j)
  if pi != pj:
    data[pi] = pj

def isConnected(data: list, i: int, j: int) -> bool:
  return disjointFind(data, i) == disjointFind(data, j)

"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
"""
def friendCircle(M: list) -> int:
  n = len(M)
  data = [i for i in range(n)]

  for i in range(n):
    for j in range(n):
      if i != j and M[i][j] == 1 and not isConnected(data, i, j):
        union(data, i, j)

  s = set()
  for num in data:
    s.add(disjointFind(data, num))
  return(len(s))

if __name__ == "__main__":
  M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
  print(friendCircle(M))