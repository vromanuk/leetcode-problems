def search(nums: list[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def main():
    assert search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert search(nums=[4, 5, 6, 7, 0, 1, 2], target=2) == 6
    assert search(nums=[4, 5, 6, 7, 0, 1, 2], target=4) == 0
    assert search(nums=[0, 1, 2, 4, 5, 6, 7], target=7) == 6
    assert search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
    assert search(nums=[1], target=0) == -1
    assert search(nums=[1, 3], target=3) == 1
    assert search(nums=[3, 1], target=3) == 0

    print("All tests passed!")


if __name__ == "__main__":
    main()
