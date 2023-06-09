import random

def generate_1_number_division_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        problems.append((a, b))
        if b == 0:
            solutions.append('undefined')
        else:
            solutions.append(round(a / b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_1_number_division_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} / {format(problems[i][1], ',')} = {solutions[i]}")


def generate_2_number_division_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(0, 99)
        b = random.randint(0, 99)
        problems.append((a, b))
        solutions.append(round(a / b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_number_division_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} / {format(problems[i][1], ',')} = {solutions[i]}")


def generate_3_number_division_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(0, 999)
        b = random.randint(0, 999)
        problems.append((a, b))
        solutions.append(round(a / b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_3_number_division_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} / {format(problems[i][1], ',')} = {solutions[i]}")


def generate_4_number_division_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(0, 9999)
        b = random.randint(0, 9999)
        problems.append((a, b))
        solutions.append(round(a / b, 2))  # Round to two decimal places

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_4_number_division_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} / {format(problems[i][1], ',')} = {solutions[i]}")

