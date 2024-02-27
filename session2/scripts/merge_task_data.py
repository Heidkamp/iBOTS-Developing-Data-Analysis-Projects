# given the path to the task data, combines all files into a CSV file called task_data.csv


# read in single trial
# ../Steinmetz_rawdata/subject-Lederberg/session-20171205/task


import os
import pandas as pd
import argparse


def merge_task_data(task_data_folder, output_csv):
    # List all files in the task data folder
    files = [f for f in os.listdir(task_data_folder) if f.endswith('.csv')]

    # Initialize an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()

    # Iterate through each file and merge the data
    for file in files:
        file_path = os.path.join(task_data_folder, file)
        data = pd.read_csv(file_path)
        merged_data = pd.concat([merged_data, data], axis=0, ignore_index=True)


    # Save the merged data to a CSV file
    merged_data.to_csv(output_csv, index=False)




def main():
    parser = argparse.ArgumentParser(description="Merge task data files into a single CSV file.")
    parser.add_argument("task_data_folder", help="Path to the folder containing task data files.")
    output_csv = "data/processed/performance_data.csv"
    args = parser.parse_args()

    output_directory = os.path.dirname(output_csv)
    os.makedirs(output_directory, exist_ok=True)

    merge_task_data(args.task_data_folder, output_csv)

if __name__ == "__main__":
    main()