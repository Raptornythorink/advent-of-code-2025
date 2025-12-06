def parse_input() -> tuple[list[str], list[str]]:
    all_operands = []
    operators = []
    with open("input.txt", "r") as file:
        for line in file:
            if line[0] == "+" or line[0] == "*":
                n = len(line)
                i = 0
                curr_operator = ""
                while i < n:
                    if line[i] == "+" or line[i] == "*":
                        if curr_operator:
                            operators.append(curr_operator[:-1])
                        curr_operator = line[i]
                    else:
                        curr_operator += line[i]
                    i += 1
                if curr_operator:
                    operators.append(curr_operator)
            else:
                all_operands.append(line[:-1])
    return all_operands, operators


def apply_operation(operands: list[int], operator: str) -> int:
    if operator[0] == "+":
        result = sum(operands)
    elif operator[0] == "*":
        result = 1
        for operand in operands:
            result *= operand
    else:
        raise ValueError(f"Unknown operator: {operator}")
    return result


def main1() -> int:
    all_operands, operators = parse_input()

    transposed_int_operands = list(
        map(
            list,
            zip(
                *(
                    [int(operand) for operand in operands.split()]
                    for operands in all_operands
                )
            ),
        )
    )

    total = 0

    for i, operator in enumerate(operators):
        total += apply_operation(transposed_int_operands[i], operator)

    return total


def main2() -> int:
    all_operands, operators = parse_input()

    col_index = 0
    total = 0

    for operator in operators:
        operator_length = len(operator)

        transposed_int_operands = list(
            map(
                lambda t: int("".join(t)),
                zip(
                    *(
                        operands_str[col_index : col_index + operator_length]
                        for operands_str in all_operands
                    )
                ),
            )
        )

        total += apply_operation(transposed_int_operands, operator)

        col_index += operator_length + 1
    return total


if __name__ == "__main__":
    print(main1())
    print(main2())
