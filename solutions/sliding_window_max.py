import heapq
from collections import deque


def sliding_window_max_brute_force(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    result = []

    for i in range(len(nums) - k + 1):
        result.append(max(nums[i : i + k]))

    return result


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    result = []
    q = deque()

    for i, num in enumerate(nums):
        if q and i - k + 1 > q[0]:
            q.popleft()

        while q and nums[q[-1]] <= num:
            q.pop()

        q.append(i)

        if i >= k - 1:
            result.append(nums[q[0]])

    return result


def sliding_window_max_heapq(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    result = []
    heap = []

    for i, num in enumerate(nums):
        heapq.heappush(heap, (-num, i))

        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        if i >= k - 1:
            result.append(-heap[0][0])

    return result


def main():
    assert sliding_window_max_brute_force([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        3,
        3,
        5,
        5,
        6,
        7,
    ]
    assert sliding_window_max_brute_force([1], 1) == [1]

    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_max([1], 1) == [1]

    assert sliding_window_max_heapq([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_max_heapq([1], 1) == [1]

    print("All tests passed!")


if __name__ == "__main__":
    main()
