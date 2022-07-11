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
from jinja2 import Template
from datetime import datetime

# Globals
### A variable that points to this file's parent directory
PARENT_DIR = pathlib.Path(__file__).parent.absolute()
INPUT_DIR = os.path.join(PARENT_DIR, "input")
TEMPLATE_FILE = os.path.join(INPUT_DIR, "template.sql")
OUTPUT_DIR = os.path.join(PARENT_DIR, "output")

# Argument Parsing
def parse_args():
    """
    Parse input arguments and return them as a dict-like object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "author",
        help="The author's name.",
    )
    parser.add_argument(
        "ticket_number",
        help="The ticket number.",
    )
    args = parser.parse_args()
    return args


# Main Function
def main(args):
    """
    The main function.
    """
    # Generate file from template
    with open(TEMPLATE_FILE, "r") as f:
        # Read data in as a list of strings
        template_list = f.readlines()
        # Convert the list into a single string
        template_str = "".join(template_list)
        # Create a Template object from the strings
        template = Template(template_str)

        # Fill in values surrounded by curly brackets (i.e. {{ author }})
        template_filled = template.render(
            author=args.author,
            date=datetime.now().strftime("%Y/%m/%d"),
            pt=args.ticket_number,
        )

    # Write the finished file
    output_filename = f"pt_{args.ticket_number}.sql"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    with open(output_path, "w") as f:
        f.writelines(template_filled)

    print(f"---{output_filename} Created---")
    print(f"{output_path}")


# If called from the command line, parse arguments and run main()
if __name__ == "__main__":
    args = parse_args()
    main(args)
