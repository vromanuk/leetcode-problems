def three_sum(nums: list[int]) -> list[list[int]]:
    if not nums:
        return []

    result = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = num + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([num, nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


def main():
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([-1, 0, 1, 2, -1, -4, 0, 0]) == [
        [-1, -1, 2],
        [-1, 0, 1],
        [0, 0, 0],
    ]
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([0, 1, 1]) == []

    print("All tests passed!")


if __name__ == "__main__":
    main()
