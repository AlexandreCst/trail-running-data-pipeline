"""Data transformer module"""

import pandas as pd

from pathlib import Path

def export_to_parquet(weather_dict):
    """Export the weather data in parquet file"""
    
    # Get weather by hour contain in json_file
    hourly_data = weather_dict["hourly"]["time"]

    # Convert str time values in datetime format
    weather_dict["hourly"]["time"] = pd.to_datetime(hourly_data, format="%Y-%m-%dT%H:%M")

    # Define DataFrame based on hourly weather contained in json_file dict
    df = pd.DataFrame(weather_dict["hourly"])

    # Define path and generate parquet file
    path = Path(__file__).parent.parent.joinpath("data", "raw", "hourly_weather.parquet")
    df.to_parquet(path, engine="pyarrow")