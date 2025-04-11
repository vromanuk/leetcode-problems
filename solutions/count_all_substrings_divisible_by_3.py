def count_all_substrings_divisible_by_3(s: str) -> int:
    if not s or s.startswith("0"):
        return 0

    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            current_substring = s[i:j]

            if current_substring.startswith("0"):
                continue

            if int(current_substring) % 3 == 0:
                count += 1

    return count


def main():
    # Edge Cases
    assert count_all_substrings_divisible_by_3("") == 0  # Empty string
    assert count_all_substrings_divisible_by_3("3") == 1  # Single digit divisible by 3
    assert count_all_substrings_divisible_by_3("9") == 1  # Single digit divisible by 3
    assert count_all_substrings_divisible_by_3("0") == 0  # Single digit 0 (excluded)

    # Multi-digit numbers
    assert count_all_substrings_divisible_by_3("12") == 1  # "12" (12 is divisible by 3)
    assert count_all_substrings_divisible_by_3("36") == 3  # "3", "6", "36"
    assert count_all_substrings_divisible_by_3("303") == 4  # "3", "3", "30", "303"
    assert (
        count_all_substrings_divisible_by_3("999") == 6
    )  # Every substring is divisible
    assert count_all_substrings_divisible_by_3("123") == 3  # "3", "12", "123"

    # Numbers with leading zeros in substrings
    assert count_all_substrings_divisible_by_3("102") == 1  # "102"
    assert count_all_substrings_divisible_by_3("120") == 2  # "12", "120"

    print("All tests passed!")


if __name__ == "__main__":
    main()
