import random
import json
from fractions import Fraction

# List of operations
OPERATIONS = {
    'addition': lambda a, b: a + b,
    'subtraction': lambda a, b: a - b,
    'multiplication': lambda a, b: a * b,
    'division': lambda a, b: a / b if b != 0 else 'undefined'
}

# Dict for operator symbols
OPERATORS = {
    'addition': '+',
    'subtraction': '-',
    'multiplication': '*',
    'division': '/'
}

# Instruction templates
INSTRUCTIONS = {
    'addition': [
        "Can you figure out the sum of",
        "What is the result when you add",
        "Please compute the total of",
        "Sum up",
        "Could you please add",
        "What is the addition of",
        "Calculate these two values:",
        "Solve for the sum of",
        "Add these numbers:",
        "What's the sum of",
        "Can you solve this equation:",
        "I need the sum of",
        "What do you get when you add",
        "Tell me the solution to this equation:",
        "Can you determine the result of"
    ],
    'subtraction': [
        "Can you figure out the result of subtracting",
        "What is the result when you subtract",
        "Please compute the difference of",
        "Subtract",
        "Could you please subtract",
        "What is the subtraction of",
        "Calculate the difference between these two values:",
        "Solve for the difference of",
        "Subtract these numbers:",
        "What's the difference of",
        "Can you solve this equation:",
        "I need the difference of",
        "What do you get when you subtract",
        "Tell me the solution to this equation:",
        "Can you determine the result of subtracting"
    ],
    'multiplication': [
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
    ],
    'division': [
        "Can you figure out the result of dividing",
        "What is the result when you divide",
        "Please compute the quotient of",
        "Divide",
        "Could you please divide",
        "What is the quotient of",
        "Calculate the quotient of these two values:",
        "Solve for the quotient of",
        "Divide these numbers:",
        "What's the quotient of",
        "Can you solve this equation:",
        "I need the quotient of",
        "What do you get when you divide",
        "Tell me the solution to this equation:",
        "Can you determine the result of dividing"
    ]
}

def generate_fraction_problems(n_problems, n_digits, operation):
    problems = []
    solutions = []
    instructions = []
    max_value = 10**n_digits - 1

    for _ in range(n_problems):
        a = Fraction(random.randint(1, max_value), random.randint(1, max_value))
        b = Fraction(random.randint(1, max_value), random.randint(1, max_value))
        instruction = random.choice(INSTRUCTIONS[operation])
        problems.append((a, b, instruction))
        solutions.append(OPERATIONS[operation](a, b))

    return problems, solutions

n_problems = 300000

with open('fraction_math_problems.jsonl', 'w') as f:
    for operation in OPERATIONS:
        for n_digits in range(2, 6):  # From 2-digit to 5-digit
            problems, solutions = generate_fraction_problems(n_problems, n_digits, operation)
            for i in range(n_problems):
                problem_equation = f"{str(problems[i][0])} {OPERATORS[operation]} {str(problems[i][1])}"
                problem_dict = {
                    "answer": str(solutions[i]),
                    "input": problem_equation,
                    "output": f"{problem_equation} = {str(solutions[i])}",
                    "instruction": f"{problems[i][2]} {problem_equation}"
                }
                f.write(json.dumps(problem_dict) + '\n')
