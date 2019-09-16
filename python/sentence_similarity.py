import itertools

class DSU:
  def __init__(self, n: int):
    self.p = list(range(n))

  def find(self, x):
    if self.p[x] != x:
      self.p[x] = self.find(self.p[x])
    return self.p[x]

  def union(self, x, y):
    self.p[self.find(x)] = self.find(y)

"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word 
pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar 
word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is not transitive. For example, if "great" and 
"fine" are similar, and "fine" and "good" are similar, "great" and "good" are not 
necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being similar 
is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences 
words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there 
are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. 
So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
"""
def are_sentences_similar(words1: list, words2: list, pairs: list) -> bool:
  if len(words1) != len(words2):
    return False

  pairset = set(map(tuple, pairs))
  return all(w1 == w2 or (w1, w2) in pairset or (w2, w1) in pairset for w1, w2 in zip(words1, words2))

"""
Same as first, but the similarity relation is transitive.
"""
def are_sentences_similar_II(words1: list, words2: list, pairs: list) -> bool:
  if len(words1) != len(words2):
    return False

  index = {}
  counter = itertools.count()
  dsu = DSU(2 * len(pairs))

  for pair in pairs:
    for p in pair:
      if p not in index:
        index[p] = next(counter)
    dsu.union(index[pair[0]], index[pair[1]])

  return all(
    (w1 == w2) or 
    (w1 in index and w2 in index and dsu.find(index[w1]) == dsu.find(index[w2]))
    for w1, w2 in zip(words1, words2)
  )


if __name__ == "__main__":
  words1, words2 = ["great","acting","skills"] ,["fine","drama","talent"]
  pairs = [["great","fine"],["drama","acting"],["skills","talent"]]
  print(are_sentences_similar(words1, words2, pairs))   # expected: true

  print(are_sentences_similar_II(words1, words2, pairs))    # expected: true