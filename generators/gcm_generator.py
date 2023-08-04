import random
import json
import math

instructions = [
    "Can you find the greatest common divisor of",
    "What is the greatest common divisor of",
    "Please compute the greatest common divisor of",
    "Find the greatest common divisor of",
    "Could you please find the greatest common divisor of",
    "What is the greatest common divisor of",
    "Calculate the greatest common divisor of",
    "What's the greatest common divisor of",
    "Can you solve for the greatest common divisor of",
    "I need the greatest common divisor of",
    "What do you get when you find the greatest common divisor of",
    "Tell me the greatest common divisor of",
    "Can you determine the greatest common divisor of"
]

def generate_math_problems(n_problems, min_num, max_num):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a, b = random.randint(min_num, max_num), random.randint(min_num, max_num)
        instruction = random.choice(instructions)
        problems.append(((a, b), instruction))
        gcd = math.gcd(a, b)
        solutions.append(gcd)

    return problems, solutions

levels = [(1, 9), (1, 99), (1, 999), (1, 9999)]

n_problems = 250000  # Will generate this many problems for each level

problem_id = 1
all_problems = []
for i, level in enumerate(levels):
    problems, solutions = generate_math_problems(n_problems, level[0], level[1])
    for j in range(n_problems):
        problem_dict = {
            "answer": f"{solutions[j]}",
            "input": f"Greatest common divisor of {problems[j][0][0]} and {problems[j][0][1]}",
            "output": f"Greatest common divisor of {problems[j][0][0]} and {problems[j][0][1]} is {solutions[j]}",
            "instruction": f"{problems[j][1]} {problems[j][0][0]} and {problems[j][0][1]}"
        }
        all_problems.append(problem_dict)
        problem_id += 1

with open('gcd_math_problems_all_levels.jsonl', 'w') as f:
    for problem in all_problems:
        f.write(json.dumps(problem) + '\n')
