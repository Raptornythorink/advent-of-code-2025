def parse_input() -> tuple[list[tuple[int, int]], list[int]]:
    fresh_ranges = []
    ingredients = []

    with open("input.txt", "r") as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            start, end = map(int, line.split("-"))
            fresh_ranges.append((start, end))
        while True:
            line = file.readline().strip()
            if not line:
                break
            ingredients.append(int(line))

    return fresh_ranges, ingredients


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged = []
    for start, end in sorted(ranges):
        if not merged or merged[-1][1] < start - 1:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    return merged


def is_fresh(fresh_ranges: list[tuple[int, int]], ingredient: int) -> bool:
    for start, end in fresh_ranges:
        if start <= ingredient <= end:
            return True
        if ingredient < start:
            break
    return False


def main1() -> int:
    fresh_ranges, ingredients = parse_input()
    merged_ranges = merge_ranges(fresh_ranges)
    fresh_count = sum(is_fresh(merged_ranges, ingredient) for ingredient in ingredients)
    return fresh_count


def main2() -> int:
    fresh_ranges, _ = parse_input()
    merged_ranges = merge_ranges(fresh_ranges)
    fresh_count = sum(end - start + 1 for start, end in merged_ranges)
    return fresh_count


if __name__ == "__main__":
    print(main1())
    print(main2())
