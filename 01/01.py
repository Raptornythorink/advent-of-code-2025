from typing import Iterator


def parse_input() -> Iterator[int]:
    with open("input.txt", "r") as file:
        for line in file:
            rotation = line.strip()
            if rotation:
                direction = 1 if rotation[0] == "R" else -1
                distance = int(rotation[1:])
                yield (direction * distance)


def main1() -> int:
    rotations = parse_input()
    dial = 50
    zero_count = 0
    for rotation in rotations:
        dial = (dial + rotation) % 100
        if dial == 0:
            zero_count += 1
    return zero_count


def main2() -> int:
    rotations = parse_input()
    dial = 50
    zero_count = 0
    for rotation in rotations:
        remainder = abs(rotation) % 100
        zero_count += abs(rotation) // 100 + (
            dial != 0 and remainder >= (100 - dial if rotation > 0 else dial)
        )
        dial = (dial + rotation) % 100
    return zero_count


if __name__ == "__main__":
    print(main1())
    print(main2())
