import os
import subprocess
import glob
import json
import random

# List of python scripts to be executed
scripts = [
    'addition_generator.py',
    'decimal_generator.py',
    'division_generator.py',
    'exponent_generator.py',
    'fraction_generator.py',
    'multiplication_generator.py',
    'subtraction_generator.py',
    'square_root_generator.py',
    'cube_root_generator.py',
    'factor_generator.py',
    'lcm_generator.py',
    'gcm_generator.py'
]

# Prompt the user for the number of times to run each script
n_runs = int(input("How many times do you want to run each generator? "))

# For each script
for script in scripts:
    # Run the script the specified number of times
    for i in range(n_runs):
        print(f"Running {script}, iteration {i+1} of {n_runs}")
        subprocess.run(["python", os.path.join("generators", script)])

print("All scripts have finished running.")

# Combine JSONL files
output_files = glob.glob('*.jsonl')
combined_data = []

for file_name in output_files:
    with open(file_name, 'r') as file:
        for line in file:
            data = json.loads(line)
            combined_data.append(data)

# Shuffle combined data
random.shuffle(combined_data)

# Deduplicate
print(f"Number of problems before deduplication: {len(combined_data)}")
combined_data = list({instruction['instruction']: instruction for instruction in combined_data}.values())
print(f"Number of problems after deduplication: {len(combined_data)}")

# Split data into training, validation, and test sets
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

train_data = combined_data[:int(len(combined_data) * train_ratio)]
val_data = combined_data[int(len(combined_data) * train_ratio):int(len(combined_data) * (train_ratio + val_ratio))]
test_data = combined_data[int(len(combined_data) * (train_ratio + val_ratio)):]

# Write each dataset to a new JSONL file
with open('atlas-math-train.jsonl', 'w') as file:
    for data in train_data:
        file.write(json.dumps(data) + '\n')

with open('atlas-math-val.jsonl', 'w') as file:
    for data in val_data:
        file.write(json.dumps(data) + '\n')

with open('atlas-math-test.jsonl', 'w') as file:
    for data in test_data:
        file.write(json.dumps(data) + '\n')

# Delete individual output files
for file_name in output_files:
    os.remove(file_name)

print("All outputs have been combined, shuffled, deduplicated, and split into 'atlas-math-train.jsonl', 'atlas-math-val.jsonl', and 'atlas-math-test.jsonl'. Individual output files have been deleted.")
