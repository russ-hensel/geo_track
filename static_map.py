# -*- coding: utf-8 -*-
"""
Purpose:
    part of my ( rsh ) library of reusable code 
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.
        
        
"""
#   --- do not use for now see photo_inspect photo_ext.py
import sys
# import dis
# import geopy
import gmplot
# from   gmplot import gmplot
# from   geopy.geocoders import Nominatim
# import webbrowser
import requests
import os
import exifread   # with pip install

import PIL.Image
# import PIL.ExifTags
from   geopy.geocoders import Nominatim
import webbrowser


# ---- local imports

sys.path.append( "../rsh" )
import data

# ----------------------------------------
class StaticMap():
    """
    builds a .png of the map of the location.... as specified in the arguments


    not done look for others .....


    but has somone already done this do not go too far
    center (required if markers not present) defines the center of 
    the map, equidistant from all edges of the map. This parameter 
    takes a location as either a comma-separated {latitude,longitude} 
    pair (e.g. "40.714728,-73.998672") or a string address (e.g. 
    "city hall, new york, ny") identifying a unique location on the 
    face of the earth. For more information, see Locations.

     open file
     build html local
     center (required if markers not present) defines the center 
     of the map, equidistant from all edges of the map. This parameter 
     takes a location as either a comma-separated {latitude,longitude} 
     pair (e.g. "40.714728,-73.998672") or a string address 
     (e.g. "city hall, new york, ny") identifying a unique 
     location on the face of the earth. For more information, see Locations.


    """
    def __init__( self, api_key, **kwargs ):
        """



        """

        self.reset( api_key,  **kwargs )

    # -----------------------------
    def reset( self, api_key,  **kwargs ):
        """



        """
        #sekf,long_lat_dict  = None    # have not yet fetched
        #rint( "in reset" )

        self.api_key        = api_key
        #rint( self.api_key )

        # !! fix rest of them
        self.url            = kwargs.get( "url",  "https://maps.googleapis.com/maps/api/staticmap?" )

        self.sensor         = kwargs.get( "sensor",  None )

        self.size           = kwargs.get( "size", "400x400" )
        # if value is None:
        #     value              = "400x400"   # may be limit at 640 .. {}
        # self.size              = value
        self.picture_fn     = kwargs.get( "picture_fn",  )

        zoom                 = kwargs.get( "zoom", 5 )
        # if zoom is None:
        #     zoom              = 5   #
        # self.zoom        = zoom

        center                = kwargs.get( "center", None )
        # if center is None:
        #     center            = None
        # self.center    = center

        marker                = kwargs.get( "marker", "cornflowerblue" )
        # if marker is None:
        #     marker            = "cornflowerblue"
        # self.marker = marker

        #rint( f"\n\n    url {self.url},\n    size {self.size}, ...." )
        return

    # ----------------------------------------
    def _append_request( self, a_request, a_key, a_value ):
        """
        helper to aid in building requests
        read it
        """
        if a_value is not None:
            a_request = f"{a_request}&{a_key}={a_value}"
        return a_request

    # -----------------------------
    def write_map_png_file( self, file_name_out ):
        """
        write file after all set up

        """
        my_request      = self.url
        my_request      = self._append_request( my_request, "center", self.center  )
        my_request      = self._append_request( my_request, "zoom",   self.zoom    )
        my_request      = self._append_request( my_request, "key",    self.api_key )
        my_request      = self._append_request( my_request, "size",   self.size    )
        my_request      = self._append_request( my_request, "sensor", self.sensor  )
        my_request      = self._append_request( my_request, "marker", self.marker  )

        #rint( my_request )
        #rint()

        r = requests.get( my_request )

        with open( file_name_out, 'wb') as a_file:
            a_file.write(r.content)

        if len( r.content ) < 5000  :   # generally an error
            print( "\n\n========= short r.content ================\n\n")
            print( r.content )
            print( "\n\n=========== end r.content ==============\n\n")

    #----------------------------------------------------------------------
    def read_exif( self, file_name ):
        """
        !! only partly working
        read other data in the image file
        and print it ( change to log it )
        should not be in gui.
        not clear belongs in this class   !!!

        Key: GPS GPSLatitude, value [41, 32, 1101/50]
        Key: GPS GPSLongitudeRef, value W
        Key: GPS GPSLongitude, value [71, 0, 79/2]
        see ex_geo_photo for another way


        long lat not working because of typing issues
        """
        print( "" )
        #print(( "read_exif fileInfo.fullname", fileInfo.fullname ))
        print(( f"read_exif file_name  {file_name}" ))

#        print "gui.py  readExif early return so no file info show"
#        return

        f = open( file_name, 'rb')

        # Return Exif tags
        tags = exifread.process_file( f )
        #Note: To use this library in your project as a Git submodule, you should: from <submodule_folder> import exifread
        #Returned tags will be a dictionary mapping names of Exif tags to their values in the file named by path_name.
        #You can process the tags as you wish. In particular, you can iterate through all the tags with:
        f.close()
        for tag in list(tags.keys()):
            if tag not in ('JPEGThumbnail', 'TIFFThumbnailxx', 'Filenamexx', 'EXIF MakerNotexx'):
                print(( "Key: %s, value %s" % (tag, tags[tag] ) ))


        #gps_info     = exif['GPSInfo']
        north        = tags.get( "GPS GPSLatitude", None )
        east         = tags.get( "GPS GPSLongitude", None )
        print( "gps_info" )
        print( f"north {repr(north)}" )
        print( north, east )
        print( north.values[0] )
        print( float( north.values[0]) + 1., flush = True)

        lat      =  ((( north.values[0] * 60 + north.values[1] ) * 60 + north.values[2]) / (60 * 60.) )
        long     =  ((( east[0] *  60 + east[1] )  * 60 + east[2])  / (60 * 60.) )
        long     = -long    # else I got to afganastan
        #rint( lat, long )

        return

    #----------------------------------------------------------------------
    def _convert_to_degress( self, value ):
        """
        Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
        :param value:
        :type value: exifread.utils.Ratio
        :rtype: float
        """
        d = float(value.values[0].num) / float(value.values[0].den)
        m = float(value.values[1].num) / float(value.values[1].den)
        s = float(value.values[2].num) / float(value.values[2].den)

        return d + (m / 60.0) + (s / 3600.0)

    #----------------------------------------------------------------------
    def open_web_map_from_ll( self, long, lat, zoom_level = None ):
        """
        open given long, lat and zoom level ( or use instance ??)
        parameters
            ?? filename html
             ?? file name
             ?? open browser flag

        """
        if zoom_level is None:
            zoom_level  = self.zoom_level
        if zoom_level is None:
            zoom_level =  10

        filename_html  = r"d:/temp.html"  # need full path
        gmap       = gmplot.GoogleMapPlotter( lat, long, zoom_level )
        gmap.marker( lat, long, "cornflowerblue" )
        gmap.draw( filename_html )   # a file name for the html
        webbrowser.open( filename_html, new = 2 )        # auto open file above in new tab

    #----------------------------------------------------------------------
    def get_location( self, file_name ):
        """
        return  ??
            self.long_lat_dict
            mutate:  self.a
        """
        geoloc     = Nominatim( user_agent = "GetLoc")
        locname    = geoloc.reverse( f"{lat}, {long}")
        print( locname.address )

    #----------------------------------------------------------------------
    def get_long_lat( self, file_name ):
        """
        return
            self.long_lat_dict
            mutate:  self.a
        """
        if self.long_lat_dict is not None:
            return self.long_lat_dict #  lready attempted

        ret = {}
        with open( file_name, 'rb' ) as f:
            tags            = exifread.process_file(f)
            latitude        = tags.get('GPS GPSLatitude'     )
            latitude_ref    = tags.get('GPS GPSLatitudeRef'  )
            longitude       = tags.get('GPS GPSLongitude'    )
            longitude_ref   = tags.get('GPS GPSLongitudeRef' )

            if latitude and longitude:

                lat_value = self._convert_to_degress( latitude )
                if latitude_ref.values != 'N':
                    lat_value = -lat_value

                lon_value   = self._convert_to_degress(longitude)
                if longitude_ref.values != 'E':
                    lon_value = -lon_value

                ret =  {'latitude': lat_value, 'longitude': lon_value}

        print( ret  )

        self.long_lat_dict   = ret

        return self.long_lat_dict

    #----------------------------------------------------------------------
    def read_exif_2xxx( self, file_name ):
        """

        # barrowed from
        # https://gist.github.com/snakeye/fdc372dbf11370fe29eb


        #def getGPS(filepath):

        returns gps data if present other wise returns empty dictionary
        """
        ret = {}
        with open( file_name, 'rb' ) as f:
            tags            = exifread.process_file(f)
            latitude        = tags.get('GPS GPSLatitude'     )
            latitude_ref    = tags.get('GPS GPSLatitudeRef'  )
            longitude       = tags.get('GPS GPSLongitude'    )
            longitude_ref   = tags.get('GPS GPSLongitudeRef' )
            if latitude:
                lat_value = self._convert_to_degress( latitude )
                if latitude_ref.values != 'N':
                    lat_value = -lat_value
            else:
                return {}    # !! not right refactor

            if longitude:
                lon_value   = self._convert_to_degress(longitude)
                if longitude_ref.values != 'E':
                    lon_value = -lon_value
            # else:
            #     return {}
                ret =  {'latitude': lat_value, 'longitude': lon_value}

        print( ret  )
        return ret


# file_path = 'file path of the file'
# gps = getGPS(file_path)
# print gps





# ----------------------------------------
def ex_static_map_class ():
    # ex_name  = "ex_static_map_class"   # end with >>    ex_helpers.end_example( ex_name )  # not part of example, marks end
    # print( f"""{ex_helpers.begin_example( ex_name )}
    #        Python | Get a google map image of specified location using Google Static Maps API - GeeksforGeeks
    #                *>url  https://www.geeksforgeeks.org/python-get-google-map-image-specified-location-using-google-static-maps-api/

    #       """ )

    zoom_world      = 1
    zoom_landmass   = 5
    zoom_city       = 10
    zoom_street     = 15
    zoom_building   = 20

    url             = None
    zoom            = None        # zoom defines the zoom  level of the map
    center          = None
    size            = "400x400"   # may be limit at 640 ...
    size            = "600x600"   # may be limit at 640 ...
    size            = None
    marker          = None        # values "cornflowerblue" ??
    sensor          = None        # dont know
    api_key         = None        # sign up for one

    fn_out          = "ex_static_map.png"

    # ---- actual values
    #api_key         = ex_helpers.get_data( "google_api_key_gmp" )
    api_key         = data.get_data( "google_api_key_gmp" )  # you will need to get you own key


    # url variable store url
    url             = "https://maps.googleapis.com/maps/api/staticmap?"

    # center defines the center of the map,
    # equidistant from all edges of the map.
    center          = "Dehradun"
    center          = "Williamsburg,Brooklyn,NY"
    zoom            = 10
    zoom            = zoom_street
    marker          = "cornflowerblue"

    a_staticmap_dict    = {    "url":       url,
                               "api_key":   api_key,
                               "size":      size,
                               "zoom":      zoom,
                               "center":    center,
                               "marker":    marker,
                               "sensor":    sensor,
                        }

    a_staticmap_dict    = {    "url":       url,
                               "api_key":   api_key,
                               "size":      size,
                               "zoom":      zoom,
                               "center":    "540 Horseneck Rd, Dartmouth, Ma, USA",
                               "marker":    marker,
                               "sensor":    sensor,
                        }

    a_static_map    = StaticMap( **a_staticmap_dict )
    a_static_map.write_map_png_file( fn_out )

    a_dict          = a_static_map.read_exif_2(  r"D:\PhotosRaw\2022\Phone\PXL_20220914_193543215.jpg"  )

    # if a_dict: !!
    lat      = a_dict[  'latitude' ]
    long      = a_dict[ 'longitude' ]

    a_static_map.open_web_map( long, lat, zoom_city  )


    # shell out to see
    ret   = os.system( fn_out )

    # ex_helpers.print_double_bar_sep()

    # ex_helpers.end_example( ex_name )  # not part of example, marks end

ex_static_map_class()
