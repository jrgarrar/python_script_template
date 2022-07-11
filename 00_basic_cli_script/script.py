"""
A template for creating Python scripts.

$ python script.py [--optional_argument OPTIONAL_ARGUMENT] required_argument

- jrgarrar
"""

# Library Imports
import pathlib
import argparse

# Globals
### A variable that points to this file's parent directory
PARENT_DIR = pathlib.Path(__file__).parent.absolute()

# Argument Parsing
def parse_args():
    """
    Parse input arguments and return them as a dict-like object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "required_argument",
        help="A description of this argument.",
    )
    parser.add_argument(
        "--optional_argument",
        help="A description of this argument.",
        default="some_default",
    )
    args = parser.parse_args()
    return args


# Main Function
def main(args):
    """
    The main function.
    """
    print("Hello, world!")
    print(f"Your input argument was {args.required_argument}.")


# If called from the command line, parse arguments and run main()
if __name__ == "__main__":
    args = parse_args()
    main(args)
