def zig_zag_convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    result = [""] * num_rows
    row, jump = 0, 1

    for char in s:
        result[row] += char

        if row == 0:
            jump = 1
        elif row == num_rows - 1:
            jump = -1

        row += jump

    return "".join(result)


def main():
    assert zig_zag_convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert zig_zag_convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


if __name__ == "__main__":
    main()
