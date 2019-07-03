import collections

class WordNode():
  def __init__(self, word: str, count: int):
    self.word = word
    self.count = count

  def __repr__(self) -> str:
    return str(self.word)


"""
Given a startWord, endWord, and a dictionary of valid words, find the shortest
transformation sequence with only one letter change.
"""
def ladderLength(startWord: str, endWord: str, wordList: list) -> int:
  validChars = "abcdefghijklmnopqrstuvwxyz"
  wordSet = set(wordList)
  queue = [WordNode(startWord, 1)]
  while len(queue) > 0:
    top = queue.pop(0)
    word = top.word
    if word == endWord:
      return top.count

    for i, ch in enumerate(list(word)):
      for vch in validChars:
        if ch != vch:
          newWord = word[:i] + vch + word[i+1:]
          if newWord in wordSet:
            queue.append(WordNode(newWord, top.count + 1))
            wordSet.remove(newWord)

  return 0

"""
O(M*N) time complexity
"""
def ladderLengthOptimal(beginWord: str, endWord: str, wordList: list) -> int:
  n, d, q = len(beginWord), collections.defaultdict(list), collections.deque()

  for word in wordList:
    for i in range(n):
      d[word[:i] + "*" + word[i+1:]].append(word)
  
  q.append(WordNode(beginWord, 1))
  visited = collections.defaultdict(bool)
  visited[beginWord] = True
  while q:
    top = q.popleft()
    curr, currWord = top.count, top.word
    for i in range(n):
      derivedWord = currWord[:i] + "*" + currWord[i+1:]
      for word in d[derivedWord]:
        if word == endWord:
          return curr + 1
        if derivedWord not in visited:
          visited[word] = True
          q.append(WordNode(word, curr + 1))
    d[derivedWord] = []

  # if endWord not in the given word list
  return 0

if __name__ == "__main__":
  wordList = ["hit", "hot","dot","dog","lot","log", "cog"]
  print(ladderLengthOptimal("hit", "cog", wordList))