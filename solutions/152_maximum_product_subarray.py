def max_product_subarray(nums: list[int]) -> int:
    if not nums:
        return 0

    result = nums[0]
    product = 1

    for n in nums:
        product *= n
        result = max(result, product)

        if product == 0:
            product = 1

    product = 1
    for n in reversed(nums):
        product *= n
        result = max(result, product)

        if product == 0:
            product = 1

    return result


def main():
    assert max_product_subarray([2, 3, -2, 4]) == 6
    assert max_product_subarray([-2, 0, -1]) == 0
    assert max_product_subarray([-2, 3, -4]) == 24

    print("All tests passed!")


if __name__ == "__main__":
    main()
