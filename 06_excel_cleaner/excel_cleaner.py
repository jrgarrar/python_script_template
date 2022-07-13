"""
A template for creating Python scripts.

$ python script.py [--optional_argument OPTIONAL_ARGUMENT] required_argument

- jrgarrar
"""

# Library Imports
import os
import datetime
import pathlib
import argparse
import pandas as pd

# Globals
### A variable that points to this file's parent directory
PARENT_DIR = pathlib.Path(__file__).parent.absolute()
INPUT_DIR = os.path.join(PARENT_DIR, "input")
INPUT_FILE = os.path.join(INPUT_DIR, "accounting.xlsx")
OUTPUT_DIR = os.path.join(PARENT_DIR, "output")
ACCOUNTING_OUTPUT_FILE = os.path.join(OUTPUT_DIR, "accounting.xlsx")
STAFFING_OUTPUT_FILE = os.path.join(OUTPUT_DIR, "staffing.xlsx")

# Argument Parsing
def parse_args():
    """
    Parse input arguments and return them as a dict-like object.
    """
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args


# Main Function
def main(args):
    """
    The main function.
    """
    # Load in both pages of Excel data
    accounting_data = pd.read_excel(INPUT_FILE, 0)
    staffing_data = pd.read_excel(INPUT_FILE, 1)

    # Print to the terminal
    print("Accounting Data:")
    print(accounting_data)
    print("")
    print("Staffing Data:")
    print(staffing_data)

    # Put each tab into its own Excel file
    accounting_data.to_excel(ACCOUNTING_OUTPUT_FILE, index=None)
    staffing_data.to_excel(STAFFING_OUTPUT_FILE, index=None)


# If called from the command line, parse arguments and run main()
if __name__ == "__main__":
    args = parse_args()
    main(args)
