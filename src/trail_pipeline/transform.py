"""Data transformer module"""

import logging, pandas as pd

from pathlib import Path

# Define trail_pipeline.transform logger
logger = logging.getLogger(__name__)

def export_to_parquet(weather_dict):
    """Export the weather data in parquet file"""
    
    try:
        # Get weather by hour contain in json_file
        hourly_data = weather_dict["hourly"]["time"]

        # Convert str time values in datetime format
        weather_dict["hourly"]["time"] = pd.to_datetime(hourly_data, format="%Y-%m-%dT%H:%M")
        logger.debug("Hourly and time keys exist")
    
    except KeyError:
        logger.error("No such key hourly or time", exc_info=True)
        raise

    # Define DataFrame based on hourly weather contained in json_file dict
    df = pd.DataFrame(weather_dict["hourly"])

    try:
        # Define path and generate parquet file
        path = Path(__file__).parent.parent.parent.joinpath("data", "raw", "hourly_weather.parquet")
        df.to_parquet(path, engine="pyarrow")
        logger.info("Parquet file created")
    
    except OSError:
        logger.error("No Parquet file created", exc_info=True)
        raise