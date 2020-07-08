class TrieNode:
    def __init__(self, word=None):
        self.word = word
        self.nodes = {}


class WordDictionary:
    """
    # 211: Design a data structure that supports the following two operations:

        - void addWord(word)
        - bool search(word)

    search(word) can search a literal word or a regular expression string containing only letters a-z 
    or .. A . means it can represent any one letter.

    NOTE: You may assume that all words are consist of lowercase letters a-z.
    """

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.nodes:
                node.nodes[ch] = TrieNode()

            node = node.nodes[ch]

        node.word = word

    def search(self, word: str) -> str:
        def _search(node: TrieNode, word: str) -> bool:
            if word == "":
                return node.word is not None

            ch, word = word[0], word[1:]
            if ch == ".":
                return any([_search(node.nodes[k], word) for k in node.nodes])

            if ch not in node.nodes:
                return False
            return _search(node.nodes[ch], word)

        return _search(self.root, word)


if __name__ == "__main__":
    word_dict = WordDictionary()

    for word in ["at", "and", "an", "add"]:
        word_dict.add_word(word)

    assert not word_dict.search("a")
    assert not word_dict.search(".at")

    word_dict.add_word("bat")

    assert word_dict.search(".at")
    assert word_dict.search("an.")
    assert word_dict.search("a.d")
    assert not word_dict.search("a.d.")
    assert not word_dict.search(".an")
    assert not word_dict.search("b.")
    assert not word_dict.search(".")

    print("Passed all tests!")
