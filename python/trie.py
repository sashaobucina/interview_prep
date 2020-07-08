from typing import Optional


class TrieNode:
    def __init__(self, word=None):
        self.word = word
        self.nodes = {}


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        node = self.head
        for ch in word:
            if ch not in node.nodes:
                node.nodes[ch] = TrieNode()
            node = node.nodes[ch]

        node.word = word

    def _search_prefix(self, prefix: str) -> Optional[TrieNode]:
        node = self.head
        for ch in prefix:
            node = node.nodes.get(ch)

            if node is None:
                return None

        return node

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node and node.word is not None

    def startswith(self, prefix: str) -> bool:
        return self._search_prefix(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    for word in ["hell", "hello", "hi"]:
        trie.insert(word)

    assert trie.search("hello")
    assert trie.search("hell")
    assert trie.search("hi")
    assert not trie.search("h")
    assert not trie.search("helloa")

    assert trie.startswith("hel")
    assert trie.startswith("h")

    print("Passed all tests!")
