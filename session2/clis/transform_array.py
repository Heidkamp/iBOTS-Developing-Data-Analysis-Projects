import argparse
import numpy as np


parser = argparse.ArgumentParser(description="transforms")
# Defining the first argument
parser.add_argument('input_path', type=str, help='Choose the path to your array')
# Defining the second argument
parser.add_argument('output_path', type=str, help='Choose where the array is saved')
parser.add_argument('--operation', type=str, default="standardize", help="Choose either standardize or normalize")
# Parse the arguments
args = parser.parse_args()


input_array = np.load(args.input_path)
if args.operation == "standardize":
    # Load the input and normalize it
    
    output_array = input_array - np.min(input_array)
    output_array = output_array / np.max(output_array)

    # Save the normalized array
    np.save(args.output_path+"_"+args.operation, output_array)
else:
    
    # Load the input and standardize it
    output_array_stand = (input_array - np.mean(input_array)) / np.std(input_array)

    # Save the standardized array
    np.save(args.output_path+"_"+args.operation, output_array_stand)