


=tk
=random
========Status
========chat
========Versions ====
========Environment =================
========Scratch ====
========Links ====
========Logic ====
========Long and Latitude ====
========Install====
========venv
========to pythonistas gui



!!!!!!!!!!!!!!!!!!!!!!!!


========Status
Status:  basic functions all seem to work if
         system is not stressed


=================tests =====================

for directory scan
D:\PhotosRaw\2023\aferica\phone\africa_3023\safarie\PXL_20230919_163207438.jpg


=========Versions

remember to rename data_hidden to data.py

---------version 10 ---------
     Why:  lots of progress timezone but not done
         still lots of dead code to remove and
         lets get processing to the background
        !! try copy to github again
        ** some code renamed better
        ** more code to rshlib
        ** few more defaults some via parameters
        !* improve help
        !! spacer befor go and bold??


---------version 9 ---------
    Why:  lots of progress on new gui pretty much done
            lots of dead code to remove and lets get processing
            to the background
            wait cursor


    !! problem sorting on none file name... make none ? or something low
    !! problem filter on date that is not timezone aware, may need to convert all
       consider a temporary patch for now

    ** long lat filter done, needs testing, perhaps more values
    !! ?? consider sort on long lat values, by place name or by value
    !! next try filters first on input_gpx file.....

    !! processing to background
    !! and of course below
    !! issues with gpx in file
        !! oputpt control seems not to work
        !! filter on date seems not to work
        ** make it produce photo_points ??
    !* default optput, and sanity check on output
    !* fix error conditions with operation terminate
    !* add progress and info messages
    !* remove dead code, modules....   geo_track start at 2.2.k lines
    !! think v write_file_list( file_name, file_list, append_flag = False ): needs to be hooked in
       to replace geo_track.write_todffl

---------version 8---------
    Why:  lots of progress on new gui, but big changes may mess up
          so just a check point
    !! processing to background
    *! remove old gui components -- when sure have all in new gui, most is
    !! finish below
    ** find old mem size fo about box
    ** get the output check boxes to work at least some
    ** fix all output edit buttons

    map and folium seem to be synomonous

---------version 7
    seems to be lost in mist

---------version 6---------
    -- because version 5 working pretty well

    **  change gui, specif input and output
    ** save the geo_photo_points to csv file
    1! look at ability of stuff to sav!!e file names
    ** save geo_photo_points --- prior to filter sort, use this as a new name
    !! do undone items below
    !! more integrate with infran.view -- look at command line options
    !! let browse be a ddl preload with val from parms then add history
    !! test recursion limit

---------version 5---------

    !! clear dffl file
    ** button to open filelist file
    ** map from directory does not add \n to end of filenames in saving to default
    *! add more info at start of default file list file
    ** adapt dir processor to make an object for file system exploration
    ?? filter on camera ..... ( list cameras found )
    ?? might want to filter on size as it reflects resolution ??
    ?? a filter ?? that checks the file name to see if it is likely from a phone
    ** now drop of points without lat long
    ** add counts to info
    !! add picture frame like functions
    *! integrate with infran.view
    !! work on zoom
    ** implement sorts and filters -- date ok -- sorts seem ok more test ??
    ?? add option to a default filelist file -- just do it, may have append check box
    ** recuse down n levels in directory
    *! more stuff to parms
    !! think about starting dir for browse

    ** allow comments in file list files  -- test
    !! allow other content after file list file name  -- test
    !! convert gpx to kmz
    *! get geotrack icon  -- ok in linux
    !! do undone items below
    ?? consider file line counter

---------version 4---------

    ** convert to list of photplus objects
    *! implement sorts and filters -- date ok
    *! make kmz and open in google earth
    !! filter distance from reference location
    ?? show list of files .... create a file to view in editor and/or message area

---------version 1---------

    ** some stuff works, carry on
    ** get rid of clipboard code
    ** make kmz and open in google earth
    ** scan a dir and make a filelist

---------version 0---------

    ** browse to file
    ** browse to directory
    ** show state

    !! convert to kmz

    note
        kmz open in google earth with double click -- linux and windws i think

========Logic

------------------ new logic

    get input
        then all will be make into PhotoPlus points and process

    dir input


    gpx input
        make photo plus     _gpx_to_pp
            ....


 _dir_to_fl       from a dir           --> make a list of files ( side effect save a file list file  dir_to_file_list.txt )
 _fl_to_fl        from a file- list    --> make a list of files



 gpx_to...       from a gpx file .....                                --> pretty much right to optput, perhaps conversions
 pp_to_pp        from a photo points file .......   ---> make list photo points ( )

 _fl_to_pp               from a list of files ..... ---> make a list of photo points  ( side effect save points )


 pp_filer                        from a list of photo points    --> filter points

 pp_sort                        from filterd points---> sorted photo points

pp_kmz    change to _pp_to_kmz
_pp_gpx                 change to _pp_to_gpx          from sorted photo points make  kmz make map make gph files   -- get ready to open map and earth

 gpx_to_map


------------------- old logic
    separate functions

    map from a list of files
        make a list of files from a file of file names
            make a list of photo plus objects
                sort and filter photo plus objects gpx_points
                    make a gpx object
                        make a map

    map from dir
        make a list of files from a dir
            make a list of photo plus objects
                sort and filter photo plus objects gpx_points
                    make a kmz file
                        open google earth

            if photo_plus.has_lat_long:

========Install====

***ok millhouseMint py_10 jan 2024


No module named 'gpxpy'
No module named 'folium'
No module named 'simplekml'
No module named 'tkcalendar'
No module named 'geopy'
No module named 'gmplot'
No module named 'exifread'
No module named 'haversine'

========Long and Latitude


====venv setup
    geo_track
        python 3.10
import folium

import folium
    conda install folium  worked

      lxml
        conda install lxml   worked

conda install pyperclip
    shapely

        conda install shapely

pip install tkcalendar


import gpxpy
    conda install  gpxpy
import gpxpy.gpx

gpxpy documentation

====Links ====

--------gpx
gpxpy · PyPI
    *>url  https://pypi.org/project/gpxpy/

How to extract .gpx data with python - Stack Overflow
    *>url  https://stackoverflow.com/questions/11105663/how-to-extract-gpx-data-with-python

gpxplotter · PyPI
    *>url  https://pypi.org/project/gpxplotter/

python - Programmatically manipulate GPX data - Geographic Information Systems Stack Exchange
    *>url  https://gis.stackexchange.com/questions/64818/programmatically-manipulate-gpx-data

gpx · PyPI
    *>url  https://pypi.org/project/gpx/

python - open and parse multiple gpx files - Stack Overflow
    *>url  https://stackoverflow.com/questions/51811258/open-and-parse-multiple-gpx-files


--------kml

pyKML Tutorial — pyKML v0.1.0 documentation
    *>url  https://pythonhosted.org/pykml/tutorial.html

fastkml · PyPI
    *>url  https://pypi.org/project/fastkml/

Reading kml file using python - Stack Overflow
    *>url  https://stackoverflow.com/questions/52566302/reading-kml-file-using-python

Overview — SIMPLEKML 1.3.6 documentation
    *>url  https://simplekml.readthedocs.io/en/latest/index.html

KML Tutorial  |  Keyhole Markup Language  |  Google for Developers
    *>url  https://developers.google.com/kml/documentation/kml_tut

Google KML file to python - Stack Overflow
    *>url  https://stackoverflow.com/questions/67454345/google-kml-file-to-python


--------kmz
A KMZ file consists of a main KML file and zero or more supporting files that are packaged using a Zip utility into one unit, called an archive.


How to use Python to open Kmz file and display it on interactive map? - Stack Overflow
    *>url  https://stackoverflow.com/questions/76598717/how-to-use-python-to-open-kmz-file-and-display-it-on-interactive-map

kml - Python - Write to KMZ format - Geographic Information Systems Stack Exchange
    *>url  https://gis.stackexchange.com/questions/455547/python-write-to-kmz-format

geotable · PyPI
    *>url  https://pypi.org/project/geotable/

KMZ Files  |  Keyhole Markup Language  |  Google for Developers
    *>url  https://developers.google.com/kml/documentation/kmzarchives


=======Environment =================

Application developed in the standard python 3.10 environment ( uses f"" so do not go < 3.6 )
Linux mint after initial dev in Windows 10 Pro, but should work on any Python 3.10 or higher  environment
GUI in tkinter and ttk
tasks tend to be quick so this app is single threaded
Author:    Russ Hensel
russ-hensel (russ_hensel)
    *>url  https://github.com/russ-hensel


====errors =====================


Can you write a python program using simpleKML that creates a path or track
in a kml file using made up coordinate values.  The path should be a drawing
on the surface of the earth, not straight lines that go through the earth.
I think the line string should be of the type tessellate.
Save the file to disk.  Your earlier attempts seem to plot around the antarctic,
not in the US.


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
========Scratch =========================================================

D:/PhotosRaw/2023/aferica/phone/africa_3023/safarie/PXL_20230917_142037713.jpg
D:/Russ/0000/python00/python3/_projects/geo_track/test/june2022.txt


========chat


Can you make me a list of the major cities in the
United States and their longitude and latitude ( as decimals )
Please list   the data for each city on a single line and separate with commas.
Do not use a degree sign, and use the signed value of the long and latitude.
List state, city, then the other data.

Can you make me a list of the major cities in the
United States and their longitude and latitude ( as decimals )
Please list   the data for each city on a single line and separate with commas.
Do not use a degree sign, and use the signed value of the long and latitude.
List state, city, then the other data.

------------ used this and that to make csf look at files and think about little program to make the values

  Can you make me a list of the major cities in the
  world and their longitude and latitude ( as decimals )
  Please list   the data for each city on a single line and separate with commas.
  Do not use a degree sign, and use the signed value of the long and latitude.
  List country, city, then the other data.

Australia:


manipulated a bit with libre office see sheet


Australia:     Sydney  =   151.2093
Brazil:         Rio de Janeiro  =   -43.1729
Canada:         Toronto  =   -79.3832
China:         Beijing  =   116.4074
France:         Paris  =   2.3522
India:         Mumbai  =   72.8777
Japan:         Tokyo  =   139.6917
South Africa:         Johannesburg  =   28.0473
United Kingdom:         London  =   -0.1278
USA:    AZ,     Phoenix  =   -112.074
USA:    CA,     Los Angeles  =   -118.2437
USA:    CA,     San Diego  =   -117.1611
USA:    CA,     San Jose  =   -121.8863
USA:    CA,     San Francisco  =   -122.4194
USA:    CO,     Denver  =   -104.9903
USA:    FL,     Jacksonville  =   -81.6557
USA:    IL,     Chicago  =   -87.6298
USA:    IN,     Indianapolis  =   -86.1581
USA:    NC,     Charlotte  =   -80.8431
USA:    NY,     New York City  =   -74.006
USA:    OH,     Columbus  =   -82.9988
USA:    PA,     Philadelphia  =   -75.1652
USA:    TX,     Houston  =   -95.3698
USA:    TX,     San Antonio  =   -98.4936
USA:    TX,     Dallas  =   -96.797
USA:    TX,     Austin  =   -97.75
USA:    TX,     Fort Worth  =   -97.3308
USA:    TX,     El Paso  =   -106.485
USA:    WA,     Seattle  =   -122.3321

values_lat = (
[ "Australia:     Sydney  =   151.2093",
"Brazil:         Rio de Janeiro  =   -43.1729",
"Canada:         Toronto  =   -79.3832",
"China:         Beijing  =   116.4074",
"France:         Paris  =   2.3522",
"India:         Mumbai  =   72.8777",
"Japan:         Tokyo  =   139.6917",
"South Africa:         Johannesburg  =   28.0473",
"United Kingdom:         London  =   -0.1278",
"USA:    AZ,     Phoenix  =   -112.074",
"USA:    CA,     Los Angeles  =   -118.2437",
"USA:    CA,     San Diego  =   -117.1611",
"USA:    CA,     San Jose  =   -121.8863",
"USA:    CA,     San Francisco  =   -122.4194",
"USA:    CO,     Denver  =   -104.9903",
"USA:    FL,     Jacksonville  =   -81.6557",
"USA:    IL,     Chicago  =   -87.6298",
"USA:    IN,     Indianapolis  =   -86.1581",
"USA:    NC,     Charlotte  =   -80.8431",
"USA:    NY,     New York City  =   -74.006",
"USA:    OH,     Columbus  =   -82.9988",
"USA:    PA,     Philadelphia  =   -75.1652",
"USA:    TX,     Houston  =   -95.3698",
"USA:    TX,     San Antonio  =   -98.4936",
"USA:    TX,     Dallas  =   -96.797",
"USA:    TX,     Austin  =   -97.75",
"USA:    TX,     Fort Worth  =   -97.3308",
"USA:    TX,     El Paso  =   -106.485",
"USA:    WA,     Seattle  =   -122.3321" ]

)


    ========to pythonistas gui

    Anyone here interested in desktop applications using graphical user interfaces?
    I have done quite a few apps with a graphical user interface and feel like
    I am getting pretty facile with tk and ttk.  I have also done dome work with qt,
    and just a little with wx.  I would like to learn how to work with Kivy.
    Would any of yoou be interested in working on or discussing
    these topics, or working in some sort of collaborative relationship?

    For info about my work:
        Mostly used tk and ttk, similar coding in about 8 projects.  Gui component
        of 1000 lines ( lots of white space and comments ).

        You can see my code at:

            the gui component is usually in a module with a name like gui.py






