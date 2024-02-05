# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:33:35 2021

@author: russ
"""

import sys

sys.path.append(  "../rsh" )
sys.path.append(  "../rshlib" )
sys.path.append(  "/media/sf_0000/python00/python3/_projects/rshlib" )
sys.path.append( r"D:\Russ\0000\python00\python3\_projects\rshlib"   )

print( "put a useful comment about above here remove sys.path.append, and copy over contents" )

def main( ):
    import geo_track
    app   = geo_track.App()
    # geo_track.main()  creating it is enough

# --------------------
if __name__ == "__main__":
    # #----- run the full app
    main( )


# # put this at top of each app file:
# # ------------------------------------------
# if __name__ == "__main__":
#     import main
#     main.main()

# ------------------------------------------

# -------- scratch
    #try:  !! add a main
    #the_app = main()
    #except Exception as exception:
#        msg   = "exception in __main__ run the app -- it will end"
#        a_app.logger.critical( msg )
#        a_app.logger.critical( exception,  stack_info=True )
                # just where I am full trace back most info
#        raise
#
#    #finally:
#        print( "here we are done with clipboard" )
#        sys.stdout.flush()
#
