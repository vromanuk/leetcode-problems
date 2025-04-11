from collections import deque, Counter


def min_stickers(stickers: list[str], target: str) -> int:
    if not (stickers and target):
        return 0

    sticker_counts = [Counter(sticker) for sticker in stickers]
    queue = deque([(target, 0)])
    visited = {target}

    while queue:
        current, steps = queue.popleft()

        if not current:
            return steps

        current_count = Counter(current)

        for sticker_count in sticker_counts:
            if any(sticker_count[char] > 0 for char in current_count):
                new_state = []
                for char in current_count:
                    if current_count[char] > sticker_count[char]:
                        new_state.append(
                            char * (current_count[char] - sticker_count[char])
                        )

                new_state = "".join(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

    return -1


def main():
    assert min_stickers(stickers=["with", "example", "science"], target="thehat") == 3
    assert min_stickers(stickers=["notice", "possible"], target="basicbasic") == -1

    print("All tests passed!")


if __name__ == "__main__":
    main()
