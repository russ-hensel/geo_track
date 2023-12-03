    # ------------------------------------------


One quick solution is to access the share with nautilus (going to Network or manually entering smb://...).

smb://bulldog.local/j_sg_bigcase/


ln -s /path/to/original /path/to/link


can i create a symbolic link to a smb: like directory


ln -s  smb://bulldog.local/j_sg_bigcase/  ~/j_on_net

    made a broken link


ln -s  smb://bulldog.local/j_sg_bigcase/  ~/j_on_net/
     ln: failed to create symbolic link '/home/russ/j_on_net/': No such file or directory


created dir then ran command
    ln -s  smb://bulldog.local/j_sg_bigcase  ~/j_on_net_2
            created a doc not a dir  --- is a broken link



def _make_gpx_from_data( self, gpx_data ):
        """
        Purpose
            from self.gpx_data make
            self.gpx     a gpx object


        Arg
            gpx_data -- photo plus objects
        Return
             gpx object
        Notes:
            reject data point if lat or long misssing
        """
        msg     = f"make_gpx_from_data..."
        AppGlobal.gui.write_gui( msg )
        # Create a GPX object
        gpx = gpxpy.gpx.GPX()

        # Create a track
        track = gpxpy.gpx.GPXTrack()
        gpx.tracks.append(track)

        track_point_list        = []
        max_min_lat_long        = MaxMinLatLong()  # move to

        # for i_lat_long in self.gpx_data:

        #     # Create some track points with made-up data
        #     a_track_point           = gpxpy.gpx.GPXTrackPoint(
        #                                  latitude  = i_lat_long[0],
        #                                  longitude = i_lat_long[1] )

        for data_point in gpx_data:

            if data_point.lat is None or data_point.long is None:
                continue

            max_min_lat_long.add_lat_long( data_point.lat, data_point.long)
            # Create some track points with made-up data
            a_track_point           = gpxpy.gpx.GPXTrackPoint(
                                         latitude  = data_point.lat,
                                         longitude = data_point.long,
                                             )

            a_track_point.time      = datetime.datetime( 2023, 10, 26, 10, 0, 0 )
            a_track_point.elevation = 100
            # a_track_point.speed     = 5  # meters per second
            track_point_list.append( a_track_point )

            # a_track_point = gpxpy.gpx.GPXTrackPoint(latitude=37.234567, longitude=-122.876543)
            # # a_track_point.time      = datetime.datetime(2023, 10, 26, 10, 15, 0)
            # # a_track_point.elevation = 110
            # # a_track_point.speed     = 4.5  # meters per second
            # track_point_list.append( a_track_point )

        # Add track points to the track
        track.segments.append(gpxpy.gpx.GPXTrackSegment( track_point_list ))
        self.max_min_lat_long = max_min_lat_long   # not good
        # Serialize the GPX data to a string
        gpx_data = gpx.to_xml()

        #rint(gpx_data)
        msg     = "make_gpx_from_data done" #" {gpx_data}"
        AppGlobal.gui.write_gui( msg )
        return  gpx







--------------



runfile('/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track/geo_track.py', wdir='/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track')
put a useful comment about above here remove sys.path.append, and copy over contents
========= restart =================
Directory: (  >>/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track<< switch if not '' to >>/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track<<
self.tk_win_geo 1200x500+50+50
In parameters: no special settings for computer_id russ-thinkpad-p72
log_saved_for_later 10 pre logger debug -- did it work
Message from AppGlobal.print_debug >> logger level in App = 10 will show at level 10
self._polling_pause >False<
Error messages may be in log file, check it if problems -- check parameters.py for logging level
gui.run: mainloop comming up...
<bound method DFabc.demo_filter of <file_filters.DFAll object at 0x7fe8375f1f60>>
File format not recognized.
rb indes is 0
allright to comment out
Starting _gpx_to_map... unknown points
Adding coords to the map...
span_lat  = 96.66437197222223    span_long = 176.297167
got zoom 5 for a max_span of 176.297167
len( gpx.tracks )  {len( gpx.tracks )}
Added 30 coords to the map.
Map saved.


--------------------


Python 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0]
Type "copyright", "credits" or "license" for more information.

IPython 8.15.0 -- An enhanced Interactive Python.

runfile('/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track/scratch.py', wdir='/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track')
  File <unknown>:83
    self.tk_win_geo 1200x500+50+50
                       ^
SyntaxError: invalid decimal literal


runfile('/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track/geo_track.py', wdir='/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track')
put a useful comment about above here remove sys.path.append, and copy over contents
========= restart =================
Directory: (  >>/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track<< switch if not '' to >>/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track<<
self.tk_win_geo 1200x500+50+50
In parameters: no special settings for computer_id russ-thinkpad-p72
log_saved_for_later 10 pre logger debug -- did it work
Message from AppGlobal.print_debug >> logger level in App = 10 will show at level 10
self._polling_pause >False<
Error messages may be in log file, check it if problems -- check parameters.py for logging level
gui.run: mainloop comming up...
<bound method DFabc.demo_filter of <file_filters.DFAll object at 0x7fd0cc3d9f30>>
File format not recognized.
write_photo_points default_photo_points.csv
write_photo_points done 29
len(photo_points) {len(photo_points)}
Starting _gpx_to_map... unknown points
Adding coords to the map...
span_lat  = 0.0    span_long = 0.0
got zoom 14 for a max_span of None
len( gpx.tracks )  {len( gpx.tracks )}
Added 1 coords to the map.
Map saved.
done DirScan