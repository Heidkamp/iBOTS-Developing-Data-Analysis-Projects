
 # merge_single_trial_data.py
import pandas as pd
import argparse

def merge_single_trial_data(task_csv, performance_csv, output_csv):
    # Read task and performance data
    task_data = pd.read_csv(task_csv)
    performance_data = pd.read_csv(performance_csv)

    # Merge the data based on some common column, e.g., trial_id
    merged_data = pd.merge(task_data, performance_data, on='trial')

    # Sort the rows based on the "trial" column
    merged_data = merged_data.sort_values(by='trial')

    # Save the merged data to a CSV file
    merged_data.to_csv(output_csv, index=False)

def main():
    parser = argparse.ArgumentParser(description="Merge single-trial task and performance data into a single CSV file.")
    parser.add_argument("task_csv", help="Path to the task data CSV file.")
    parser.add_argument("performance_csv", help="Path to the performance data CSV file.")
    parser.add_argument("output_csv", help="Path to the output CSV file.")
    args = parser.parse_args()

    merge_single_trial_data(args.task_csv, args.performance_csv, args.output_csv)

if __name__ == "__main__":
    main()


# ../data/processed/performance_data.csv
# ../data/processed/task_data.csv