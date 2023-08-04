import random
import json

instructions = [
    "Can you list all the factors of",
    "What are the factors of",
    "Please compute the factors of",
    "Provide all factors of",
    "Could you please list the factors of",
    "What is the set of factors of",
    "Calculate the factors of this number:",
    "List all the factors of",
    "Provide factors of this number:",
    "What's the set of factors of",
    "Can you solve for the factors of:",
    "I need the factors of",
    "What do you get when you find the factors of",
    "Tell me the factors of this number:",
    "Can you determine the factors of"
]

def generate_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def generate_math_problems(n_problems, min_num, max_num):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(min_num, max_num)
        instruction = random.choice(instructions)
        problems.append((a, instruction))
        solutions.append(generate_factors(a))

    return problems, solutions

levels = [(1, 9), (1, 99), (1, 999), (1, 9999)]

n_problems = 100000  # Will generate this many problems for each level

problem_id = 1
all_problems = []
for i, level in enumerate(levels):
    problems, solutions = generate_math_problems(n_problems, level[0], level[1])
    for j in range(n_problems):
        problem_dict = {
            "answer": f"{solutions[j]}",
            "input": f"Factors of {problems[j][0]}",
            "output": f"Factors of {problems[j][0]} are {solutions[j]}",
            "instruction": f"{problems[j][1]} {problems[j][0]}"
        }
        all_problems.append(problem_dict)
        problem_id += 1

with open('factors_math_problems_all_levels.jsonl', 'w') as f:
    for problem in all_problems:
        f.write(json.dumps(problem) + '\n')
