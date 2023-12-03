# -*- coding: utf-8 -*-
"""

Purpose:
    part of my ( rsh ) library of reusable code 
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.

for work in progress looking for a home





"""



def dt_to_1900( a_datetime ):
    """
    this may be too easy for a util.
    use this for time of year


    """

       # convert to 1900
    dt          = datetime.datetime( 2008, 11, 10, 17, 53, 59 )
    print(( "datetime( 2008, 11, 10, 17, 53, 59 ) = ", dt ))
    dt_1900      = dt.replace( year = 1900 )
    print( f"dt_1900 = {dt_1900}" )

    print(( 'year  :     ', dt_data.year   ))   # all attributes may not exist so may need try except
    print( f"month :     {dt_data.month}"   )   # all
    print(( 'hour  :     ', dt_data.hour   ))
    print(( 'minute:     ', dt_data.minute ))
    print(( 'second:     ', dt_data.second ))
    print(( 'microsecond:', dt_data.microsecond ))
    print(( 'tzinfo:     ', dt_data.tzinfo ))

#

date_1900:
time_of_year:
