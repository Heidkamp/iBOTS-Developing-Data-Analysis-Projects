import sys
import numpy as np
import pandas as pd

# Command-line inputs
input_path = sys.argv[1] # grab the first input
output_path = sys.argv[2] # grab the second input


df = pd.read_csv(input_path)
output_csv = df.loc[df['valid'] == True]

# Save the csv
output_csv.to_csv(output_path, index=False)