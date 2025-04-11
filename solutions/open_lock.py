from collections import deque


def open_lock(deadends: list[str], target: str) -> int:
    if "0000" in deadends:
        return -1

    seen = set(["0000"])
    deadends = set(deadends)
    q = deque([("0000", 0)])

    while q:
        guess, steps = q.popleft()

        if guess == target:
            return steps

        if guess in deadends:
            continue

        for i in range(4):
            for d in (-1, 1):
                new_digit = (int(guess[i]) + d) % 10
                new_guess = guess[:i] + str(new_digit) + guess[i + 1 :]

                if new_guess not in seen and new_guess not in deadends:
                    seen.add(new_guess)
                    q.append((new_guess, steps + 1))

    return -1


def main():
    assert (
        open_lock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202") == 6
    )
    assert open_lock(deadends=["8888"], target="0009") == 1
    assert (
        open_lock(
            deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
            target="8888",
        )
        == -1
    )

    print("All tests passed!!")


if __name__ == "__main__":
    main()
