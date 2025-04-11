def decode_string(s: str) -> str:
    if not s:
        return ""

    stack = []
    curr_num = 0
    curr_str = ""

    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        elif ch == "[":
            stack.append((curr_str, curr_num))
            curr_str, curr_num = "", 0
        elif ch == "]":
            last_str, num = stack.pop()
            curr_str = last_str + num * curr_str
        else:
            curr_str += ch

    return curr_str


def main():
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"

    print("All tests passed successfully!!")


if __name__ == "__main__":
    main()
