import simplekml

# Create a KML object
kml = simplekml.Kml()

# Define some coordinate points (latitude, longitude)
coordinates = [
    (37.7749, -122.4194),  # San Francisco, CA
    (34.0522, -118.2437),  # Los Angeles, CA
    (40.7128, -74.0060),   # New York City, NY
]

# Create a KML LineString
linestring = kml.newlinestring(name="My Path")
linestring.coords = coordinates

# Set altitude mode to clampToGround to ensure the path follows the Earth's surface
linestring.altitudemode = simplekml.AltitudeMode.clamptoground

# Save the KML file to disk
kml.save("path.kml")

print("KML file 'path.kml' has been created.")




