import heapq


class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

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

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def min_cost_connect_points_kruskal(points: list[list[int]]) -> int:
    if not points:
        return 0

    n = len(points)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            distance = abs(x1 - x2) + abs(y1 - y2)

            edges.append((distance, i, j))

    edges.sort()

    uf = UnionFind(n)
    min_cost = 0
    edges_used = 0

    for cost, node, next_node in edges:
        if not uf.is_connected(node, next_node):
            uf.union(node, next_node)
            min_cost += cost
            edges_used += 1

            if edges_used == n - 1:
                break

    return min_cost


def min_cost_connect_points_prim(points: list[list[int]]) -> int:
    if not points:
        return 0

    n = len(points)
    graph = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            distance = abs(x1 - x2) + abs(y1 - y2)

            graph[i].append((distance, j))
            graph[j].append((distance, i))

    min_cost = 0
    min_heap = [(0, 0)]
    seen = set()

    while min_heap and len(seen) < n:
        cost, node = heapq.heappop(min_heap)

        if node in seen:
            continue

        seen.add(node)
        min_cost += cost

        for neighbor_cost, neighbor in graph[node]:
            if neighbor not in seen:
                heapq.heappush(min_heap, (neighbor_cost, neighbor))

    return min_cost


def main():
    assert min_cost_connect_points_prim([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert min_cost_connect_points_prim([[3, 12], [-2, 5], [-4, 1]]) == 18

    assert (
        min_cost_connect_points_kruskal([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    )
    assert min_cost_connect_points_kruskal([[3, 12], [-2, 5], [-4, 1]]) == 18

    print("All tests passed!")


if __name__ == "__main__":
    main()
