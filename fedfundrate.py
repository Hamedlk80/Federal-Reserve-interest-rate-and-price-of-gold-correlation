import requests

# Define the FRED API endpoint and your API key
api_url = "https://api.stlouisfed.org/fred/series/observations"
api_key = "your_api_key_here"

# Define the series ID for the Federal Funds Rate
series_id = "FEDFUNDS"

# Define parameters for the API request
params = {
    "series_id": series_id,
    "api_key": api_key,
    "file_type": "xml"
}

# Make the API request
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Print the XML response
    print(response.text)
else:
    print("Failed to fetch data. Status code:", response.status_code)
