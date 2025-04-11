import heapq


def find_lowest_cost_node(costs: dict[str, int], seen: set[str]) -> str | None:
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in seen:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def find_shortest_path(graph: dict[str, dict[str, int]]) -> int:
    if not graph:
        return -1

    costs = {"end": float("inf")}
    parents = {"end": None}
    seen = set()

    for key in graph.keys():
        if key != "start":
            continue

        start_directions = graph[key]
        parents[key] = "start"

        for direction, cost in start_directions.items():
            costs[direction] = cost

    node = find_lowest_cost_node(costs, seen)

    while node:
        cost = costs[node]
        neighbors = graph[node]

        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]

            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node

        seen.add(node)
        node = find_lowest_cost_node(costs, seen)

    return costs["end"]


def find_shortest_path_optimized(graph: dict[str, dict[str, int]]) -> int:
    if not graph:
        return -1

    costs = {"end": float("inf"), "start": 0}
    parents = {"end": None, "start": None}
    seen = set()

    q = []
    heapq.heappush(q, (0, "start"))

    while q:
        cost, node = heapq.heappop(q)

        if node in seen:
            continue
        seen.add(node)

        for neighbor in graph[node]:
            new_cost = cost + graph[node][neighbor]

            if costs.get(neighbor, float("inf")) > new_cost:
                heapq.heappush(q, (new_cost, neighbor))
                costs[neighbor] = new_cost
                parents[neighbor] = node

    return costs["end"]


def main():
    graph = {
        "start": {"a": 6, "b": 2},
        "a": {"end": 1},
        "b": {"a": 3, "end": 5},
        "end": {},
    }

    assert find_shortest_path(graph) == 6, "Wrong shortest path"
    assert find_shortest_path_optimized(graph) == 6, "Wrong shortest path"

    graph = {
        "start": {"a": 6, "b": 2},
        "a": {"end": 1},
        "b": {"a": 3, "end": 5},
        "end": {},
    }

    assert find_shortest_path(graph) == 6, "Wrong shortest path"
    assert find_shortest_path_optimized(graph) == 6, "Wrong shortest path"

    graph = {
        "start": {"a": 2, "b": 5},
        "a": {"b": 2, "end": 2},
        "b": {"end": 1},
        "end": {},
    }

    assert (
        find_shortest_path(graph) == 4
    ), "Wrong shortest path for graph with multiple paths"
    assert (
        find_shortest_path_optimized(graph) == 4
    ), "Wrong shortest path for graph with multiple paths"

    print("All tests passed!")


if __name__ == "__main__":
    main()
