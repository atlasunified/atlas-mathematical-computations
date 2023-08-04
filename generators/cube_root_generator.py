import random
import json

instructions = [
    "Can you figure out the cube root of",
    "What is the cube root of",
    "Please compute the cube root of",
    "Find the cube root of",
    "Could you please find the cube root of",
    "What is the cube root of",
    "Calculate the cube root of",
    "Solve for the cube root of",
    "Determine the cube root of",
    "What's the cube root of",
    "Can you solve for the cube root of",
    "I need the cube root of",
    "What do you get when you take the cube root of",
    "Tell me the cube root of",
    "Can you determine the cube root of"
]

def generate_math_problems(n_problems, min_num, max_num):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(min_num, max_num)
        instruction = random.choice(instructions)
        problems.append((a, instruction))
        solutions.append(round(a ** (1. / 3.), 2))  # Cube root calculation

    return problems, solutions

levels = [(1, 9), (1, 99), (1, 999), (1, 9999), (1, 99999), (1, 999999), (1, 9999999), (1, 99999999)]

n_problems = 300000  # Will generate this many problems for each level

problem_id = 1
all_problems = []
for i, level in enumerate(levels):
    problems, solutions = generate_math_problems(n_problems, level[0], level[1])
    for j in range(n_problems):
        problem_dict = {
            "answer": f"{solutions[j]}",
            "input": f"{problems[j][0]}^(1/3)",
            "output": f"cube root of {problems[j][0]} = {solutions[j]}",
            "instruction": f"{problems[j][1]} {problems[j][0]}"
        }
        all_problems.append(problem_dict)
        problem_id += 1

with open('cube_root_math_problems_all_levels.jsonl', 'w') as f:
    for problem in all_problems:
        f.write(json.dumps(problem) + '\n')
