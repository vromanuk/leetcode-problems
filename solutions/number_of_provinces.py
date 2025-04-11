class UnionFind:
    def __init__(self, size: int = 0):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def get_count(self):
        return self.count


def find_circle_num(is_connected: list[list[int]]) -> int:
    if not is_connected:
        return 0

    n = len(is_connected)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(n):
            if is_connected[i][j] == 1:
                uf.union(i, j)

    return uf.get_count()


def main():
    assert find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert find_circle_num([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3

    print("All tests passed!")


if __name__ == "__main__":
    main()
