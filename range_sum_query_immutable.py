class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix_sum = [0]

        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sum_range(self, left: int, right: int) -> int:
        """
        Returns the sum of elements in the array from index 'left' to 'right' (inclusive).

        The key insight:
        If we want to get the sum of the range [left, right], we need to:
        1. Take the prefix sum up to the right index (including it): prefix_sum[right+1]
        2. Subtract the prefix sum up to the left index (excluding it): prefix_sum[left]

        Example:
        nums:       [3, 2, 1, 3, 1, 4, 2]
        prefix_sum: [0, 3, 5, 6, 9, 10, 14, 16]

        For range [2, 5], we calculate:
        prefix_sum[right+1] - prefix_sum[left] = prefix_sum[6] - prefix_sum[2] = 14 - 5 = 9

        Visually:
        [3, 2, 1, 3, 1, 4, 2]  (original array)
         0  1  2  3  4  5  6   (indices)
            [     sum     ]    (range [2,5])

        We're essentially taking:
        [3, 2, 1, 3, 1, 4] - [3, 2]
               ^        ^
               |        |
             left      right
        """
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


def main():
    num_array = NumArray([-2, 0, 3, -5, 2, -1])

    assert num_array.sum_range(0, 2) == 1  # return (-2) + 0 + 3 = 1
    assert num_array.sum_range(2, 5) == -1  # return 3 + (-5) + 2 + (-1) = -1
    assert num_array.sum_range(0, 5) == -3  # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

    print("All tests passed!")


if __name__ == "__main__":
    main()
