from typing import List
from collections import defaultdict


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """
    # 212: Given a 2D board and a list of words from the dictionary, find all words in the board.

    Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells 
    are those horizontally or vertically neighboring. The same letter cell may not be used more than 
    once in a word.
    """
    def _dfs(x: int, y: int, node: TrieNode) -> None:
        if node.word:
            res.append(node.word)
            node.word = None

        if 0 <= x < m and 0 <= y < n and board[x][y] in node.children:
            ch = board[x][y]
            board[x][y] = "#"
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                _dfs(x + dx, y + dy, node.children[ch])
            board[x][y] = ch

    # construct trie
    trie = Trie()
    for word in words:
        trie.add(word)

    res = []
    m, n = len(board), len(board[0])

    # go through board searching for wordds using DFS
    for i in range(m):
        for j in range(n):
            _dfs(i, j, trie.head)

    return res


class TrieNode:
    def __init__(self, word=None):
        self.children = defaultdict(TrieNode)
        self.word = word


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def add(self, word: str) -> None:
        curr = self.head
        for ch in word:
            curr = curr.children[ch]
        curr.word = word


if __name__ == "__main__":
    board = [['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']]
    words = ["oath", "pea", "eat", "rain"]
    assert sorted(find_words(board, words)) == ["eat", "oath"]

    board = [["a", "a"]]
    words = ["a"]
    assert find_words(board, words) == ["a"]

    board = [["a", "b"], ["a", "a"]]
    words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]
    assert sorted(find_words(board, words)) == [
        "aaa", "aaab", "aaba", "aba", "baa"]

    print("Passed all tests!")
