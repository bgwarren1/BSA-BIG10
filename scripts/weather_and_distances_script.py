from meteostat import Point, Daily
from datetime import datetime
from geopy.distance import geodesic


# I will be manually inputting these results into my .csv
# Coordinates for UCLA 
ucla_location = (34.0689, -118.4452)

# for San Diego State
school_location = (32.7831, -117.1195)  # Coordinates for San Diego State
location = Point(school_location[0], school_location[1])
start = datetime(2023, 9, 9)
end = datetime(2023, 9, 9)

data = Daily(location, start, end)
data = data.fetch()

print(data)

# Calculate the distance from UCLA to the school location
distance = geodesic(ucla_location, school_location).miles  # Distance in miles
print(f"Distance from UCLA to San Diego State: {distance} miles")
