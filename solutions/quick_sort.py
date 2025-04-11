def quick_sort(array: list[int]) -> list[int]:
    if not array:
        return array

    if len(array) < 2:
        return array

    pivot = array[0]

    left = [i for i in array[1:] if i <= pivot]
    right = [i for i in array[1:] if i > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


def main():
    # Basic test cases
    assert quick_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
    assert quick_sort([-1, 3, 0, 2, 321]) == [-1, 0, 2, 3, 321]
    assert quick_sort([10, 9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9, 10]
    assert quick_sort([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

    # Edge cases
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([2, 1]) == [1, 2]

    # Large numbers
    assert quick_sort([1000000, 999999]) == [999999, 1000000]

    # Negative numbers
    assert quick_sort([-5, -10, -3, -8]) == [-10, -8, -5, -3]

    # Mixed positive and negative
    assert quick_sort([-1, 2, -3, 4, -5]) == [-5, -3, -1, 2, 4]

    # Already sorted array
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Reverse sorted array
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Duplicate numbers
    assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [
        1,
        1,
        2,
        3,
        3,
        4,
        5,
        5,
        5,
        6,
        9,
    ]

    # All negative numbers
    assert quick_sort([-1, -1, -2, -2, -3, -3]) == [-3, -3, -2, -2, -1, -1]

    # Large array
    large_array = list(range(100, 0, -1))  # [100, 99, ..., 1]
    assert quick_sort(large_array) == list(range(1, 101))  # [1, 2, ..., 100]

    print("All tests passed")


if __name__ == "__main__":
    main()
