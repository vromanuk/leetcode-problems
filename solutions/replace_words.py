class TrieNode:
    def __init__(self, key: str | None = None):
        self.key = key
        self.children = {}
        self.is_end = False

    def __repr__(self):
        return (
            f"TrieNode(key={self.key}, children={self.children}, is_end={self.is_end})"
        )


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if not word:
            return None

        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]

        node.is_end = True

    def get_shortest_prefix(self, word: str) -> str:
        node = self.root

        prefix = ""
        for ch in word:
            if ch not in node.children:
                break

            node = node.children[ch]
            prefix += ch

            if node.is_end:
                return prefix

        return word


def replace_words(dictionary: list[str], sentence: str) -> str:
    if not dictionary or not sentence:
        return sentence

    trie = Trie()

    for word in dictionary:
        trie.insert(word)

    return " ".join(trie.get_shortest_prefix(word) for word in sentence.split())


def main():
    assert (
        replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery")
        == "the cat was rat by the bat"
    )
    assert replace_words(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs") == "a a b c"
    assert (
        replace_words(
            ["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
        )
        == "a a a a a a a a bbb baba a"
    )

    print("All tests passed!")


if __name__ == "__main__":
    main()
