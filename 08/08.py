from collections import Counter

MAX_CONNECTIONS_COUNT = 1000


def parse_input() -> list[tuple[int, int, int]]:
    junction_boxes = []

    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            x, y, z = map(int, line.split(","))
            junction_boxes.append((x, y, z))

    return junction_boxes


def squared_distance(box1: tuple[int, int, int], box2: tuple[int, int, int]) -> int:
    return sum((a - b) ** 2 for a, b in zip(box1, box2))


def find(circuits: list[int], x: int) -> int:
    while circuits[x] != x:
        circuits[x] = circuits[circuits[x]]
        x = circuits[x]
    return x


def union(circuits: list[int], x: int, y: int) -> None:
    circuits[find(circuits, x)] = find(circuits, y)


def main1() -> int:
    junction_boxes = parse_input()
    n = len(junction_boxes)

    squared_distances = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            dist = squared_distance(junction_boxes[i], junction_boxes[j])
            squared_distances[i][j] = dist

    shortest_connections = sorted(
        (squared_distances[i][j], i, j) for i in range(n) for j in range(i)
    )[:MAX_CONNECTIONS_COUNT]

    circuits = list(range(n))
    for _, i, j in shortest_connections:
        union(circuits, i, j)

    circuit_sizes = Counter(find(circuits, i) for i in range(n))
    sorted_sizes = sorted(circuit_sizes.values(), reverse=True)

    return sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]


def main2() -> int:
    junction_boxes = parse_input()
    n = len(junction_boxes)

    squared_distances = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            dist = squared_distance(junction_boxes[i], junction_boxes[j])
            squared_distances[i][j] = dist

    sorted_connections = sorted(
        (squared_distances[i][j], i, j) for i in range(n) for j in range(i)
    )

    circuits = list(range(n))
    for _, i, j in sorted_connections:
        union(circuits, i, j)
        if len(set(find(circuits, k) for k in range(n))) == 1:
            break

    return junction_boxes[i][0] * junction_boxes[j][0]


if __name__ == "__main__":
    print(main1())
    print(main2())
