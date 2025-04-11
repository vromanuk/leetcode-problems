from collections import deque


def word_exists_bfs(board: list[list[str]], word: str) -> bool:
    if not board or not word:
        return False

    rows, cols = len(board), len(board[0])

    char_count = {}

    for row in range(rows):
        for col in range(cols):
            char_count[board[row][col]] = char_count.get(board[row][col], 0) + 1

    for ch in word:
        if ch not in char_count or char_count[ch] == 0:
            return False
        char_count[ch] -= 1

    def bfs(start_row: int, start_col: int) -> bool:
        q = deque([(start_row, start_col, 0, {(start_row, start_col)})])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c, index, visited = q.popleft()

            if index == len(word) - 1:
                return True

            for dx, dy in directions:
                new_row, new_col = r + dx, c + dy

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and (new_row, new_col) not in visited
                    and board[new_row][new_col] == word[index + 1]
                ):
                    q.append(
                        (new_row, new_col, index + 1, visited | {(new_row, new_col)})
                    )

        return False

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0] and bfs(row, col):
                return True

    return False


def word_exists_dfs(board: list[list[str]], word: str) -> bool:
    if not board or not word:
        return False

    rows, cols = len(board), len(board[0])

    char_count = {}

    for i in range(rows):
        for j in range(cols):
            char_count[board[i][j]] = char_count.get(board[i][j], 0) + 1

    for ch in word:
        if ch not in char_count or char_count[ch] == 0:
            return False
        char_count[ch] -= 1

    def dfs(start_row: int, start_col: int, index: int) -> bool:
        stack = [(start_row, start_col, index, {(start_row, start_col)})]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while stack:
            r, c, index, visited = stack.pop()

            if index == len(word) - 1:
                return True

            for dx, dy in directions:
                new_row, new_col = r + dx, c + dy

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and (new_row, new_col) not in visited
                    and board[new_row][new_col] == word[index + 1]
                ):
                    stack.append(
                        (new_row, new_col, index + 1, visited | {(new_row, new_col)})
                    )

        return False

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0] and dfs(row, col, 0):
                return True
    return False


def main():
    assert (
        word_exists_bfs(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="ABCCED",
        )
        is True
    )
    assert (
        word_exists_dfs(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="ABCCED",
        )
        is True
    )

    assert (
        word_exists_bfs(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="SEE",
        )
        is True
    )
    assert (
        word_exists_dfs(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="SEE",
        )
        is True
    )

    assert (
        word_exists_bfs(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="ABCB",
        )
        is False
    )

    assert (
        word_exists_dfs(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="ABCB",
        )
        is False
    )

    print("All tests passed!")


if __name__ == "__main__":
    main()
