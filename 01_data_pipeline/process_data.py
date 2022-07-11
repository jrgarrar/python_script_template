"""
A simple data pipeline template.

$ python process_data.py target_filename

- jrgarrar
"""

# Library Imports
import os
import pathlib
import argparse
import numpy as np
import pandas as pd

# Globals
### A variable that points to this file's parent directory
PARENT_DIR = pathlib.Path(__file__).parent.absolute()
INPUT_DIR = os.path.join(PARENT_DIR, "input")
OUTPUT_DIR = os.path.join(PARENT_DIR, "output")

# Argument Parsing
def parse_args():
    """
    Parse input arguments and return them as a dict-like object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "target_filename",
        help="The name of a file in the input/ directory.",
    )
    args = parser.parse_args()
    return args


# Main Function
def main(args):
    """
    The main function.
    """
    # Load in the data
    input_file_path = os.path.join(INPUT_DIR, args.target_filename)
    input_data = pd.read_csv(input_file_path, header=None)
    print(f"Input file found at {input_file_path}")

    # Transform the data (add a new column)
    output_data = input_data.copy(deep=True)
    output_data["new_col"] = 1

    # Output to file
    output_file_path = os.path.join(OUTPUT_DIR, args.target_filename)
    output_data.to_csv(output_file_path, header=None)
    print(f"Output file placed at {output_file_path}")


# If called from the command line, parse arguments and run main()
if __name__ == "__main__":
    args = parse_args()
    main(args)
