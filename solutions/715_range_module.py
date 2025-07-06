class RangeModule:
    def __init__(self):
        self._intervals = []

    def __str__(self):
        return str(self._intervals)

    def add_range(self, left: int, right: int) -> None:
        self._intervals.append([left, right])
        self._intervals.sort(key=lambda i: i[0])
        self._merge()

    def _merge(self) -> None:
        if len(self._intervals) <= 1:
            return

        write_idx = 0
        for read_idx in range(1, len(self._intervals)):
            start, end = self._intervals[read_idx]
            _, last_end = self._intervals[write_idx]

            if start <= last_end:
                self._intervals[write_idx][1] = max(end, last_end)
            else:
                write_idx += 1
                self._intervals[write_idx] = [start, end]

        self._intervals = self._intervals[: write_idx + 1]

    def query_range(self, left: int, right: int) -> bool:
        low, high = 0, len(self._intervals) - 1

        while low <= high:
            mid = (low + high) // 2
            start, end = self._intervals[mid]

            if end < left:
                low = mid + 1
            elif start > left:
                high = mid - 1
            else:
                return end >= right

        return False

    def remove_range(self, left: int, right: int) -> None:
        if not self._intervals:
            return

        new_intervals = []

        for start, end in self._intervals:
            if end <= left or start >= right:
                new_intervals.append([start, end])
            else:
                if start < left:
                    new_intervals.append([start, left])

                if end > right:
                    new_intervals.append([right, end])

        self._intervals = new_intervals


def main():
    range_module = RangeModule()

    # Test case 1: Basic removal
    left, right = 10, 20
    range_module.add_range(left, right)
    assert range_module.query_range(left, right)
    range_module.remove_range(left, right)
    assert not range_module.query_range(left, right)

    # Test case 2: Partial removal
    range_module = RangeModule()
    range_module.add_range(10, 30)
    range_module.remove_range(15, 25)
    assert range_module.query_range(10, 15)
    assert range_module.query_range(25, 30)
    assert not range_module.query_range(15, 25)
    assert not range_module.query_range(10, 30)

    # Test case 3: Remove from multiple intervals
    range_module = RangeModule()
    range_module.add_range(10, 20)
    range_module.add_range(30, 40)
    range_module.remove_range(15, 35)
    assert range_module.query_range(10, 15)
    assert range_module.query_range(35, 40)
    assert not range_module.query_range(15, 20)
    assert not range_module.query_range(30, 35)

    # Test case 4: Remove entire interval
    range_module = RangeModule()
    range_module.add_range(10, 20)
    range_module.remove_range(5, 25)
    assert not range_module.query_range(10, 20)

    print("All tests passed!")


if __name__ == "__main__":
    main()
