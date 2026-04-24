"""API ingestion script"""

import requests, json, pandas as pd


from pathlib import Path
from requests.exceptions import RequestException

# Build the URL and define the params of the request
historical_url = "https://archive-api.open-meteo.com/v1/archive"
historical_params = {
    "latitude": 45.7485,
    "longitude": 4.8467,
    "start_date": "2026-03-29",
    "end_date": "2026-03-29",
    "hourly": ["temperature_2m", "relative_humidity_2m", "cloud_cover", "rain"],
}

# Request API
try:
    response = requests.get(historical_url, params=historical_params)
    response_data = response.json() # Convert response to JSON format

# Catch if an error occured when calling API
except RequestException: 
    raise


# Define the relative path compared with the file where the script are located
path = Path(__file__).parent.parent.joinpath("data", "raw", "historical_data.json")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

# Save data in JSON file
with path.open(mode="w") as historical_json:
    json.dump(response_data, historical_json, indent=4)

# Convert time values (str) in datetime64[us] format
response_data["hourly"]["time"] = pd.to_datetime(response_data["hourly"]["time"], format="%Y-%m-%dT%H:%M")

# Define DataFrame based on hourly key in response_data dict
df = pd.DataFrame(response_data["hourly"])

# Define path and generate parquet file
parquet_path = Path(__file__).parent.parent.joinpath("data", "raw", "historical_data.parquet")
parquet_file = df.to_parquet(parquet_path, engine="pyarrow")