def h_index_sorting(citations: list[int]) -> int:
    if not citations:
        return 0

    citations.sort(reverse=True)

    result = 0

    for i, citation in enumerate(citations):
        if i + 1 <= citation:
            result = i + 1
        else:
            break

    return result


def h_index_brute_force(citations: list[int]) -> int:
    if not citations:
        return 0

    result = 0

    for h in range(1, len(citations) + 1):
        count = 0

        for citation in citations:
            if citation >= h:
                count += 1

        if count >= h:
            result = h

    return result


def h_index_binary_search(citations: list[int]) -> int:
    if not citations:
        return 0

    citations.sort()

    left, right = 0, len(citations) - 1

    while left <= right:
        middle = (left + right) // 2
        h = len(citations) - middle

        if citations[middle] >= h:
            right = middle - 1
        else:
            left = middle + 1

    return len(citations) - left


def h_index_bucket_sort(citations: list[int]) -> int:
    if not citations:
        return 0

    buckets = [0] * (len(citations) + 1)

    for citation in citations:
        if citation >= len(buckets):
            buckets[-1] += 1
        else:
            buckets[citation] += 1

    h_index = 0

    for h in range(len(buckets) - 1, -1, -1):
        h_index += buckets[h]

        if h_index >= h:
            return h

    return h_index


def main():
    assert h_index_sorting([3, 0, 6, 1, 5]) == 3
    assert h_index_sorting([1, 3, 10, 2, 5]) == 3
    assert h_index_sorting([1, 3, 1]) == 1

    assert h_index_brute_force([3, 0, 6, 1, 5]) == 3
    assert h_index_brute_force([1, 3, 10, 2, 5]) == 3
    assert h_index_brute_force([1, 3, 1]) == 1

    assert h_index_binary_search([3, 0, 6, 1, 5]) == 3
    assert h_index_binary_search([1, 3, 10, 2, 5]) == 3
    assert h_index_binary_search([1, 3, 1]) == 1

    assert h_index_bucket_sort([3, 0, 6, 1, 5]) == 3
    assert h_index_bucket_sort([1, 3, 10, 2, 5]) == 3
    assert h_index_bucket_sort([1, 3, 1]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    main()
