from collections import deque


def evaluate_equation(
    equations: list[list[str]], values: list[float], queries: list[list[str]]
) -> list[float]:
    if not equations or not values or not queries:
        return []

    graph = {}

    for idx, (a, b) in enumerate(equations):
        if a not in graph:
            graph[a] = []
        graph[a].append((b, values[idx]))

        if b not in graph:
            graph[b] = []
        graph[b].append((a, 1 / values[idx]))

    def bfs(source, target):
        if source not in graph or target not in graph:
            return -1

        q = deque([(source, 1)])
        seen = set()

        while q:
            node, val = q.popleft()

            if node in seen:
                continue

            if node == target:
                return val

            seen.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in seen:
                    q.append((neighbor, val * weight))

        return -1

    return [bfs(source, target) for source, target in queries]


def main():
    assert evaluate_equation(
        equations=[["a", "b"], ["b", "c"]],
        values=[2.0, 3.0],
        queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    ), [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

    assert evaluate_equation(
        equations=[["a", "b"], ["b", "c"], ["bc", "cd"]],
        values=[1.5, 2.5, 5.0],
        queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
    ), [3.75000, 0.40000, 5.00000, 0.20000]

    assert evaluate_equation(
        equations=[["a", "b"]],
        values=[0.5],
        queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
    ), [0.50000, 2.00000, -1.00000, -1.00000]

    print("All tests passed!!!")


if __name__ == "__main__":
    main()
