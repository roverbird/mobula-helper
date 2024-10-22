import os
import csv
from collections import defaultdict
from datetime import datetime

# The purpose of this script is to check integrity of historical price data
# The resulting csv will show you days where price data is missing

# Define directories and files
# Input_dir contains csv files with price data
input_dir = './data/'
# Output contains diagnistics results
output_file = './mdiagnoz.csv'

# Initialize list to hold diagnostic results
diagnostic_results = []

# Function to group timestamps by day and find incomplete days
def find_incomplete_days_in_file(filename):
    # Dictionary to hold counts of hours per day
    daily_counts = defaultdict(set)

    # Open and read the CSV file
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) > 1:  # Ensure row has at least two columns (timestamp)
                timestamp_str = row[0]

                # Convert timestamp string to datetime object
                try:
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                    day_str = timestamp.strftime('%Y-%m-%d')
                    hour_str = timestamp.strftime('%H')  # Get the hour part
                    # Use a set to track unique hours for each day
                    daily_counts[day_str].add(hour_str)
                except ValueError:
                    print(f"Skipping invalid timestamp: {timestamp_str} in file {filename}")
                    continue

    # Check for incomplete days
    incomplete_days = []
    for day, hours in daily_counts.items():
        if len(hours) < 24:  # If less than 24 unique hourly data points
            incomplete_days.append(f"{day} ({len(hours)}/24 hours)")

    return incomplete_days

# Iterate over all *_data.csv files in the directory
for filename in os.listdir(input_dir):
    if filename.endswith('_data.csv'):
        filepath = os.path.join(input_dir, filename)
        incomplete_days = find_incomplete_days_in_file(filepath)

        # If there are incomplete days, add them to the diagnostic results
        if incomplete_days:
            for day_info in incomplete_days:
                diagnostic_results.append(f"{filename},{day_info}")

# Write the diagnostic results to output CSV
with open(output_file, 'w') as diag_file:
    diag_file.write("filename,day_info\n")  # Write header
    for line in diagnostic_results:
        diag_file.write(line + "\n")

print(f"Diagnostic completed. Results saved to {output_file}.")

