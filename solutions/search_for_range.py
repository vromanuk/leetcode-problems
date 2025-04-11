def search_for_range(nums: list[int], target: int) -> list[int]:
    if not nums:
        return [-1, -1]

    if len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        else:
            return [-1, -1]

    left, right = 0, len(nums) - 1

    while left + 1 < right:
        middle = (left + right) // 2

        if nums[middle] == target:
            if nums[middle + 1] >= target:
                right = middle
            else:
                left = middle
        else:
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

    if nums[left] == target and nums[right] == target:
        return [left, right]

    if nums[right] == target:
        return [right, right]

    if nums[left] == target and nums[right] != target:
        return [left, left]

    return [-1, -1]


def main():
    assert search_for_range(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    assert search_for_range(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
    assert search_for_range(nums=[1], target=1) == [0, 0]
    assert search_for_range(nums=[1, 1], target=1) == [0, 1]
    assert search_for_range(nums=[8, 8, 8, 8, 8], target=8) == [0, 1]
    assert search_for_range(nums=[1, 3], target=1) == [0, 0]
    assert search_for_range(nums=[1, 4], target=4) == [1, 1]
    assert search_for_range(nums=[1, 2, 2], target=2) == [1, 1]

    print("All tests passed!")


if __name__ == "__main__":
    main()
