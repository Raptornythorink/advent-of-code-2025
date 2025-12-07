from collections import defaultdict


def parse_input() -> tuple[int, tuple[int, int], set[tuple[int, int]]]:
    height = 0
    start = (0, 0)
    splitters = set()

    with open("input.txt", "r") as file:
        for y, line in enumerate(file):
            line = line.strip()
            for x, char in enumerate(line):
                if char == "S":
                    start = (x, y)
                elif char == "^":
                    splitters.add((x, y))
            height += 1

    return height, start, splitters


def main1() -> int:
    height, start, splitters = parse_input()

    curr_y = 0
    split_count = 0
    beams_x = {start[0]}

    while curr_y < height:
        next_beams_x = set()

        for beam_x in beams_x:
            if (beam_x, curr_y) in splitters:
                next_beams_x.add(beam_x - 1)
                next_beams_x.add(beam_x + 1)
                split_count += 1
            else:
                next_beams_x.add(beam_x)

        beams_x = next_beams_x
        curr_y += 1

    return split_count


def main2() -> int:
    height, start, splitters = parse_input()

    curr_y = 0
    beams_x = {start[0]: 1}

    while curr_y < height:
        next_beams_x = defaultdict(int)

        for beam_x in beams_x:
            if (beam_x, curr_y) in splitters:
                next_beams_x[beam_x - 1] += beams_x[beam_x]
                next_beams_x[beam_x + 1] += beams_x[beam_x]
            else:
                next_beams_x[beam_x] += beams_x[beam_x]

        beams_x = next_beams_x
        curr_y += 1

    timelines = sum(beams_x.values())
    return timelines


if __name__ == "__main__":
    print(main1())
    print(main2())
