class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if not word:
            return None

        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()

            current = current.children[ch]

        current.is_word = True

    def search(self, word: str) -> bool:
        if not word:
            return False

        current = self.root

        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]

        return current.is_word

    def startswith(self, prefix: str) -> bool:
        if not prefix:
            return False

        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]

        return True


def main():
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startswith("app") is True

    print("All tests passed!")


if __name__ == "__main__":
    main()
