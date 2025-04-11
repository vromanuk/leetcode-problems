def is_palindrome(s: str) -> bool:
    if not s:
        return False

    left, right = 0, len(s) - 1

    while left <= right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def main():
    assert is_palindrome("abba") == True
    assert is_palindrome("abb") == False
    assert is_palindrome("ab") == False
    assert is_palindrome("a") == True
    assert is_palindrome("aa") == True
    assert is_palindrome("aba") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("A man, a plan, a canal: Panama") == True

    print("All test cases passed!")


if __name__ == "__main__":
    main()
