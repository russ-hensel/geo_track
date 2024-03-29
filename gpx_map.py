# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 08:01:35 2023

@author: russ


gpx_map.py



from



        fuelio-trip-visualizer        #
        russ mess with it
        runs ok, nice ... add error check, make more modular
          from git hub, url  = ??



"""

# ------------------------------------------
if __name__ == "__main__":
    import main
    main.main()

# ------------------------------------------

# ------------ import libs ----------- #

# core ↓
import gpxpy # parsing and manipulating GPX files (XML based format for GPS tracks)
import folium # visualize data on a Leaflet map
# from folium.plugins import HeatMap

# other ↓
import os # work with files in a folder
import time # calculate script's run time



# ===================== class
class GpxMap( ):
    """
    what is say
    """
    def __init__( self,   ):

        self.gpx_files    = []

        # startTime = time.time()  # run time start
        print("Starting the script...")  # status
        self.routesFolder  = './routes'
        self.map_html      =

    # ---------------------
    def gpx_folder_list( self,   ):
        """


        Parameters
            self.routesFolder = './routes'
        Returns
            mutates self.gpx_files    = []

        """
        # ---------- fun begins here --------- #

        # directory containing GPX files saved by Fuelio


        # get a list of all the files in the directory
        files = os.listdir( self.routesFolder )

        print( f"found files {files}")  # status

        # filter the list to include only .gpx files
        # gpxFiles = [file for file in files if file.endswith('.gpx')][:200] # limit trips to 200
        gpxFiles = [file for file in files if file.endswith('.gpx')]

        if len( gpxFiles ) < 1:
            print( f">>>>>>>>>>did not find any .gpx files in {files} so we are all done here")
            print( "division by 0 comming up  >>>>>>>>>")
            return

        self.gpx_files    = gpxFiles

        return


    # ---------------------
    def what( self, ):
        """


        """

        startTime = time.time()  # run time start


        # variables are later used to calculate the center coordinates of all the GPX files so the map can be centered at that location
        latCenter = 0
        lngCenter = 0

        # count how many trips we are adding to the map; files = trips
        countTrips = len( self.gpx_files )
        print(f"Taking {countTrips} trips...") # status

        print("Adding coords to the map...") # status

        # start counter of points added to the map
        countCoords = 0

        # ---- calculate center of the map --- #

        # loop through the GPX files

        for gpxFile in self.gpx_files:
            # read the GPX file
            with open(os.path.join( self.routesFolder, gpxFile), 'r') as readFile:
                gpx = gpxpy.parse(readFile)

            # extract the latitude and longitude data from the GPX file
            lats, lngs = [], []

            # extracts the latitude and longitude coordinates of each point in each track segment, appending them to separate lists called lats and lngs
            for track in gpx.tracks: # iterable that contains all of the tracks in the GPX file
                for segment in track.segments: # each track is composed of one or more track segments, which are represented by the track.segments iterable
                    for point in segment.points: # each track segment consists of a series of GPS points that make up the track
                        lats.append(point.latitude)
                        lngs.append(point.longitude)
                        countCoords += 1  # increment counter

            # calculates the sum of all latitudes and longitudes, and then divides them by the total number of points in the GPX files to get the average latitude and longitude of all the points
            latCenter += sum(lats)/len(lats)
            lngCenter += sum(lngs)/len(lngs)

        # divides the sum of the averages by the total number of trips to get the center latitude and longitude of all the GPX files
        latCenter /= countTrips
        lngCenter /= countTrips

        # create a Folium map centered at the center coordinates of all the GPX files
        foliumMap = folium.Map(location=[latCenter, lngCenter], zoom_start=14)

        # ------- add a polyline to map ------ #

        # loop through the GPX files and add a PolyLine to the map for each file; if this loop is removed or polyline code is not indented, the map will only show the polyline for 1 file
        for gpxFile in  self.gpx_files:
            # read the GPX file
            with open(os.path.join(self.routesFolder, gpxFile), 'r') as readFile:
                gpx = gpxpy.parse(readFile)

            # extract the latitude and longitude data from the GPX file
            lats, lngs = [], [] # NOTE: map
            # data = [] # NOTE: heatmap

            # extracts the latitude and longitude coordinates of each point in each track segment, appending them to separate lists called lats and lngs
            for track in gpx.tracks: # iterable that contains all of the tracks in the GPX file
                for segment in track.segments: # each track is composed of one or more track segments, which are represented by the track.segments iterable
                    for point in segment.points: # each track segment consists of a series of GPS points that make up the track
                        # NOTE: map
                        lats.append(point.latitude) # extract and add to the list
                        lngs.append(point.longitude) # extract and add to the list

                        # NOTE: heatmap
                        # data.append([point.latitude, point.longitude])

            # NOTE: map
            # add a PolyLine to the map using the latitude and longitude data of the GPX file
            folium.PolyLine(locations=list(zip(lats, lngs))).add_to(foliumMap)

            # NOTE: heatmap
            # add a heat map to the map using the latitude and longitude data of the GPX file
            # HeatMap(data).add_to(foliumMap)

        print(f"Added {countCoords} coords to the map.")

        # ------------ save files ------------ #

        # NOTE: map
        # save the map as an HTML file
        print("Saving map...") # status
        foliumMap.save( self.map_html )
        print("Map saved.") # status

        # NOTE: heatmap
        # print("Saving heatmap...") # status
        # foliumMap.save('heatmap.html')
        # print("Heatmap saved.") # status

        # ------------- run time ------------- #

        endTime = time.time()  # run time end
        totalRunTime = round(endTime-startTime, 2) # round to 0.xx
        print(f"Total script run time: {totalRunTime} seconds. That's {round(totalRunTime/60,2)} minutes.") # status