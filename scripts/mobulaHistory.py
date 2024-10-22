import requests
import json
import os
import argparse
from datetime import datetime

# The purpose of this script is to collect historical crypto price data from Mobula
# Each symbol processed individually
# List of tokens to process is assets_list.csv
# The script is ran from history.sh

# Define the function to parse JSON to CSV
def parse_json_to_csv(data, symbol):
    # Extract the name from the data
    name = data['data']['name']
    
    # Initialize a list to hold CSV formatted strings
    csv_lines = []
    
    # Extract price and volume history
    price_history = data['data']['price_history']
    volume_history = data['data']['volume_history']
    
    # Iterate through both price and volume history
    for price_entry, volume_entry in zip(price_history, volume_history):
        timestamp_ms_price = price_entry[0]
        price = price_entry[1]
        
        timestamp_ms_volume = volume_entry[0]
        volume = volume_entry[1]
        
        # Convert from Unix ms to human-readable format
        human_timestamp = datetime.utcfromtimestamp(timestamp_ms_price / 1000).strftime('%Y-%m-%d %H:%M:%S')
        
        # Format the CSV line to include timestamp, symbol, price, volume, and name
        csv_line = f"{human_timestamp},{symbol},{price},{volume},{name}"
        csv_lines.append(csv_line)
    
    # Join all lines into a single CSV string
    csv_output = "\n".join(csv_lines)
    
    return csv_output

# Set up command line argument parsing
parser = argparse.ArgumentParser(description="Fetch market history data and save as CSV.")
parser.add_argument("name", type=str, help="The asset name (e.g., Bitcoin).")
parser.add_argument("symbol", type=str, help="The asset symbol (e.g. BTC)")
parser.add_argument("time", type=str, help="The start time in Unix milliseconds (e.g., 1695168000000).")

args = parser.parse_args()

# Define the URL for the API
url = "https://api.mobula.io/api/1/market/history"

# Define the names query parameter
querystring = {
    "asset": args.name,  # Use command line argument for asset name
    "from": args.time,   # Use command line argument for time
    "period": "1h"
}

# Add your API key to the headers
headers = {
    'Authorization': 'code'  # Replace with your actual API key
}

# Define the directory path for saving CSV files
directory = "./data"

# Make the GET request with the headers and query parameters
response = requests.get(url, params=querystring, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Convert the JSON data to CSV format, passing the symbol
    csv_data = parse_json_to_csv(data, args.symbol)

    # Define the filename
    filename = f"{args.symbol}_USDT_data.csv"
    file_path = os.path.join(directory, filename)

    # Save the CSV data to a file
    with open(file_path, 'w') as file:
        file.write(csv_data)

    print(f"Data saved to {file_path}")
else:
    print(f"Error fetching data: {response.status_code} - {response.text}")

