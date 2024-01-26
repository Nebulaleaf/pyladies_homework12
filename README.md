Homework12 CLI Program
Description

This Python CLI (Command Line Interface) program processes text files based on user-defined operations. It supports various text manipulation operations such as converting text to uppercase and inserting random animal names after every third word in the text.
Features

    Convert Text to Uppercase: Transforms all the text in the input file to uppercase letters.
    Insert Random Animals: Adds a random animal name from a predefined list after every third word in the text.

Usage

To use this program, you will need Python installed on your system. You can run the program from the command line by navigating to the directory containing the script and executing it with the required arguments.
Arguments

    input_file: The path to the input file containing the text to be processed.
    output_file: The path where the processed text will be saved.
    --operation: Specifies the operation to perform on the text. Choose between uppercase and random_animal.
    --add_summary: (Optional) Adds a summary at the end of the output file.

Examples

Convert text in input.txt to uppercase and save the result to output.txt:

lua

python homework12_CLI.py input.txt output.txt --operation uppercase

Insert random animal names in input.txt after every third word and save the result to output.txt:

lua

python homework12_CLI.py input.txt output.txt --operation random_animal

Insert random animal names and add a summary to output.txt:

css

python homework12_CLI.py input.txt output.txt --operation random_animal --add_summary

Requirements

    Python 3.x

Installation

No additional installation is required. Just ensure you have Python 3.x installed on your system.