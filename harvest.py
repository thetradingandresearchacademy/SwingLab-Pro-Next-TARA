import pandas as pd
import requests
import zipfile
import io
import os
from datetime import datetime

def fetch_bhavcopy():
    # Get today's date in NSE format (DDMMYYYY)
    today = datetime.now().strftime("%d%m%Y")
    # Base URL for the full daily report
    url = f"https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_{today}.csv"
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    print(f"SwingLab Pro Next by TARA: Attempting harvest for {today}...")
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Save to your Smart DB (CSV for GitHub simplicity)
        with open("smart_db.csv", "a") as f:
            f.write(response.text)
        print("✔ Harvest Successful. Data added to Smart DB.")
    else:
        print(f"✘ Harvest Idle: Market Holiday or Data not yet released (Status {response.status_code}).")

if __name__ == "__main__":
    fetch_bhavcopy()
