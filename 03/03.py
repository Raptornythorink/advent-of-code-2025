from typing import Iterator


def parse_input() -> Iterator[tuple[int]]:
    with open("input.txt", "r") as file:
        for line in file:
            yield tuple(map(int, line.strip()))


def find_max_output(bank: tuple[int], min_idx: int, max_idx: int) -> tuple[int, int]:
    n = len(bank)
    max_output, i_max_output = max(
        ((value, index) for index, value in enumerate(bank[min_idx:max_idx])),
        key=lambda e: n * e[0] + (n - e[1]),
    )
    return max_output, min_idx + i_max_output


def main1() -> int:
    banks = parse_input()
    total_output_joltage = 0

    for bank in banks:
        n = len(bank)

        max_output, i_max_output = find_max_output(bank, 0, n - 1)
        following_max_output, _ = find_max_output(bank, i_max_output + 1, n)

        output_joltage = 10 * max_output + following_max_output
        total_output_joltage += output_joltage

    return total_output_joltage


def main2() -> int:
    banks = parse_input()
    total_output_joltage = 0

    for bank in banks:
        n = len(bank)
        max_outputs = []
        start_idx = 0

        for k in range(12):
            max_output, i_max_output = find_max_output(bank, start_idx, n - 11 + k)
            max_outputs.append(max_output)
            start_idx = i_max_output + 1

        output_joltage = sum(
            (10 ** (11 - k)) * output for k, output in enumerate(max_outputs)
        )
        total_output_joltage += output_joltage

    return total_output_joltage


if __name__ == "__main__":
    print(main1())
    print(main2())
