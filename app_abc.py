# -*- coding: utf-8 -*-
#! /usr/bin/python3
#!python3


"""
this is the controller module for the clipboard app

/media/russ/j_sg_bigcase/sync_py_3

"""
# ------------------------------------------
if __name__ == "__main__":
    import main
    main.main()

# ------------------------------------------

import os
import logging
import sys
import traceback
import importlib

# from   subprocess import Popen   #, PIPE  #
import time
import datetime


#----- local imports
import parameters
# import gui_snippets
# import cmd_processor
# import clipper
# import clip_utils
# import string_utils
#import splash

from   app_global import AppGlobal

#---- end imports

# ============================================
class AppABC( ):
    """
    this class is the "main" or controller for the whole app
    to run see end of this file
    it is the controller of an mvc app
    """
    def __init__( self,  q_to_splash, q_from_splash  ):
        """
        usual init for main app
        splash not working as desired, disabled
        splash screen which is of not help unless we sleep the init
        """
        self.app_name          = "None"
        self.version           = "None"
        self.app_version       = self.version   # get rid of dupe at some point... app_version in gui_ext
        self.app_url           = "www.where"
        # clean out dead
        AppGlobal.controller   = self
        self.gui               = None
        #self.old_clip          = ""     # please comment this
        #self.undo_clip         = ""     # and this

        self.polling_delta     = None      # actually set from parameters may want to move location
        self.starting_dir      = ""     # defined later but maybe move to ... -- !! delete in parameters
        # self.polling_pause     = False  # to make polling pause, set from main thread  move to gui
        self.restart( )

    # ----------------------------------
    def restart( self ):
        """
        use to restart the app without ending it
        this process can be very quick -- much quicker than a cold start
        this code is also an extension of __init__
        """
        print( "========= restart =================" ) # not logged until logging is turned on
        if not self.gui is None:
            #self.gui.root.destroy()           # make gui.destroy()
            self.gui.root_destroy()
            importlib.reload( parameters )    # should work on python 3 but sometimes does not
        else:
            #self.q_to_splash
            pass

        self.parameters     = parameters.Parameters( )
             # open early as may effect other parts of code

        #if  self.parameters.set_default_path_here:    # Now change the directory to location of this file
#        if True:
#            py_path    = self.parameters.running_on.py_path
#
#            # retval = os.getcwd()
#            # print( f"Directory now            {retval}")
#
#            print( f"Directory now ( sw if not ''  {os.getcwd()} change to >>{py_path}<<")
#            if py_path != "":
#                os.chdir( py_path )


    # ----------------------------------
    def _prep_gui(self ):
        """
        before gui do this .... not implement yet !! --- but what does it do
        could be import place and clipper setup !!
        """
        pass


    # ------------------------------------------
    def config_logger( self, ):
        """
        configure the python logger
        return change of state
        !! consider putting in app global, include close
        """
        AppGlobal.logger_id     = "App"
        logger                  = logging.getLogger( AppGlobal.logger_id )
        logger.handlers         = []  # get stuff to close from here

        logger.setLevel( self.parameters.logging_level )

        # create the logging file handler
        file_handler = logging.FileHandler( self.parameters.pylogging_fn )

        formatter    = logging.Formatter( '%(asctime)s - %(name)s - %(levelname)s - %(message)s' )
        file_handler.setFormatter( formatter )

        # add handler to logger object -- want only one add may be a problem
        logger.addHandler( file_handler )
        msg  = "pre logger debug -- did it work"
        AppGlobal.logger.debug( msg )

        logger.info( "Done config_logger .. next AppGlobal msg" )
        #rint( "configed logger", flush = True )
        self.logger      = logger   # for access in rest of class?
        AppGlobal.set_logger( logger )

        msg  = ( f"Message from AppGlobal.print_debug >> logger level in App = "
                 f"{self.logger.level} will show at level 10"
                )
        AppGlobal.print_debug( msg )

    # ------------------------------------------
    def close_logger( self, ):
        """
        configure the python logger
        return change of state
        !! consider putting in app global, include close
        """
        logger  = AppGlobal.logger
        for a_handler in logger.handlers:
            a_handler.close()

    # --------------------------------------------
    def prog_info( self,  ):
        """
        record info about the program to the log file
        """
        #logger_level( "util_foo.prog_info"  )
        fll         = AppGlobal.force_log_level
        logger      = self.logger
        logger.log( fll, "" )
        logger.log( fll, "============================" )
        logger.log( fll, "" )
        title       =   ( f"Application: {self.app_name} in mode {AppGlobal.parameters.mode}"
                          f"and version  {self.version}" )
        logger.log( fll, title )
        logger.log( fll, "" )

        if len( sys.argv ) == 0:
            logger.info( "no command line arg " )
        else:
            for ix_arg, i_arg in enumerate( sys.argv ):
                msg = f"command line arg + {str( ix_arg ) }  =  { i_arg })"
                logger.log( AppGlobal.force_log_level, msg )

        msg          = f"current directory {os.getcwd()}"
        logger.log( fll, msg  )

        start_ts     = time.time()
        dt_obj       = datetime.datetime.utcfromtimestamp( start_ts )
        string_rep   = dt_obj.strftime('%Y-%m-%d %H:%M:%S')
        msg          = f"Time now: {string_rep}"
        logger.log( fll, msg )
        # logger_level( "Parameters say log to: " + self.parameters.pylogging_fn )
                         # parameters and controller not available can ge fro logger_level

    # ----------------------------------
    def a_test_polling_function( self,  ):
        """
        test only delete later
        """
        print( "_>" )

    # # ----------------------------------
    # def _polling_task( self,  ):
    #     """
    #     poll for clipboard change and process them
    #     this is only for the auto commands, for
    #     the button push ones see:  controller.button_switcher
    #     protect with a try so polling does not crash the entire application -- "no matter what"
    #     """
    #     # msg       = "+."
    #     # print( msg, end = ""  )   # showing polling is alive

    #     #try:
    #     # ------ begin try
    #     #!#! need a skip in here if doing a redo -- do this next
    #     clipper_text    = self.a_clipper.get_changed_text( )
    #     if clipper_text: # None is false

    #         #self.undo_clip   = clipper_text
    #  #      new_clip_b       = str( new_clip.encode( 'ascii', 'ignore') )
    #                   # some uni just does not seem to work
    # #        self.logger.info( "new_clip = " +  new_clip_b  )
    #         #print( "no app history for now")
    #         print( "need to reinstate history see gui_with_tabs")
    #         # AppGlobal.history.add_item( clipper_text  )
    #         ( is_done, did_what, ret_text )  = self.do_command_transform( clipper_text )

    #         # is_done,
    #         #       True
    #         #               replace clip contents
    #         #               display message with title
    #         #       False
    #         #               no change to clip contents
    #         #
    #         # did_what, ret_text
    #         # ret_text

    #        # if true will have done something ( did_what, and new text
    #        #    if false, the other two args are basically ignored )
    #         if is_done:
    #             self.a_clipper.set_text_stelth( ret_text )
    #             msg    = ( f"<<<<<<<<< polling clip copy:"
    #                        f"\nret: {len(ret_text)} >>{ret_text}<<"
    #                      )
    #             print( msg )
    #             self.gui.write_gui_wt( did_what, ret_text  )

    #         else:
    #             msg    = ( f"<><><><> polling nothing :"
    #                        f"\nnew: {len(clipper_text)} >>{clipper_text}<<"
    #                      )
    #             print( msg )
    #             self.gui.write_gui_wt( "polling did nothing", clipper_text  )

    #     # except dion as ex_arg:
    #     #     self.logger.error( "polling Exception: " + str( ex_arg ) )
    #     #     # ?? need to look at which we catch maybe just rsh
    #     #     (atype, avalue, atraceback)   = sys.exc_info()
    #     #     a_join  = "".join( traceback.format_list ( traceback.extract_tb( atraceback ) ) )
    #     #     self.logger.error( a_join )

    #     # finally:
    #     #     self.gui.root.after( self.polling_delta, self.polling )  # reschedule event


    # -----------------------------------
    def print_list( self, a_list  ):
        """
        what it says, just a little utility, read it.
        !! move to somewhere or replace with pprint
        """
        for i_item in a_list:
            print( i_item )




    # ------------------------------------------
    def some_test( self, ):
        """
        some test, for when I need to experiment
        """
        gui_function_str     = "self.gui.gui_2()"

        self.replace_GUI( gui_function_str  )



    # ----------------- button call backs from gui
    def cb_about( self, ):
        """
        what it says -- about box
        """
        AppGlobal.about()

    # ----------------------------------------------
    def bcb_edit_dev_notes( self, event ):
        """
        used as callback from gui button
        if there is a bind then event sent as well... perhaps shold
        do with all but set event = None as it is not used
        """
        AppGlobal.os_open_txt_file( "readme_rsh.txt" )

    # ----------------------------------------------
    def os_open_dev_notes( self,  ):
        """
        used as callback from gui button
        """
        AppGlobal.os_open_txt_file( "readme_rsh.txt" )

    # ----------------------------------------------
    def os_open_logfile( self,  ):
        """
        used as callback from gui button
        """
        AppGlobal.os_open_txt_file( self.parameters.pylogging_fn )

    # ----------------------------------------------
    def os_open_readme( self,  ):
        """
        often used as callback from gui button
        """
        AppGlobal.os_open_txt_file( self.parameters.readme_fn  )

    # ----------------------------------------------
    def open_tabp_help( self,  ):
        """
        what is says, read
        just a bit of cleanup for a nice file name
        """
        file_name    = self.gui.get_notebook()
        # nex lines may not be complete   may be good enough
        file_name    = file_name.replace( "/", "_" )
        file_name    = file_name.replace( " ", "_" )
        file_name    = file_name.replace( "\n", "_" )
        file_name    = file_name.replace( "*", "" )
        file_name    = f"./help/{file_name}"   # move help to sub dir
        AppGlobal.os_open_txt_file( file_name )



    # ----------------------------------------------
    def os_open_help( self,  ):
        """
        what it says, read
        used as callback from gui button !! change to use app_global
        """
        AppGlobal.os_open_help_file( AppGlobal.parameters.help_file )

    # ----------------------------------------------
    def os_open_parmfile( self,  ):
        """
        used as callback from gui button
        """
        # a_filename = self.starting_dir  + os.path.sep + "parameters.py"
        AppGlobal.os_open_txt_file( "parameters.py" )

    # ----------------------------------------------
    def os_open_gui_log( self,  ):
        """
        gui log loggs what is sent to the gui message area
        used as callback from gui button
        """
        # a_filename = self.starting_dir  + os.path.sep + "parameters.py"
        AppGlobal.os_open_txt_file(  self.parameters.gui_text_log_fn )





# ---- eof =======================
