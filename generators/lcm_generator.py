import random
import json
import math

instructions = [
    "Can you find the least common multiple of",
    "What is the least common multiple of",
    "Please compute the least common multiple of",
    "Find the least common multiple of",
    "Could you please find the least common multiple of",
    "What is the least common multiple of",
    "Calculate the least common multiple of",
    "What's the least common multiple of",
    "Can you solve for the least common multiple of",
    "I need the least common multiple of",
    "What do you get when you find the least common multiple of",
    "Tell me the least common multiple of",
    "Can you determine the least common multiple of"
]

def generate_math_problems(n_problems, min_num, max_num):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a, b = random.randint(min_num, max_num), random.randint(min_num, max_num)
        instruction = random.choice(instructions)
        problems.append(((a, b), instruction))
        lcm = a * b // math.gcd(a, b)
        solutions.append(lcm)

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
            "input": f"Least common multiple of {problems[j][0][0]} and {problems[j][0][1]}",
            "output": f"Least common multiple of {problems[j][0][0]} and {problems[j][0][1]} is {solutions[j]}",
            "instruction": f"{problems[j][1]} {problems[j][0][0]} and {problems[j][0][1]}"
        }
        all_problems.append(problem_dict)
        problem_id += 1

with open('lcm_math_problems_all_levels.jsonl', 'w') as f:
    for problem in all_problems:
        f.write(json.dumps(problem) + '\n')
