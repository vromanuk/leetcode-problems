def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    if not nums1 or not nums2:
        return

    if not nums2:
        return

    last = m + n - 1
    i = m - 1
    j = n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1

        last -= 1


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    assert nums1 == [1]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    assert nums1 == [1]

    print("All tests passed!!")


if __name__ == "__main__":
    main()
