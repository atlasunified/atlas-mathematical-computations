import random
import json

instructions = [
    "Can you figure out the result of raising",
    "What is the result when you raise",
    "Please compute the value of",
    "Raise",
    "Could you please raise",
    "What is the result of",
    "Calculate the value of this expression:",
    "Solve for the value of",
    "Compute the result of this expression:",
    "What's the result of",
    "Can you solve this equation:",
    "I need the result of",
    "What do you get when you raise",
    "Tell me the solution to this equation:",
    "Can you determine the result of raising"
]

def generate_math_problems(n_problems, min_num, max_num, max_exponent):
    problems = []
    solutions = []

    for _ in range(n_problems):
        a = random.randint(min_num, max_num)
        b = random.randint(1, max_exponent)
        instruction = random.choice(instructions)
        problems.append((a, b, instruction))
        solutions.append(a ** b)

    return problems, solutions

levels = [(1, 9, 9), (1, 99, 5), (1, 999, 4)]  # Adjust the levels and max_exponents as needed

n_problems = 350000  # Will generate this many problems for each level

# Open the file outside the loop, so all problems are written to the same file
with open('exponent_math_problems.jsonl', 'w') as f:
    for i, level in enumerate(levels):
        problems, solutions = generate_math_problems(n_problems, level[0], level[1], level[2])
        for j in range(n_problems):
            problem_dict = {
                "answer": f"{solutions[j]}",
                "input": f"{problems[j][0]}^{problems[j][1]}",
                "output": f"{problems[j][0]}^{problems[j][1]} = {solutions[j]}",
                "instruction": f"{problems[j][2]} {problems[j][0]}^{problems[j][1]}"
            }
            f.write(json.dumps(problem_dict) + '\n')
