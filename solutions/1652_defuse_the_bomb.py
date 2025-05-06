def decrypt_prefix_sum(code: list[int], k: int) -> list[int]:
    if not code:
        return []

    if k == 0:
        return [0] * len(code)

    prefix_sum = [0]

    for c in code:
        prefix_sum.append(c + prefix_sum[-1])

    n = len(code)
    result = [0] * n

    for i in range(n):
        if k > 0:
            """
            Example:
            code:       [3, 1, 4, 2]
            prefix_sum: [0, 3, 4, 8, 10]
            k = 2

            For i = 0:
            - We need the sum of the next k elements (wrapping if needed)
            - end_index = (0 + 2) % 4 = 2
            - result[0] = prefix_sum[end_index + 1] - prefix_sum[i + 1]
                       = prefix_sum[3] - prefix_sum[1] = 8 - 3 = 5

            Visually:
            [3, 1, 4, 2]  (original array)
             0  1  2  3   (indices)
                [sum]     (range from i+1 to end_index)

            We're summing:
            (1 + 4) = 5

            For i = 3 (example of circular case):
            - end_index = (3 + 2) % 4 = 1
            - Since end_index < i, we wrap around the array
            - result[3] = (prefix_sum[n] - prefix_sum[i+1]) + prefix_sum[end_index+1]
                       = (prefix_sum[4] - prefix_sum[4]) + prefix_sum[2]
                       = (10 - 10) + 4 = 4

            Visually:
            [3, 1, 4, 2]  (original array)
             0  1  2  3   (indices)
             [s]      [s] (sum wraps around)

            We're summing:
            (3 + 1) = 4
              ^     ^
              |     |
            index 0 index 1 (after wrapping)
            """
            end_index = (i + k) % n

            if end_index > i:
                result[i] = prefix_sum[end_index + 1] - prefix_sum[i + 1]
            else:
                result[i] = (prefix_sum[n] - prefix_sum[i + 1]) + (
                    prefix_sum[end_index + 1]
                )
        else:
            start_index = (i + k) % n

            if start_index < i:
                result[i] = prefix_sum[i] - prefix_sum[start_index]
            else:
                result[i] = (prefix_sum[i] + prefix_sum[n]) - prefix_sum[start_index]

    return result


def decrypt(code: list[int], k: int) -> list[int]:
    if not code:
        return []

    if k == 0:
        return [0] * len(code)

    result = []
    n = len(code)

    for i in range(n):
        current_sum = 0

        for j in range(1, abs(k) + 1):
            if k > 0:
                index = (i + j) % n
            else:
                index = (i - j) % n

            current_sum += code[index]

        result.append(current_sum)

    return result


def main():
    assert decrypt_prefix_sum([5, 7, 1, 4], 3) == [12, 10, 16, 13]
    assert decrypt_prefix_sum([1, 2, 3, 4], 0) == [0, 0, 0, 0]
    assert decrypt_prefix_sum([2, 4, 9, 3], -2) == [12, 5, 6, 13]

    assert decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
    assert decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
    assert decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]

    print("All tests passed!")


if __name__ == "__main__":
    main()
