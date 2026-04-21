"""API ingestion script"""

import openmeteo_requests, numpy

openmeteo = openmeteo_requests.Client()

url = "https://archive-api.open-meteo.com/v1/archive" # API url to query
# Params to get data of Lyon (french city)
params = {
    "latitude": 45.7485,
    "longitude": 4.8467,
    "hourly": ["temperature_2m", "relative_humidity_2m", "cloud_cover", "precipitation_probability"],
    "current": ["temperature_2m", "relative_humidity_2m", "cloud_cover", "precipitation_probability"]
}

responses = openmeteo.weather_api(url, params=params)
response = responses[0]
hourly = response.Hourly()
print(hourly.Variables(0).ValuesAsNumpy())
