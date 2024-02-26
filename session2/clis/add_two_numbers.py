import argparse

parser = argparse.ArgumentParser(description="Take in numbers")

# Defining the first argument
parser.add_argument('number1', type=float, help='First input')

# Defining the second argument
parser.add_argument('number2', type=float, help='Second input')

# Parse the arguments
args = parser.parse_args()


print(args.number1 + args.number2)