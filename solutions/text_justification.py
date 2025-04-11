def justify_line(line: list[str], max_width: int, is_last_line: bool) -> str:
    if is_last_line or len(line) == 1:
        # Join words with a single space and pad the end with spaces if it's the last line or a single word
        return " ".join(line) + " " * (
            max_width - sum(len(word) for word in line) - (len(line) - 1)
        )

    total_spaces = max_width - sum(len(word) for word in line)
    spaces_between_words = len(line) - 1
    space, extra = divmod(total_spaces, spaces_between_words)

    for i in range(extra):
        line[i] += " "

    return (" " * space).join(line)


def text_justify(words: list[str], maxWidth: int) -> list[str]:
    result = []

    current_line = []
    current_length = 0

    for word in words:
        if len(word) + len(current_line) + current_length <= maxWidth:
            current_line.append(word)
            current_length += len(word)
        else:
            result.append(current_line)
            current_line = [word]
            current_length = len(word)

    if current_line:
        result.append(current_line)

    for i, line in enumerate(result):
        result[i] = justify_line(line, maxWidth, i == len(result) - 1)

    return result


def main():
    assert text_justify(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
    ) == ["This    is    an", "example  of text", "justification.  "]
    assert text_justify(
        words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16
    ) == ["What   must   be", "acknowledgment  ", "shall be        "]

    print("All test cases passed!")


if __name__ == "__main__":
    main()
