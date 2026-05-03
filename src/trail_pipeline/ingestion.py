"""Data ingestion module"""

import requests, json, logging

from pathlib import Path
from requests.exceptions import RequestException

# Define trail_pipeline.ingestion logger
logger = logging.getLogger(__name__)

def openmeteo_api_call():
    """Fonction to request openmeteo API and get the historical weather in Lyon
    at 2026-03-29"""

    # API URL to get historical weather data
    url = "https://archive-api.open-meteo.com/v1/archive"

    # Params to get historical weather data for Lyon at 2026-03-29
    params = {
    "latitude": 45.7485,
    "longitude": 4.8467,
    "start_date": "2026-03-29",
    "end_date": "2026-03-29",
    "hourly": ["temperature_2m", "relative_humidity_2m", "cloud_cover", "rain"],
    }

    # API request
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Check if HTTP error occured
        data = response.json() # Convert response to JSON format
        logger.info("Data retrieved")
        return data
    # Catch if an error occured when calling API
    except RequestException:
        logger.error("No data available", exc_info=True) 
        raise


def write_json_weather(data):
    """Generate JSON file with weather data provide by calling openmeteo API"""
    
    # Define the relative path compared with the file where the script are located
    path = Path(__file__).parent.parent.parent.joinpath("data", "raw", "weather_archive.json")
    
    # Create the folder if it doesn't exist
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save data about historical weather in JSON file
    try:
        with path.open(mode="w") as json_file:
            json.dump(data, json_file, indent=4)
            logger.info("JSON file created")
    
    except OSError:
        logger.error("Error, no JSON file created", exc_info=True)
        raise