import collections


class Trie:
    def __init__(self):
        self.nodes = collections.defaultdict(Trie)
        self.is_word = False

    def add_word(self, word):
        current = self
        for c in word:
            current = current.nodes[c]
        current.is_word = True


def word_break(s: str, word_dict: list[str]) -> bool:
    root = Trie()
    for word in word_dict:
        root.add_word(word)

    tries = {root}
    for c in s:
        tries = {trie.nodes[c] for trie in tries if c in trie.nodes}
        if any(trie.is_word for trie in tries):
            tries.add(root)

    return any(trie.is_word for trie in tries)


def main():
    assert (
        word_break("leetcode", ["leet", "code"]) == True
    ), "Failed: leetcode should be breakable into leet and code."
    assert (
        word_break("applepenapple", ["apple", "pen"]) == True
    ), "Failed: applepenapple should be breakable into apple and pen."
    assert (
        word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    ), "Failed: catsandog should not be breakable into cats and dog."

    assert word_break(s="aaaaaaa", word_dict=["aaaa", "aaa"]) == True

    print("All test cases passed!")


if __name__ == "__main__":
    main()
