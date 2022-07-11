"""
A template for creating Python scripts.

$ python script.py [--optional_argument OPTIONAL_ARGUMENT] required_argument

- jrgarrar
"""

# Library Imports
import os
import pathlib
import argparse
import pandas as pd
from matplotlib import pyplot as plt

# Globals
PARENT_DIR = pathlib.Path(__file__).parent.absolute()
INPUT_DIR = os.path.join(PARENT_DIR, "input")
INPUT_FILE = os.path.join(INPUT_DIR, "iris.data")
OUTPUT_DIR = os.path.join(PARENT_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "iris.png")
plt.style.use("ggplot")

# Argument Parsing
def parse_args():
    """
    Parse input arguments and return them as a dict-like object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--color",
        help="The color of the plot points (i.e. blue, red, black).",
        default="blue"
    )
    args = parser.parse_args()
    return args


# Main Function
def main(args):
    """
    The main function.
    """
    # Load data
    input_file_path = os.path.join(INPUT_DIR, INPUT_FILE)
    input_data = pd.read_csv(input_file_path, header=None)
    print(f"Input file found at {input_file_path}")

    # Create a scatterplot of the first column vs. the second
    plt.scatter(input_data[0], input_data[1], color=args.color)
    plt.title("Sepal Length vs. Sepal Width")
    plt.xlabel("Length (cm)")
    plt.ylabel("Width (cm)")

    # Save the plot to file
    output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    plt.savefig(output_file_path)
    print(f"Output file placed at {output_file_path}")


# If called from the command line, parse arguments and run main()
if __name__ == "__main__":
    args = parse_args()
    main(args)
