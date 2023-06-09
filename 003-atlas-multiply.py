import random


def generate_1_number_multiplication_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        problems.append((a, b))
        solutions.append(a * b)

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_1_number_multiplication_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} * {format(problems[i][1], ',')} = {format(solutions[i], ',')}")
    

def generate_2_number_multiplication_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        problems.append((a, b))
        solutions.append(a * b)

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_2_number_multiplication_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} * {format(problems[i][1], ',')} = {format(solutions[i], ',')}")
        

def generate_3_number_multiplication_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 999)
        b = random.randint(1, 999)
        problems.append((a, b))
        solutions.append(a * b)

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_3_number_multiplication_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} * {format(problems[i][1], ',')} = {format(solutions[i], ',')}")
        

def generate_4_number_multiplication_problems(n_problems):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(1, 9999)
        b = random.randint(1, 9999)
        problems.append((a, b))
        solutions.append(a * b)

    return problems, solutions

n_problems = 100  # Will generate this many problems
problems, solutions = generate_4_number_multiplication_problems(n_problems)

for i in range(n_problems):
    print(f"Problem {i+1}: {format(problems[i][0], ',')} * {format(problems[i][1], ',')} = {format(solutions[i], ',')}")
