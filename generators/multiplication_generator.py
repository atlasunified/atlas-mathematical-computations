import random
import json

instructions = [
    "Can you figure out the result of multiplying",
    "What is the result when you multiply",
    "Please compute the product of",
    "Multiply",
    "Could you please multiply",
    "What is the product of",
    "Calculate the product of these two values:",
    "Solve for the product of",
    "Multiply these numbers:",
    "What's the product of",
    "Can you solve this equation:",
    "I need the product of",
    "What do you get when you multiply",
    "Tell me the solution to this equation:",
    "Can you determine the result of multiplying"
]

def generate_math_problems(n_problems, min_num, max_num):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(min_num, max_num)
        b = random.randint(min_num, max_num)
        instruction = random.choice(instructions)
        problems.append((a, b, instruction))
        solutions.append(a * b)

    return problems, solutions

levels = [(1, 9), (1, 99), (1, 999), (1, 9999), (1, 99999), (1, 999999), (1, 9999999), (1, 99999999)]

n_problems = 300000 # Will generate this many problems for each level

for level in levels:
    problems, solutions = generate_math_problems(n_problems, level[0], level[1])

    with open('multiplication_math_problems.jsonl', 'a') as f:
        for i in range(n_problems):
            problem_dict = {
                "answer": str(solutions[i]),
                "input": f"{problems[i][0]} * {problems[i][1]}",
                "output": f"{problems[i][0]} x {problems[i][1]} = {solutions[i]}",
                "instruction": f"{problems[i][2]} {problems[i][0]} * {problems[i][1]}"
            }
            f.write(json.dumps(problem_dict) + '\n')
