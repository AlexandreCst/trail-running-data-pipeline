"""Script to orchestrate weather data ingestion and transformation"""

from trail_pipeline import ingestion, transform

if __name__ == "__main__":

    # Get weather archive by calling openmeteo API 
    weather_data = ingestion.openmeteo_api_call()

    # Write JSON file to save weather data
    ingestion.write_json_weather(weather_data)

    # Export the weather data in parquet file
    transform.export_to_parquet(weather_data)