def duplicate_zeros(arr: list[int]) -> None:
    if not arr:
        return

    i = 0

    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 1

        i += 1


def duplicate_zeros_in_place(arr: list[int]) -> None:
    if not arr:
        return

    zeros = 0

    for n in arr:
        if n == 0:
            zeros += 1

    for i in range(len(arr) - 1, -1, -1):
        if i + zeros < len(arr):
            arr[i + zeros] = arr[i]

        if arr[i] == 0:
            zeros -= 1
            if i + zeros < len(arr):
                arr[i + zeros] = 0


def main():
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros(arr)
    assert arr == [1, 0, 0, 2, 3, 0, 0, 4]

    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros_in_place(arr)
    assert arr == [1, 0, 0, 2, 3, 0, 0, 4]

    arr = [1, 2, 3]
    duplicate_zeros(arr)
    assert arr == [1, 2, 3]

    arr = [1, 2, 3]
    duplicate_zeros_in_place(arr)
    assert arr == [1, 2, 3]

    print("All tests passed!")


if __name__ == "__main__":
    main()
