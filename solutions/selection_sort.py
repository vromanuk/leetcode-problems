def selection_sort_in_place(array: list[int]) -> list[int]:
    if not array:
        return array

    length = len(array)

    for i in range(0, length):
        min_index = i

        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array


def _find_min_index(array: list[int]) -> int | None:
    if not array:
        return None

    current_min_index = 0

    for idx in range(0, len(array)):
        if array[current_min_index] > array[idx]:
            current_min_index = idx

    return current_min_index


def selection_sort(array: list[int]) -> list[int]:
    if not array:
        return array

    copied = list(array)
    result = []

    for _ in range(0, len(copied)):
        min_index = _find_min_index(copied)
        result.append(copied.pop(min_index))

    return result


def main():
    # Basic test cases
    assert selection_sort_in_place([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
    assert selection_sort_in_place([-1, 3, 0, 2, 321]) == [-1, 0, 2, 3, 321]
    assert selection_sort_in_place([10, 9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9, 10]
    assert selection_sort_in_place([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

    assert selection_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
    assert selection_sort([-1, 3, 0, 2, 321]) == [-1, 0, 2, 3, 321]
    assert selection_sort([10, 9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9, 10]
    assert selection_sort([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

    # Edge cases
    assert selection_sort_in_place([]) == []
    assert selection_sort([]) == []
    assert selection_sort_in_place([1]) == [1]
    assert selection_sort([1]) == [1]

    # Large numbers
    assert selection_sort_in_place([1000000, 999999]) == [999999, 1000000]
    assert selection_sort([1000000, 999999]) == [999999, 1000000]

    # Negative numbers
    assert selection_sort_in_place([-5, -10, -3, -8]) == [-10, -8, -5, -3]
    assert selection_sort([-5, -10, -3, -8]) == [-10, -8, -5, -3]

    # Mixed positive and negative
    assert selection_sort_in_place([-1, 2, -3, 4, -5]) == [-5, -3, -1, 2, 4]
    assert selection_sort([-1, 2, -3, 4, -5]) == [-5, -3, -1, 2, 4]

    # Already sorted array
    assert selection_sort_in_place([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Reverse sorted array
    assert selection_sort_in_place([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Duplicate numbers
    assert selection_sort_in_place([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [
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
    assert selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [
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
    assert selection_sort_in_place([-1, -1, -2, -2, -3, -3]) == [-3, -3, -2, -2, -1, -1]
    assert selection_sort([-1, -1, -2, -2, -3, -3]) == [-3, -3, -2, -2, -1, -1]

    # Large array
    large_array = list(range(100, 0, -1))  # [100, 99, ..., 1]
    assert selection_sort_in_place(large_array) == list(
        range(1, 101)
    )  # [1, 2, ..., 100]
    assert selection_sort(large_array) == list(range(1, 101))  # [1, 2, ..., 100]

    print("All tests passed")


if __name__ == "__main__":
    main()
