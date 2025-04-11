from collections import deque


class UnionFind:
    def __init__(self, size: int = 0):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if self.root[x] == x:
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


def smallest_string_with_swaps_union_find(s: str, pairs: list[list[int]]) -> str:
    if not (s or pairs):
        return s

    n = len(s)
    uf = UnionFind(n)

    for a, b in pairs:
        uf.union(a, b)

    groups_index = {}
    groups_ch = {}

    for i in range(n):
        root = uf.find(i)

        if root not in groups_index:
            groups_index[root] = []
        if root not in groups_ch:
            groups_ch[root] = []

        groups_index[root].append(i)
        groups_ch[root].append(s[i])

    result = [""] * n

    for group in groups_index:
        idx = sorted(groups_index[group])
        chars = sorted(groups_ch[group])

        for i, c in zip(idx, chars):
            result[i] = c

    return "".join(result)


def smallest_string_with_swaps_brute_force(s: str, pairs: list[list[int]]) -> str:
    if not (s or pairs):
        return ""

    smallest = s
    seen = set()
    q = deque([s])

    while q:
        current = q.popleft()

        if current in seen:
            continue

        seen.add(current)

        smallest = min(smallest, current)

        for a, b in pairs:
            swapped = list(current)
            swapped[a], swapped[b] = swapped[b], swapped[a]
            swapped_str = "".join(swapped)

            if swapped_str not in seen:
                q.append(swapped_str)

    return smallest


def smallest_string_with_swaps_bfs(s: str, pairs: list[list[int]]) -> str:
    if not s or not pairs:
        return s

    def bfs(root):
        q = deque([root])
        component = []

        while q:
            current = q.popleft()

            if current in seen:
                continue

            seen.add(current)
            component.append(current)

            for neighbor in graph[current]:
                if neighbor not in seen:
                    q.append(neighbor)

        return component

    n = len(s)
    seen = set()
    graph = {i: [] for i in range(n)}

    for a, b in pairs:
        graph[a].append(b)
        graph[b].append(a)

    result = list(s)

    for i in range(n):
        if i not in seen:
            component = bfs(i)

            sorted_indices = sorted(component)
            sorted_chars = sorted(s[idx] for idx in sorted_indices)

            for idx, ch in zip(sorted_indices, sorted_chars):
                result[idx] = ch

    return "".join(result)


def main():
    assert smallest_string_with_swaps_brute_force("dcab", [[0, 3], [1, 2]]) == "bacd"
    assert (
        smallest_string_with_swaps_brute_force("dcab", [[0, 3], [1, 2], [0, 2]])
        == "abcd"
    )
    assert smallest_string_with_swaps_brute_force("cba", [[0, 1], [1, 2]]) == "abc"

    assert smallest_string_with_swaps_union_find("dcab", [[0, 3], [1, 2]]) == "bacd"
    assert (
        smallest_string_with_swaps_union_find("dcab", [[0, 3], [1, 2], [0, 2]])
        == "abcd"
    )
    assert smallest_string_with_swaps_union_find("cba", [[0, 1], [1, 2]]) == "abc"

    assert smallest_string_with_swaps_bfs("dcab", [[0, 3], [1, 2]]) == "bacd"
    assert smallest_string_with_swaps_bfs("dcab", [[0, 3], [1, 2], [0, 2]]) == "abcd"
    assert smallest_string_with_swaps_bfs("cba", [[0, 1], [1, 2]]) == "abc"

    print("All tests passed!")


if __name__ == "__main__":
    main()
