"""
A template for creating Python scripts.

$ python script.py [--optional_argument OPTIONAL_ARGUMENT] required_argument

- jrgarrar
"""

# Library Imports
import requests
import pathlib
import argparse
from bs4 import BeautifulSoup

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
        "--pretty",
        help="When set, the program will format output for easier reading.",
        action="store_true",
    )
    args = parser.parse_args()
    return args


# Main Function
def main(args):
    """
    The main function.
    """
    # Ping Google
    data = requests.get("http://www.google.com")

    # Print the response
    print(f"{data}")
    print("---")
    if args.pretty:
        soup = BeautifulSoup(data.content, "html.parser")
        print(f"{ soup.prettify() }")
    else:
        print(f"{data.content}")


# If called from the command line, parse arguments and run main()
if __name__ == "__main__":
    args = parse_args()
    main(args)
