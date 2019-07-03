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

if __name__ == "__main__":
  wordList = ["hit", "hot","dot","dog","lot","log", "cog"]
  print(ladderLength("hit", "cog", wordList))