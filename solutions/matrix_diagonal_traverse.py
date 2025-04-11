from collections import deque


def diagonal_traverse_dfs(matrix: list[list[int]]) -> None:
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (1, -1),
        (-1, 1),
        (1, 1),
        (-1, -1),
    ]  # ↙ ↗ ↘ ↖

    for row in range(rows):
        for col in range(cols):
            print(f"Starting from {matrix[row][col]}:")
            for dx, dy in directions:
                dfs(matrix, row, col, dx, dy, rows, cols)
            print()


def dfs(
    matrix: list[list[int]],
    start_row: int,
    start_col: int,
    dx: int,
    dy: int,
    rows: int,
    cols: int,
) -> None:
    row, col = start_row, start_col
    path = []

    while 0 <= row < rows and 0 <= col < cols:
        path.append(matrix[row][col])
        row += dx
        col += dy

    if path:
        print(" -> ".join(map(str, path)))


def diagonal_traverse_bfs(matrix: list[list[int]]) -> None:
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (1, -1),
        (-1, 1),
        (1, 1),
        (-1, -1),
    ]  # ↙ ↗ ↘ ↖

    for row in range(rows):
        for col in range(cols):
            print(f"\nStarting from {matrix[row][col]}:")

            for dx, dy in directions:
                path = bfs(matrix, row, col, dx, dy, rows, cols)
                print(f"  Path: {' -> '.join(map(str, path))}")


def bfs(
    matrix: list[list[int]],
    start_row: int,
    start_col: int,
    dx: int,
    dy: int,
    rows: int,
    cols: int,
) -> list[int]:
    q = deque([(start_row, start_col)])
    path = []

    while q:
        row, col = q.popleft()

        if 0 <= row < rows and 0 <= col < cols:
            path.append(matrix[row][col])
            q.append((row + dx, col + dy))

    return path


def main():
    """
    Example matrix:
    1 2 3
    4 5 6
    7 8 9
    """
    matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    diagonal_traverse_dfs(matrix_1)

    print()

    diagonal_traverse_bfs(matrix_1)

    print("All good!")


if __name__ == "__main__":
    main()
