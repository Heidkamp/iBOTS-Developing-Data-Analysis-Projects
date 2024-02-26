import argparse
import numpy as np
import pandas as pd


parser = argparse.ArgumentParser(description="Takes in two pathways. The first is a path to the csv file to be processed. The second on is where the processed csv file should be saved.")

# Defining the first argument
parser.add_argument('input_path', type=str, help='Choose the path to your csv file')

# Defining the second argument
parser.add_argument('output_path', type=str, help='Choose where processed csv should be saved')

# Parse the arguments
args = parser.parse_args()


df = pd.read_csv(args.input_path)
output_csv = df.loc[df['valid'] == True]

# Save the csv
output_csv.to_csv(args.output_path, index=False)