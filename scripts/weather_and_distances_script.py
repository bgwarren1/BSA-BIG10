from meteostat import Point, Daily
from datetime import datetime
from geopy.distance import geodesic

# Coordinates for UCLA
ucla_location = (34.0689, -118.4452)

# Dictionary of school locations with their coordinates
school_locations = {
    "San Diego State": (32.7831, -117.1195),
    "Utah": (40.7608, -111.8500),
    "Oregon State": (44.5637, -123.2794),
    "Stanford": (37.4349, -122.1615),
    "Arizona": (32.2286, -110.9486),
    "Southern California": (34.0141, -118.2879),
    "Colorado": (40.0095, -105.2665),
    "Oregon": (44.0583, -123.0681),
    "Arizona State": (33.4240, -111.9327),
    "California": (37.8719, -122.2504),
    "Washington": (47.6501, -122.3016),
    "Cincinnati": (39.1313, -84.5162),
    "Washington State": (46.7325, -117.1638),
    "Oklahoma": (35.2059, -97.4424),
    "Memphis": (35.1215, -89.9773),
    "Texas A&M": (30.6103, -96.3391),
    "Brigham Young": (40.2518, -111.6493),
    "Nevada-Las Vegas": (36.0908, -115.1830),
    "Virginia": (38.0336, -78.5080),
    "Nebraska": (40.8203, -96.7056)
}

# Loop through the dictionary to calculate distances and get weather data
for school, coords in school_locations.items():
    # Get the location as a Point
    location = Point(coords[0], coords[1])
    
    # Set the date range (you can adjust as needed)
    start = datetime(2015, 9, 1)
    end = datetime(2016, 10, 30)

    # Fetch weather data
    data = Daily(location, start, end)
    data = data.fetch()
    print(f"Weather data for {school}:")
    print(data)

    # Calculate the distance from UCLA to the school location
    distance = geodesic(ucla_location, coords).miles  # Distance in miles
    print(f"Distance from UCLA to {school}: {distance:.2f} miles\n")

