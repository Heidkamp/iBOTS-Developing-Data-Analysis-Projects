import argparse as ap

# 1. Create an argument parser
parser = ap.ArgumentParser(description="Greeting user.")

# 2. create argument
parser.add_argument('name', type=str, help="name of the user")
parser.add_argument('--group', type=str, default="iBehave", help="group of the person")

# 3. parse through the arguments
args = parser.parse_args()

print(f"Hello, {args.name}. You are part of {args.group}")

