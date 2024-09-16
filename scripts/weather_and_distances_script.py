from meteostat import Point, Daily
from datetime import datetime
from geopy.distance import geodesic

# Coordinates for UCLA
ucla_location = (47.6501, -122.3016)

# Dictionary of school locations with their coordinates and altitudes
school_locations = {
    "Michigan State": (42.7018, -84.4822),
    "Arizona": (32.2286, -110.9486),
    "Stanford": (37.4349, -122.1615),
    "Southern California": (34.0141, -118.2879),
    "Oregon State": (44.5637, -123.2794),
    "UCLA": (34.0689, -118.4452),
    "Arizona State": (33.4240, -111.9327),
    "California": (37.8719, -122.2504),
    "Oregon": (44.0583, -123.0681),
    "Washington State": (46.7325, -117.1638),
    "Michigan": (42.2780, -83.7382),
    "Colorado": (40.0095, -105.2665),
    "Brigham Young": (40.2518, -111.6493),
    "Utah": (40.7608, -111.8500),
    "Rutgers": (40.5000, -74.4474),
    "Penn State": (40.7982, -77.8599),
    "Boise State": (43.6021, -116.2075),
    "Hawaii": (21.2972, -157.8170)
}


for school, (lat, lon) in school_locations.items():
    # Get the location as a Point
    location = Point(lat, lon)
    
    
    start = datetime(2015, 9, 1)
    end = datetime(2016, 10, 30)

    # Fetch weather data
    data = Daily(location, start, end)
    data = data.fetch()
    print(f"Weather data for {school}:")
    print(data)

    # Calculate the distance from UCLA to the school location
    distance = geodesic(ucla_location, (lat, lon)).miles  # Distance in miles
    print(f"Distance from UW to {school}: {distance:.2f} miles\n")
