import simplekml

# Create a KML object
kml = simplekml.Kml()

# Define some coordinate points (latitude, longitude)
coordinates = [
    (37.7749, -122.4194),  # San Francisco, CA
    (34.0522, -118.2437),  # Los Angeles, CA
    (40.7128, -74.0060),   # New York City, NY
]

# Create a KML LineString with tessellate set to True
linestring = kml.newlinestring(name="My Path")
linestring.tessellate = 1  # Set tessellate to 1 to create a tessellated line

# Add coordinates to the LineString
for lat, lon in coordinates:
    linestring.coords.addcoordinates([(lon, lat, 0)])  # Note the order: (longitude, latitude, altitude)

# Set altitude mode to clampToGround to ensure the path follows the Earth's surface
linestring.altitudemode = simplekml.AltitudeMode.clamptoground

# Save the KML file to disk
kml.save("path_tesslate.kml")

print("KML file 'path.kml' has been created.")
