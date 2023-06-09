import random


####### 2 Decimal Addition


def generate_2_decimal_2_digit_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 99), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 99), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a + b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_2_digit_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} + {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_3_digit_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a + b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_3_digit_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} + {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_4_digit_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 9999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 9999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a + b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_4_digit_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} + {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_5_digit_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 99999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 99999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a + b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_5_digit_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} + {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


####### 2 Decimal Subtraction


def generate_2_decimal_2_digit_subtraction_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 99), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 99), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a - b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_2_digit_subtraction_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} - {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_3_digit_subtraction_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a - b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_3_digit_subtraction_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} - {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_4_digit_subtraction_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 9999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 9999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a - b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_4_digit_subtraction_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} - {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_5_digit_subtraction_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 99999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 99999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a - b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_5_digit_subtraction_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} - {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


####### 2 Decimal Multiplication


def generate_2_decimal_2_digit_multiplication_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 99), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 99), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a * b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_2_digit_multiplication_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} * {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_3_digit_multiplication_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a * b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_3_digit_multiplication_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} * {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_4_digit_multiplication_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 9999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 9999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a * b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_4_digit_multiplication_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} * {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


####### 2 Decimal Division


def generate_2_decimal_2_digit_division_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 99), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 99), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a / b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_2_digit_division_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} / {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_3_digit_division_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a / b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_3_digit_division_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} / {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_4_digit_division_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 9999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 9999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a / b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_4_digit_division_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} / {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")


def generate_2_decimal_5_digit_division_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = round(random.uniform(1, 99999), 2)  # Decimal number with two decimal places
        b = round(random.uniform(1, 99999), 2)  # Decimal number with two decimal places
        problems.append((a, b))
        solutions.append(round(a / b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_decimal_5_digit_division_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], '.2f')} / {format(problems[i][1], '.2f')} = {format(solutions[i], '.2f')}")
