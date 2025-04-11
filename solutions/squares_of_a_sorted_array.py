from collections import deque


def squares_of_sorted_array_deque(nums: list[int]) -> list[int]:
    if not nums:
        return nums

    q = deque(nums)
    result = []

    while q:
        left, right = q[0] ** 2, q[-1] ** 2

        if left > right:
            result.append(left)
            q.popleft()
        else:
            result.append(right)
            q.pop()

    return result[::-1]


def squares_of_sorted_array_reversed(nums: list[int]) -> list[int]:
    if not nums:
        return nums

    result = deque()

    left, right = 0, len(nums) - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result.appendleft(left_square)
            left += 1
        else:
            result.appendleft(right_square)
            right -= 1

    return list(result)


def squares_of_sorted_array(nums: list[int]) -> list[int]:
    if not nums:
        return nums

    result = [0] * len(nums)

    left, right = 0, len(nums) - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[right - left] = left_square
            left += 1
        else:
            result[right - left] = right_square
            right -= 1

    return result


def main():
    assert squares_of_sorted_array_deque([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert squares_of_sorted_array_reversed([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert squares_of_sorted_array([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert squares_of_sorted_array_deque([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert squares_of_sorted_array_reversed([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert squares_of_sorted_array([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

    print("All tests passed!!")


if __name__ == "__main__":
    main()
