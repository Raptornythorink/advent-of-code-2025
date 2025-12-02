from typing import Iterator


def parse_input() -> Iterator[tuple[int, int]]:
    with open("input.txt", "r") as file:
        for id_range in file.readline().split(","):
            start, end = map(int, id_range.split("-"))
            yield (start, end)


def is_invalid_id1(id_str: str) -> bool:
    n = len(id_str)
    return n % 2 == 0 and id_str[: n // 2] == id_str[n // 2 :]


def is_invalid_id2(id_str: str) -> bool:
    n = len(id_str)
    for cycle_length in range(1, n // 2 + 1):
        if n % cycle_length == 0:
            if all(
                id_str[i] == id_str[i + cycle_length] for i in range(n - cycle_length)
            ):
                return True
    return False


def main1() -> int:
    id_ranges = parse_input()
    invalid_ids_count = 0
    for start, end in id_ranges:
        for id_num in range(start, end + 1):
            invalid_ids_count += is_invalid_id1(str(id_num)) * id_num
    return invalid_ids_count


def main2() -> int:
    id_ranges = parse_input()
    invalid_ids_count = 0
    for start, end in id_ranges:
        for id_num in range(start, end + 1):
            invalid_ids_count += is_invalid_id2(str(id_num)) * id_num
    return invalid_ids_count


if __name__ == "__main__":
    print(main1())
    print(main2())
