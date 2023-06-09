import random


def generate_1_number_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        problems.append((a, b))
        solutions.append(a + b)

    return problems, solutions

n_problems = 100  # Set the number of problems here
problems, solutions = generate_1_number_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {problems[i][0]} + {problems[i][1]} = {solutions[i]}")


def generate_2_number_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        problems.append((a, b))
        solutions.append(a + b)

    return problems, solutions

n_problems = 100 # Will generate this many problems
problems, solutions = generate_2_number_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} + {format(problems[i][1], ',')} = {format(solutions[i], ',')}")


def generate_3_number_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 999)
        b = random.randint(1, 999)
        problems.append((a, b))
        solutions.append(a + b)

    return problems, solutions

n_problems = 100 # Will generate this many problems
problems, solutions = generate_3_number_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} + {format(problems[i][1], ',')} = {format(solutions[i], ',')}")


def generate_4_number_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 9999)
        b = random.randint(1, 9999)
        problems.append((a, b))
        solutions.append(a + b)

    return problems, solutions

n_problems = 100 # Will generate this many problems
problems, solutions = generate_4_number_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} + {format(problems[i][1], ',')} = {format(solutions[i], ',')}")


def generate_5_number_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 99999)
        b = random.randint(1, 99999)
        problems.append((a, b))
        solutions.append(a + b)

    return problems, solutions

n_problems = 100 # Will generate this many problems
problems, solutions = generate_5_number_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} + {format(problems[i][1], ',')} = {format(solutions[i], ',')}")


def generate_6_number_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 999999)
        b = random.randint(1, 999999)
        problems.append((a, b))
        solutions.append(a + b)

    return problems, solutions

n_problems = 100 # Will generate this many problems
problems, solutions = generate_6_number_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} + {format(problems[i][1], ',')} = {format(solutions[i], ',')}")


def generate_7_number_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 9999999)
        b = random.randint(1, 9999999)
        problems.append((a, b))
        solutions.append(a + b)

    return problems, solutions

n_problems = 100 # Will generate this many problems
problems, solutions = generate_7_number_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} + {format(problems[i][1], ',')} = {format(solutions[i], ',')}")


def generate_8_number_addition_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 99999999)
        b = random.randint(1, 99999999)
        problems.append((a, b))
        solutions.append(a + b)

    return problems, solutions

n_problems = 100 # Will generate this many problems
problems, solutions = generate_8_number_addition_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} + {format(problems[i][1], ',')} = {format(solutions[i], ',')}")

