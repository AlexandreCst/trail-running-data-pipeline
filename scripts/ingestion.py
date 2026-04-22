"""API ingestion script"""

import requests, json

from pathlib import Path

# Build the URL and define the params of the request
historical_url = "https://archive-api.open-meteo.com/v1/archive"
historical_params = {
    "latitude": 45.7485,
    "longitude": 4.8467,
    "start_date": "2026-03-29",
    "end_date": "2026-03-30",
    "hourly": ["temperature_2m", "relative_humidity_2m", "cloud_cover", "rain"],
}

# Request API
response = requests.get(historical_url, params=historical_params)

if response.status_code == 200:
    response_data = response.json()

    path = Path("trail-running-data-pipeline/data/raw/historical_data.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open(mode="w") as historical_json:
        json.dump(response_data, historical_json, indent=4)

elif response.status_code in [404, 500]:
    print("Oops, bad request!")


