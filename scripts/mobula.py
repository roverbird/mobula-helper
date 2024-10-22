import requests
import csv
import os
from datetime import datetime

# The purpose of this script is to collect hourly price data for selected cryptos using Mobula API
# Run this script hourly as cronjob 
# Cronjob example:
# 0 * * * * bash /path/to/mobula-helper/scripts/mobula.py

# Define the Mobula API URL
url = "https://api.mobula.io/api/1/market/multi-data"

# List your cryple symbols here
querystring = { "symbols": "1INCH,AAVE,ADA,AIOZ,AKT,AMP,APE,APT,AR,ARB,ARKM,ASTR,ATOM,AVAX,AXL,AXS,BCH,BDX,BEAM,BGB,BLUR,BNB,BONK,BSV,BTC,BTG,BTT,CAKE,CFX,CHZ,CKB,COMP,CORE,CRO,CRV,DEXE,DOGE,DOT,EGLD,ENS,EOS,ETC,ETH,FET,FIL,FLOKI,FLOW,FLR,FTM,FTN,GALA,GMT,GNO,GT,HBAR,HNT,ICP,IMX,INJ,IOTA,IOTX,JASMY,KAS,KAVA,KCS,KLAY,KSM,LEO,LINK,LPT,LTC,LUNC,MATIC,MKR,MNT,MOG,NEAR,NEO,NEXO,OKB,OM,OP,ORDI,OSMO,PAXG,PENDLE,PEOPLE,PEPE,PEPECOIN,PRIME,QNT,RAY,RENDER,RON,ROSE,RSR,RUNE,SAFE,SEI,SFP,SHIB,SNX,SOL,STX,SUI,SUPER,TAO,TFUEL,THETA,TON,TRVL,TRX,TURBO,TWT,UNI,VET,WEMIX,WLD,XDC,XEC,XLM,XMR,XRP,ZEC,NMR,OCEAN"}

# Add your API key to the headers
headers = {
    'Authorization': 'code'  # Replace with your actual API key
}

# Define the directory path for saving CSV files
directory = "./data"

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Get the current timestamp in UTC
timestamp_now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# Make the GET request with the headers and query parameters
response = requests.get(url, params=querystring, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Iterate over each cryptocurrency in the response
    for symbol, info in data.get('data', {}).items():
        # Define the file path for each symbol's CSV file
        file_path = os.path.join(directory, f"{symbol}_USDT_data.csv")

        # Open the CSV file in append mode
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Write the header only if the file is empty
            #if file.tell() == 0:
            #    writer.writerow([
            #        "Timestamp", "Symbol", "Price", "Volume", "Liquidity", 
            #        "Total_Supply", "Circulating_Supply", "Rank", "Name"
            #    ])

            # Write the symbol's data (use .get() for safety)
            writer.writerow([
                timestamp_now,
                info.get('symbol', 'N/A'),
                info.get('price', 'N/A'),
                info.get('volume', 'N/A'),
                #info.get('liquidity', 'N/A'),
                #info.get('total_supply', 'N/A'),
                #info.get('circulating_supply', 'N/A'),
                info.get('rank', 'N/A'),
                #info.get('name', 'N/A')
            ])

        print(f"Data for {symbol} written to {file_path}")
else:
    print(f"Error: Failed to fetch data. Status code: {response.status_code}, Response: {response.text}")

