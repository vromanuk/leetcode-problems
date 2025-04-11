def remove_duplicates_from_sorted_array(nums: list[int]) -> int:
    if not nums:
        return 0

    left = 1

    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1

    return left


def main():
    assert remove_duplicates_from_sorted_array([1, 1, 2]) == 2
    assert remove_duplicates_from_sorted_array(nums=[1, 2, 3, 4, 5]) == 5
    assert remove_duplicates_from_sorted_array(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5

    print("All tests passed!")


if __name__ == "__main__":
    main()
