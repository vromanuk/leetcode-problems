def range_sum(nums: list[int], n: int, left: int, right: int) -> int:
    MOD = 10**9 + 7
    if not nums:
        return 0

    prefix_sum = [0]

    for n in nums:
        prefix_sum.append(n + prefix_sum[-1])

    all_sums = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            all_sums.append(prefix_sum[j] - prefix_sum[i])

    all_sums.sort()

    return sum(all_sums[left - 1 : right]) % MOD


def main():
    assert range_sum([1, 2, 3, 4], 4, 1, 5) == 13
    assert range_sum([1, 2, 3, 4], 4, 3, 4) == 6
    assert range_sum([1, 2, 3, 4], 4, 1, 10) == 50

    print("All tests passed!")


if __name__ == "__main__":
    main()
