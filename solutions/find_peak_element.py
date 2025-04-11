def find_peak_element(nums: list[int]) -> int:
    if not nums or len(nums) < 2:
        return 0

    left, right = 0, len(nums) - 1

    while left < right:
        middle = (left + right) // 2

        if nums[middle] > nums[middle + 1]:
            right = middle
        else:
            left = middle + 1

    return left


def main():
    assert find_peak_element([1, 2, 3, 1]) == 2
    assert find_peak_element([1, 2, 1, 3, 5, 6, 4]) == 5
    assert find_peak_element([5, 6, 4]) == 1
    assert find_peak_element([5, 6]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    main()
