ADJACENT_POS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def parse_input() -> set[tuple[int, int]]:
    rolls = set()
    with open("input.txt", "r") as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                if char == "@":
                    rolls.add((j, i))
    return rolls


def is_accessible_roll(rolls: set[tuple[int, int]], x: int, y: int) -> bool:
    adjacent_rolls = 0
    for dx, dy in ADJACENT_POS:
        nx, ny = x + dx, y + dy
        if (nx, ny) in rolls:
            adjacent_rolls += 1
            if adjacent_rolls >= 4:
                return False
    return True


def main1() -> int:
    rolls = parse_input()
    accessible_rolls_count = 0

    for j, i in rolls:
        accessible_rolls_count += is_accessible_roll(rolls, j, i)

    return accessible_rolls_count


def main2() -> int:
    rolls = parse_input()
    total_accessible_rolls_count = 0

    while True:
        accessible_rolls = []

        for j, i in rolls:
            if is_accessible_roll(rolls, j, i):
                accessible_rolls.append((j, i))
                total_accessible_rolls_count += 1

        if not accessible_rolls:
            break

        for j, i in accessible_rolls:
            rolls.remove((j, i))

    return total_accessible_rolls_count


if __name__ == "__main__":
    print(main1())
    print(main2())
