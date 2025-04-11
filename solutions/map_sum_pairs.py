class TrieNode:
    def __init__(self, key: str | None = None, val: int = 0):
        self.key = key
        self.val = val
        self.is_word = False
        self.children = {}


class MapSumDfs:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        if not key:
            return

        node = self.root

        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)

            node = node.children[ch]

        node.is_word = True
        node.val = val

    def sum(self, prefix: str) -> int:
        if not prefix:
            return 0

        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]

        return self.dfs(node)

    @staticmethod
    def dfs(node: TrieNode) -> int:
        stack = [node]
        total_sum = 0

        while stack:
            current = stack.pop()
            total_sum += current.val

            for child in current.children.values():
                stack.append(child)

        return total_sum


class MapSumPrefixSum:
    def __init__(self):
        self.root = TrieNode()
        self.prefix_sum = {}

    def insert(self, key: str, val: int) -> None:
        if not key:
            return

        diff = val - self.prefix_sum.get(key, 0)
        self.prefix_sum[key] = val

        node = self.root
        node.val += diff

        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)

            node = node.children[ch]
            node.val += diff

    def sum(self, prefix: str) -> int:
        if not prefix:
            return 0

        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]

        return node.val if node else 0


def main():
    map_sum_dfs = MapSumDfs()

    map_sum_dfs.insert("apple", 3)
    assert map_sum_dfs.sum("ap") == 3
    map_sum_dfs.insert("app", 2)
    assert map_sum_dfs.sum("ap") == 5

    map_sum_prefix_sum = MapSumPrefixSum()

    map_sum_prefix_sum.insert("apple", 3)
    assert map_sum_prefix_sum.sum("ap") == 3
    map_sum_prefix_sum.insert("app", 2)
    assert map_sum_prefix_sum.sum("ap") == 5

    print("All tests passed!")


if __name__ == "__main__":
    main()
