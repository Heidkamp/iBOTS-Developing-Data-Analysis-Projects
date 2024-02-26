import argparse

parser = argparse.ArgumentParser(description="Take in numbers")

# Defining the first argument
parser.add_argument('number1', type=float, help='First input')

# Defining the second argument
parser.add_argument('number2', type=float, help='Second input')

# Defining an optional argument
parser.add_argument('--scale', type=float, default="1", help='Scale by this number')

# Parse the arguments
args = parser.parse_args()


print((args.number1 + args.number2)*args.scale)