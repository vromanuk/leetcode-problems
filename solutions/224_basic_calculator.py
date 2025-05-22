from typing import Iterator


def calculate(s: str) -> int:
    if not s:
        return 0

    def helper(it: Iterator[str]) -> int:
        stack = []
        current_num = 0
        prev_op = "+"

        while True:
            try:
                ch = next(it)
            except StopIteration:
                if prev_op == "+":
                    stack.append(current_num)
                elif prev_op == "-":
                    stack.append(-current_num)
                elif prev_op == "*":
                    last = stack.pop()
                    stack.append(last * current_num)
                elif prev_op == "/":
                    last = stack.pop()
                    stack.append(int(last / current_num))
                break

            if ch.isdigit():
                current_num = 10 * current_num + int(ch)
            elif ch == "(":
                current_num = helper(it)
            elif ch in "+-/*)":
                if prev_op == "+":
                    stack.append(current_num)
                elif prev_op == "-":
                    stack.append(-current_num)
                elif prev_op == "*":
                    last = stack.pop()
                    stack.append(last * current_num)
                elif prev_op == "/":
                    last = stack.pop()
                    stack.append(int(last / current_num))

                if ch == ")":
                    break

                current_num = 0
                prev_op = ch

        return sum(stack)

    return helper(iter(s.strip().replace(" ", "")))


def main():
    assert calculate("1 + 1") == 2
    assert calculate(" 2-1 + 2 ") == 3
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23

    print("All tests passed!")


if __name__ == "__main__":
    main()
