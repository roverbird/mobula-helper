#!/bin/bash

# Usage: ./run_historyM.sh asset_list.csv

# Check if the correct number of arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 asset_list.csv"
    exit 1
fi

# Input file name
asset_list_file=$1

# Read each line of the asset_list.csv
while IFS=',' read -r name symbol time; do
    # Check if the line is empty (in case of blank lines)
    if [[ -z "$name" || -z "$symbol" || -z "$time" ]]; then
        echo "Skipping empty line..."
        continue
    fi
    
    # Run the historyM.py script with the extracted values
    echo "Running mobulaHistory.py for asset: $name, symbol: $symbol, time: $time"
    python3 mobulaHistory.py "$name" "$symbol" "$time"

    # Add a delay (sleep for 5 seconds) before the next request
    echo "Waiting for 2 seconds before the next request..."
    sleep 2
done < "$asset_list_file"

