from typing import List


class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.word = ""


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def add(self, word: str) -> None:
        curr = self.head
        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = TrieNode()
            curr = curr.nodes[ch]

        curr.word = word


def word_break(s: str, word_dict: List[str]) -> List[str]:
    """
    # 140: Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
    add spaces in s to construct a sentence where each word is a valid dictionary word. 
    Return all such possible sentences.

    NOTE:
        - The same word in the dictionary may be reused multiple times in the segmentation.
        - You may assume the dictionary does not contain duplicate words. 
    """
    # construct trie
    trie = Trie()
    dict_set = set()
    for word in word_dict:
        trie.add(word)
        dict_set.update(set(word))

    ans = []
    N = len(s)

    if len(dict_set) < len(set(s)):
        return []

    def search(i: int, node: TrieNode, words: List[str]):
        if i == len(s):
            if node.word:
                ans.append(" ".join(words + [node.word]))
            return

        if node.word:
            search(i, trie.head, words + [node.word])

        next_node = node.nodes.get(s[i], None)
        if next_node:
            search(i + 1, next_node, words)

    # perform search for all sentences
    search(0, trie.head, [])

    return ans


if __name__ == "__main__":
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    word_dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    assert word_break(s, word_dict) == []

    s = "catsandogs"
    word_dict = ["cats", "dogs", "and", "sand"]
    assert word_break(s, word_dict) == []

    print("Passed all tests!")
