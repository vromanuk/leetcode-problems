def calculate(s: str) -> int:
    if not s:
        return 0

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y),  # truncate toward zero
    }

    s = s.strip()
    stack = []
    current_num = 0
    prev_op = "+"

    for i, ch in enumerate(s):
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        if ch in operations or i == len(s) - 1:
            if prev_op == "+":
                stack.append(current_num)
            elif prev_op == "-":
                stack.append(-current_num)
            elif prev_op in "/*":
                last = stack.pop()
                stack.append(operations[prev_op](last, current_num))

            prev_op = ch
            current_num = 0

    return sum(stack)


def main():
    assert calculate("3+2*2") == 7
    assert calculate(" 3/2 ") == 1
    assert calculate(" 3+5 / 2 ") == 5

    print("All tests passed!")


if __name__ == "__main__":
    main()
