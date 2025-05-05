from collections import deque


def find_k_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    if not arr:
        return []

    # Binary search to find the insert position for x
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    # Two pointers to find k closest elements
    left, right = left - 1, left
    result = deque()

    while k > 0:
        if left < 0:
            result.append(arr[right])
            right += 1
        elif right >= len(arr):
            result.appendleft(arr[left])
            left -= 1
        elif abs(arr[left] - x) <= abs(arr[right] - x):
            result.appendleft(arr[left])
            left -= 1
        else:
            result.append(arr[right])
            right += 1
        k -= 1

    return list(result)


def main():
    assert find_k_closest_elements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    assert find_k_closest_elements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]

    print("All tests passed!")


if __name__ == "__main__":
    main()
