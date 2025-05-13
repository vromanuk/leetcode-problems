from typing import Set, Tuple


class Node:
    def __init__(self, key: str | None = None):
        self.key = key
        self.children = {}
        self.word = None


class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        if not word:
            return

        current_node = self.root

        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = Node(ch)
            current_node = current_node.children[ch]

        current_node.word = word


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    if not board or not words:
        return []

    prefix_tree = PrefixTree()
    for word in words:
        prefix_tree.insert(word)

    rows, cols = len(board), len(board[0])
    result = set()

    def dfs(start_row: int, start_col: int) -> None:
        stack = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        if board[start_row][start_col] in prefix_tree.root.children:
            starting_node = prefix_tree.root.children[board[start_row][start_col]]
            stack.append(
                (start_row, start_col, starting_node, {(start_row, start_col)})
            )

            if starting_node.word:
                result.add(starting_node.word)

        while stack:
            r, c, node, seen = stack.pop()

            for dx, dy in directions:
                new_r, new_c = r + dx, c + dy

                if (
                    0 <= new_r < rows
                    and 0 <= new_c < cols
                    and (new_r, new_c) not in seen
                    and board[new_r][new_c] in node.children
                ):
                    next_node = node.children[board[new_r][new_c]]

                    if next_node.word:
                        result.add(next_node.word)

                    stack.append(
                        (
                            new_r,
                            new_c,
                            next_node,
                            seen | {(new_r, new_c)},
                        )
                    )

    for row in range(rows):
        for col in range(cols):
            dfs(row, col)

    return list(result)


def find_words_simplified(board: list[list[str]], words: list[str]) -> list[str]:
    if not board or not board[0] or not words:
        return []

    prefix_tree = PrefixTree()
    for word in words:
        prefix_tree.insert(word)

    result = set()
    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def dfs(row: int, col: int, seen: Set[Tuple[int, int]], node: Node):
        if node.word:
            result.add(node.word)

        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and (new_row, new_col) not in seen
            ):
                ch = board[new_row][new_col]
                if ch in node.children:
                    dfs(
                        new_row,
                        new_col,
                        seen | {(new_row, new_col)},
                        node.children[ch],
                    )

    for i in range(rows):
        for j in range(cols):
            ch = board[i][j]
            if ch in prefix_tree.root.children:
                dfs(i, j, {(i, j)}, prefix_tree.root.children[ch])

    return list(result)


def main():
    assert find_words(
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        ["oath", "pea", "eat", "rain"],
    ) == ["oath", "eat"]
    assert find_words([["a", "b"], ["c", "d"]], ["abcb"]) == []

    assert find_words_simplified(
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        ["oath", "pea", "eat", "rain"],
    ) == ["oath", "eat"]
    assert find_words_simplified([["a", "b"], ["c", "d"]], ["abcb"]) == []

    print("All tests passed!")


if __name__ == "__main__":
    main()
