import random
import json
import math

instructions = [
    "Can you figure out the square root of",
    "What is the square root of",
    "Please compute the square root of",
    "Find the square root of",
    "Could you please find the square root of",
    "What is the root of",
    "Calculate the square root of",
    "Solve for the root of",
    "Determine the square root of",
    "What's the square root of",
    "Can you solve for the square root of",
    "I need the square root of",
    "What do you get when you take the square root of",
    "Tell me the square root of",
    "Can you determine the square root of"
]

def generate_math_problems(n_problems, min_num, max_num):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(min_num, max_num)
        instruction = random.choice(instructions)
        problems.append((a, instruction))
        solutions.append(math.sqrt(a))

    return problems, solutions

levels = [(1, 9), (1, 99), (1, 999), (1, 9999), (1, 99999), (1, 999999), (1, 9999999), (1, 99999999)]

n_problems = 300000  # Will generate this many problems for each level

problem_id = 1
all_problems = []
for i, level in enumerate(levels):
    problems, solutions = generate_math_problems(n_problems, level[0], level[1])
    for j in range(n_problems):
        equation = f"{problems[j][0]}^(1/2) = {solutions[j]}"  # the equation plus the answer
        problem_dict = {
            "answer": str(solutions[j]),
            "input": f"{problems[j][0]}^(1/2)",
            "output": equation,  # update here to include equation in the output
            "instruction": f"{problems[j][1]} {problems[j][0]}"
        }
        all_problems.append(problem_dict)
        problem_id += 1

with open('square_root_math_problems_all_levels.jsonl', 'w') as f:
    for problem in all_problems:
        f.write(json.dumps(problem) + '\n')
