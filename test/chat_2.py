# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 08:45:42 2023
chat gpt with new prompt
now works....
"""
Created on Thu Oct 26 08:26:08 2023

@author: chat gpt then russ


I would like to use the Python library gpxpy to create a gpx object ( class GPX ) from text data.
I would like this object to contain one track ( class GPXTrack ) consisting of several
GPXTrackPoints.  Make up the data for all these object.  Please ask me if you need more details
on this task.



AttributeError: 'str' object has no attribute 'isoformat'


I am getting an error :

...

File C:\apps\Anaconda3\envs\geo_track\lib\site-packages\gpxpy\gpxfield.py:100 in format_time
    return time.isoformat().replace('+00:00', 'Z')

AttributeError: 'str' object has no attribute 'isoformat'

Can you change the code to fix this?


looks like time should be a  mod_datetime.datetime

"""


"""

import gpxpy
import gpxpy.gpx
from datetime import datetime

# Create a GPX object
gpx = gpxpy.gpx.GPX()

# Create a track
track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(track)

# Create some track points with made-up data
track_point1 = gpxpy.gpx.GPXTrackPoint(latitude=37.123456, longitude=-122.987654)
track_point1.time = datetime(2023, 10, 26, 10, 0, 0)
track_point1.elevation = 100
track_point1.speed = 5  # meters per second

track_point2 = gpxpy.gpx.GPXTrackPoint(latitude=37.234567, longitude=-122.876543)
track_point2.time = datetime(2023, 10, 26, 10, 15, 0)
track_point2.elevation = 110
track_point2.speed = 4.5  # meters per second

# Add track points to the track
track.segments.append(gpxpy.gpx.GPXTrackSegment([track_point1, track_point2]))

# Serialize the GPX data to a string
gpx_data = gpx.to_xml()

# Print the GPX data
print(gpx_data)
