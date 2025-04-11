from collections import deque


def falling_figure(matrix: list[list[str]]) -> list[list[str]]:
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    q = deque()

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "F":
                q.appendleft((row, col))

    while q:
        obstacle_found = False
        for i in range(len(q)):
            row, col = q[i]
            new_row = row + 1

            if new_row < rows and matrix[new_row][col] == "#":
                obstacle_found = True
                break

        if obstacle_found:
            break
        else:
            for _ in range(len(q)):
                row, col = q.popleft()
                new_row = row + 1

                if new_row < rows and matrix[new_row][col] == "-":
                    matrix[row][col] = "-"
                    matrix[new_row][col] = "F"
                    q.append((new_row, col))

    return matrix


def main():
    matrix1 = [["-", "F", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    expected1 = [["-", "-", "-"], ["-", "-", "-"], ["-", "F", "-"]]
    assert falling_figure(matrix1) == expected1

    matrix2 = [["-", "F", "-"], ["-", "-", "-"], ["#", "#", "-"]]
    expected2 = [["-", "-", "-"], ["-", "F", "-"], ["#", "#", "-"]]
    assert falling_figure(matrix2) == expected2

    matrix3 = [["F"], ["F"], ["F"], ["F"], ["-"], ["-"], ["-"]]
    expected3 = [["-"], ["-"], ["-"], ["F"], ["F"], ["F"], ["F"]]
    assert falling_figure(matrix3) == expected3

    print("All test cases passed!")


if __name__ == "__main__":
    main()
