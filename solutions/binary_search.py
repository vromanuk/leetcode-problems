def binary_search(array: list[int], item: int) -> int:
    if not array or item is None:
        return -1

    left = 0
    right = len(array) - 1

    # Consider my_list = [3] => it won't work with left < right, since left is already < that right
    while left <= right:
        middle = (left + right) // 2
        guess = array[middle]

        if guess == item:
            return middle

        if guess > item:
            right = middle - 1
        else:
            left = middle + 1

    return -1


def main():
    # Test case 1: Element not in the list (less than the smallest element)
    assert (
        binary_search([2, 4, 6, 8, 10], 1) == -1
    ), "Failed: Element 1 should not be found."

    # Test case 2: Element not in the list (greater than the largest element)
    assert (
        binary_search([2, 4, 6, 8, 10], 11) == -1
    ), "Failed: Element 11 should not be found."

    # Test case 3: Element is the first in the list
    assert (
        binary_search([10, 20, 30, 40, 50], 10) == 0
    ), "Failed: Element 10 should be at index 0."

    # Test case 4: Element is the last in the list
    assert (
        binary_search([10, 20, 30, 40, 50], 50) == 4
    ), "Failed: Element 50 should be at index 4."

    # Test case 5: Element is in the middle of the list
    assert (
        binary_search([15, 25, 35, 45, 55], 35) == 2
    ), "Failed: Element 35 should be at index 2."

    # Test case 6: Element not in the list (between two elements)
    assert (
        binary_search([5, 15, 25, 35, 45], 20) == -1
    ), "Failed: Element 20 should not be found."

    # Test case 7: Empty list
    assert (
        binary_search([], 5) == -1
    ), "Failed: Element 5 should not be found in an empty list."

    # Test case 8: Single element list, element present
    assert binary_search([42], 42) == 0, "Failed: Element 42 should be at index 0."

    # Test case 9: Single element list, element absent
    assert (
        binary_search([42], 24) == -1
    ), "Failed: Element 24 should not be found in a single-element list."

    print("All tests passed")


if __name__ == "__main__":
    main()
