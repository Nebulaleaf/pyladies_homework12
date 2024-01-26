import argparse
import random

parser = argparse.ArgumentParser(description='Textfile changes.')

# Adding arguments
parser.add_argument('input_file', type=str, help='Path to the input file')
parser.add_argument('output_file', type=str, help='Path to the output file')

# Optional arguments
parser.add_argument('--operation', type=str, choices=['uppercase', 'random_animal'], help='Choose the operation to perform')

# Boolean flag
parser.add_argument('--add_summary', action='store_true', help='Add a summary at the end of the output file')

args = parser.parse_args()

# List of animals
animals = ['dog', 'cat', 'bird', 'elephant', 'giraffe', 'lion', 'tiger', 'bear', 'fox', 'wolf']

# Function to insert random animals into text every third word
def insert_random_animals(text):
    words = text.split()
    new_text = []
    for i, word in enumerate(words):
        new_text.append(word)
        if (i + 1) % 3 == 0:  # After every third word
            new_text.append(random.choice(animals))  # Insert a random animal
    return ' '.join(new_text)

# Operation to convert text to uppercase
if args.operation == 'uppercase':
    with open(args.input_file, 'r') as file:
        content = file.read()
    content = content.upper()  # Convert text to uppercase
    with open(args.output_file, 'w') as file:
        file.write(content)

# Operation to insert random animals into the text
if args.operation == 'random_animal':
    with open(args.input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    modified_content = insert_random_animals(content)
    with open(args.output_file, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# Add summary if the flag is set
if args.add_summary:
    with open(args.output_file, 'a', encoding='utf-8') as file:
        file.write("\n\nSummary: This document was processed by the homework12_CLI.py script.")
