# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:32:59 2023

@author: russ
"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    main.main()

# --------------------

import os
from   pathlib import Path
# ----- local


from   app_global import AppGlobal


# --------------------------------------
class DirTreeExplorer(   ):
    """

    Wanted to make a generator or itterator but ran into problems
    for now use as single threaded and makes a list
    list will be the full file name or path of the selected files

    could change to run a process instead of accumulating to a list

    args passed down recursive explore functions, treat as constants once set
    may want a copy for each thread and possibly accumulate data here

    also functions used for processing  .... perhaps a rename ??
    but some args are functions, here or in helper_thread ??
    kind of mess keep counters in app_state
    explore_args

    """
    #---------------------
    def __init__( self,   ):
        """
        Usual init see class doc string
        create
        set file.file_filter
            directory_filter
            max_dir_depth
            use get_next untill returns a null


            a_dir_tree_explorer       =  dir_tree_explorer.DirTreeExplorer()

            a_dir_tree_explorer.reset()
            a_dir_tree_explorer.directory_filter    =
            a_dir_tree_explorer.file_filter         =
            a_dir_tree_explorer.max_dir_depth       =
            a_dir_tree_explorer.gui_write           =    # any function taking a single string, print.... or debug....

            while True:
                file_name   = a_dir_tree_explorer.get_next()
                if  file_name:   # None return at end
                    ..... process
                else:
                    break


        """
        self.file_filter        = None
        self.directory_filter   = None

        self.max_dir_depth      = 0      # 0 is unlimited
        self._dir_depth         = 1      # 0 is unlimited

        # ix are counts
        self._file_ix           = 0   # get with a @property
        self._dir_ix            = 0

        self._current_path      = None    # may be dir_path or file_path
        self.gui_write          = print   # any function that takes a single string
        self.file_list          = []

    #---------------------
    def reset( self,   ):
        """
        run the process in...
        !! converting to path
        """
        1/0
        pass

    # # ----------------------------------------------
    # def __iter__( self ):
    #      return self

    # # ----------------------------------------------
    # def __next__( self ):
    #     self.ix   += 1
    #     if self.ix > self.max:
    #         raise StopIteration
    #     return  self.ix




    # # ----------------------------------------------
    # def run_process( self, ignored_arg  ):
    #     """
    #     run the process in...
    #     !! converting to path
    #     """
    #     #a_path           = Path( AppGlobal.parameters.start_dir)

    #     a_path           = Path(  AppGlobal.gui.dir_browse_widget.get_text( ) )
    #         # must sync with show parms

    #     starting_dir_list  = [a_path]
    #     a_explore_args     = explore_args.ExploreArgs(   )

    #     a_explore_args.set_for_run_process(   )

    #     self.app_state   = AppGlobal.app_state
    #     app_state        = self.app_state

    #     app_state.reset_counts()
    #     app_state.initial_dir   = a_path
    #     app_state.start_ts      = time.time()

    #     msg   = f"Run process, starting at {starting_dir_list[0]} ... "
    #     self.gui_write(  msg, )
    #     print( "helper_thread.run_process()" )
    #     for i_starting_dir in starting_dir_list:
    #         print( f"run_process {i_starting_dir}" )
    #         self.explore_dir( i_starting_dir, 0, a_explore_args  )

    #     app_state.end_ts      = time.time()

    #     msg    = f" app_state >> {app_state}"
    #     self.gui_write(  msg, )

    #     msg   = "\n---- Run Process... Done ----"
    #     self.gui_write(  msg, )



    # # ----------------------------------------------
    # def get_next_file_name( self,  ):

    #     """
    #     """

    #     # self.file_filter       = None
    #     # self.directory_filter  = None

    #     # self.max_dir_depth     = 0      # 0 is unlimited
    #     # self._dir_depth         = 1      # 0 is unlimited

    #     # # ix are counts
    #     # self._file_ix           = 0   # get with a @property
    #     # self._dir_ix            = 0

    #     # self._current_path       = None    # may be dir_path or file_pat
    #     gui   = AppGlobal.gui

    #     if self._current_path is None:
    #         # init the process
    #         msg   = f"get_next_file_name, starting at {self._current_path }"
    #         gui_write(  msg )

    #     else:
    #         #continue the process
    #         pass

    # ----------------------------------------------
    def explore_a_dir_old( self,  starting_dir ):
        """
        call after directory depth is ok
        explore recursively
            get names
            loop thru names

        """
        # new_dir_depth       = self._dir_depth dir_depth + 1
        self._dir_depth     +=1
        names               = os.listdir( starting_dir )  # may throw [WinError 3]

        msg                 = f"exploring at depth {new_dir_depth}: {starting_dir}"
        AppGlobal.logger.info( msg )
        self.gui_write( msg + "\n" )

        for i_name in names:
            # file from / file to
            i_name        = i_name.replace( "\\", "/" )
            i_full_name   = os.path.join( starting_dir, i_name )
                ## ?? just default to / why not and remove next
            i_full_name   = i_full_name.replace( "\\", "/" )   # !! revise for path
            # next a named tuple
            # i_file_info   = FileInfo( file_name         = i_name,
            #                           path_name         = starting_dir,
            #                           full_file_name    = i_full_name )

            # could have pause here too #
            if self.app_state.cancel_flag:
                msg = "user cancel"
                raise app_global.UserCancel( msg )

            if self.app_state.pause_flag:
                time.sleep( self.parameters.ht_pause_sleep )

            if os.path.isdir( i_full_name ):
                msg     = ( f"os.path.isdir self.app_state.ix_explore_dir = "
                            f"{self.app_state.ix_explore_dir} new_dir_depth = {new_dir_depth}"
                            f"    explore_args.max_dir_depth = {explore_args.max_dir_depth}" )
                AppGlobal.logger.debug( msg )
                print( msg )

                if ( ( explore_args.max_dir_depth == -1  ) or
                     ( explore_args.max_dir_depth  >  new_dir_depth  ) ):
                         # may be more efficient placement of this so called once
                    self.app_state.count_dir      += 1
                        # or one for file, one for dir, and one for error better ??
                    if explore_args.df( i_full_name ):   # the filter for dir
                        msg     = f"making recursive call {i_full_name} {new_dir_depth}"
                        print( msg )
                        self.explore_dir( i_full_name, new_dir_depth, explore_args )
                    else:
                        msg     = f"\nhit false on dir filter df  {i_full_name} "
                        print( msg )
                else:
                    msg         = f"\nhit max dir depth {i_full_name} {new_dir_depth} "
                    AppGlobal.logger.info( msg )
                    print( msg )
                continue
            #import pdb; pdb.set_trace()

            # ==== we got a file not a dir
            file_size               = os.path.getsize(  i_full_name )
                #  os.stat( file_name ).st_size  ))
            app_state               = self.app_state
            app_state.bytes_total  += file_size
            app_state.count_total  += 1

            #msg    = f"adding to bytes_total {i_name} {file_size} {app_state.bytes_total}"
            #rint( msg )

            if explore_args.ff( i_name, i_full_name ):  # ff is file filter
                # import pdb; pdb.set_trace()    # set breakpoint
                #msg   = f"file found   {i_full_name}"
                #AppGlobal.logger.info( msg )
                self.gui_write( msg )

                try:
                    if explore_args.process_item_fun is not None:
                        app_state.count_processed        += 1
                        app_state.bytes_processed        +=  file_size
                        msg   = f"file found processed {i_full_name}"
                        AppGlobal.logger.info( msg )
                        print( msg )
                        # no function yet but coming !!
                        explore_args.process_item_fun( Path( i_full_name ), "ok" )
                    else:
                        print( ">>>>>>> why is explore_args.process_item_fun None !!!!!!!!")
                        #pass # !! but this may be an error

                except Exception as a_except:
                    # way to much log it !!
                    msg = f"exception on file {i_full_name}"
                    print( type(a_except)  )   # the exception instance
                    print( "a_except.args = {a_except.args}"  )   # arguments stored in .args
                    print( a_except     )      # __str__ allows args to printed directly
                    s_trace = traceback.format_exc()
                    print( f"format-exc>>{s_trace}<<" )
            else:
                # skip
                app_state.count_skipped        += 1
                app_state.bytes_skipped        +=  file_size




    # --------------------------------------------------
    def get_filter_text( self ):
        """
        get the text of all the filters
        """
        filter_texts   = []
        filter_objects = self.filter_objects
        # is no filter all files, or do we require at least one filer
        if len( filter_objects ) == 0:
            text = "no filters"

        else:
            for i_filter_object in filter_objects:
                filter_texts.append( str( i_filter_object ) )
            text  = "\n".join( filter_texts )

        return text




    # ----------------------------------------------
    def explore_dir( self, starting_dir,    ):
        """
        set up to run process was for dups and keeps not part of this app
        recursive
        could collect files in a list and process as a batch at the end
        probably more efficient but for now one at a time

        call after directory depth is ok
        explore recursively
            get names
            loop thru names


        explore and list files in dir and recursive to sub dirs
            starting_dir  = name of dir we start from
            dir_depth     = depth of starting_dir, 0 for initial call
            additional args   current depth
                           filter

        Args:
            starting_dir -- now a path or string ... may need bigger fix for now either !!

        """

        """
        experiment if can mess with self without getting in trouble
        else pass in as args ??
        """


        # starting_dir    = starting_dir.replace( "\\", "/" )    # normalize win/linux names
        self._dir_depth        += 1
        path_names              = os.listdir( starting_dir )     # may throw [WinError 3]
        # change !! to path lib

        msg             = f"exploring at depth {self._dir_depth }: {starting_dir}"
        self.gui_write( msg + "\n" )

        #  sort of a deep loop can we cagnage
        for i_name in path_names:
            # file from / file to
            i_name        = i_name.replace( "\\", "/" )   # change to pathlib !!
            i_full_name   = os.path.join( starting_dir, i_name )
                ## ?? just default to / why not and remove next
            i_full_name   = i_full_name.replace( "\\", "/" )   # !! revise for path
            # next a named tuple
            # i_file_info   = FileInfo( file_name         = i_name,
            #                           path_name         = starting_dir,
            #                           full_file_name    = i_full_name )

            # # could have pause here too #
            # if self.app_state.cancel_flag:
            #     msg = "user cancel"
            #     raise app_global.UserCancel( msg )

            # if self.app_state.pause_flag:
            #     time.sleep( self.parameters.ht_pause_sleep )

            if os.path.isdir( i_full_name ):
                msg     = ( f"os.path.isdir self.app_state.ix_explore_dir = "
                            f"dir_depth = {self._dir_depth}"
                            f"max_dir_depth = {self.max_dir_depth}" )
                self.gui_write( msg )

                if ( ( self.max_dir_depth == 0  ) or
                     ( self.max_dir_depth  >  self._dir_depth ) ):
                         # may be more efficient placement of this so called once

                        # or one for file, one for dir, and one for error better ??

                        #-------------------------------------------
                        # def check_file( self, file_name, src_dir, dest_dir  ):
                        #     """
                        #     to unifiy with file filter
                        #     needs to be set from outside ...


                    if self.directory_filter.check_dir( i_full_name, None, ) :
                        # may need to work on the filter to make it work
                        msg     = f"making recursive call {i_full_name} {self._dir_depth}"
                        self.gui_write( msg )
                        self.explore_dir( i_full_name, )
                    else:
                        msg     = f"\nhit false on dir filter df  {i_full_name} "
                        print( msg )
                else:
                    msg         = f"\nhit max dir depth {i_full_name} {self._dir_depth} "
                    AppGlobal.logger.info( msg )
                    print( msg )
                    continue    # !! where does this go  -- next file name
            #import pdb; pdb.set_trace()

            # ==== we got a file not a dir
            # file_size               = os.path.getsize(  i_full_name )
            #     #  os.stat( file_name ).st_size  ))
            # app_state               = self.app_state
            # app_state.bytes_total  += file_size
            # app_state.count_total  += 1

            # #msg    = f"adding to bytes_total {i_name} {file_size} {app_state.bytes_total}"
            # #rint( msg )

            if self.file_filter.check_file( i_full_name, None, None  ) :   # i_name of i_full_name
            #if explore_args.ff( i_name, i_full_name ):  # ff is file filter
                # import pdb; pdb.set_trace()    # set breakpoint
                msg   = f"file found   {i_full_name}"
                self.gui_write( msg )
                self.file_list.append( i_full_name )
                # try:
                #     if explore_args.process_item_fun is not None:
                #         app_state.count_processed        += 1
                #         app_state.bytes_processed        +=  file_size
                #         msg   = f"file found processed {i_full_name}"
                #         AppGlobal.logger.info( msg )
                #         print( msg )
                #         # no function yet but coming !!
                #         explore_args.process_item_fun( Path( i_full_name ), "ok" )
                #     else:
                #         print( ">>>>>>> why is explore_args.process_item_fun None !!!!!!!!")
                #         #pass # !! but this may be an error

                # except Exception as a_except:
                #     # way to much log it !!
                #     msg = f"exception on file {i_full_name}"
                #     print( type(a_except)  )   # the exception instance
                #     print( "a_except.args = {a_except.args}"  )   # arguments stored in .args
                #     print( a_except     )      # __str__ allows args to printed directly
                #     s_trace = traceback.format_exc()
                #     print( f"format-exc>>{s_trace}<<" )
            else:
                pass
                # skip
                # self.count_skipped        += 1
                # app_state.bytes_skipped        +=  file_size

    # ----------------------------------------------


    # --------------------------------------------------
    def __str__( self ):
        """
        Purpose:
            see title, what it says, read
        Args:
            n: the number to get the square root of.
        Return:
            mutates self
        Raises:
            none planned
            NoError: if n is not a number
        Args:
            n: the number to get the square root of.
        """

        line_begin  = "\n    "  # formatting aid

        a_str       =  ""
        a_str       = f"{a_str}\n>>>>>>>>>>* app_state()  *<<<<<<<<<<<<"
        a_str       = f"{a_str}{line_begin}state             >{self.state}<"

        return a_str






# ==================== eof =====================


