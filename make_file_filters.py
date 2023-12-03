# -*- coding: utf-8 -*-
"""



MOVE EVERYTHING TO FILE_FILTER_BUILDER.PY   --------- KEEP HERE FOR JUST A WHILE

Purpose:
    part of my ( rshlib ) library of reusable code
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.


    make filters for common use and example code
    copy or include


    !! to do make a code backup filter that excludes
          _pycac.....
          .       files which seem to be ide stuff



see also file_filter_builder.py
but see make_file_filters.py


"""

import file_filters

#----------------------------------------------
def make_current_python_project_copy():
    """

#a_file_filter, a_dir_filter =  make_current_python_project_copy()

    """
    a_file_filter    = file_filters.FFAll()
    file_filter      = file_filters.FFNameStartsWith( [ "r", "read", "x" ]  )
    #FFExtList(   )  # might limit files to much include .py.....

    a_dir_filter     = file_filters.DFNameStartsWith( [ "old", ] )


    return a_file_filter, a_dir_filter


#----------------------------------------------
def make_rshlib_for_git():
    """
    depth = 0 or 1 -- not in filter
    no readme_rsh.txt  ( would overwrite project's )
    _init    for the init.py
    _        for the backup files in test

    """
    # a_file_filter    = file_filters.FFAll()
    a_file_filter               = file_filters.FFNameStartsWith( [   "readme_rsh",  "__init", "_"  ]  )
    #FFExtList(   )  # might limit files to much include .py.....
    a_file_filter.include_true  = False

    # ---- directory filter
    #a#_dir_filter     = file_filters.DFNameStartsWith( [ "old", ] )

    a_dir_filter     = file_filters.DFAll()

    #print( a_file_filter, "\ndir", a_dir_filter )

    return a_file_filter, a_dir_filter

# a_file_filter, a_dir_filter =  make_current_python_project_copy()

#----------------------------------------------
def make_src_for_git():
    """
    source filter for copying to git
    depth = 0 or 1 -- not in filter ... perhaps add

    _init    for the init.py
    _        for the backup files in test
    scratch
    old
    .        for pycache...


    # run it



    """

    a_file_filter               = file_filters.FFNameStartsWith( [   "__init", "_"  ]  )
    #FFExtList(   )  # might limit files to much include .py.....
    a_file_filter.include_true  = False

    # ---- directory filter

    # ------------------ dir filter
    # app_state.dir_filter_object       = file_filters.DFAll()   # default to DFAll() else you can

    #   _               eliminate _pycache..... as well as others
    #   old             eliminate my local version backup
    a_dir_filter                     = file_filters.DFNameStartsWith(  )
    a_dir_filter.list_of_starts_with = [ "old", "_", ".", "scratch"]
    a_dir_filter.include_true        = False


    return a_file_filter, a_dir_filter


#----------------------------------------------
def old_scratch_for_git_rshlib_for_git():
    """
    depth = 0 or 1 -- not in filter
    no readme_rsh.txt  ( would overwrite project's )

    may show how to make a multiple filter
    """

    # ------------------ file filter
    # app_state.dir_filter_object       = file_filters.DFAll()   # default to DFAll() else you can

    filter_object                     = file_filters.FFNameStartsWith(  )

    filter_object.list_of_starts_with = [ "_", "readme_rsh" ]
    filter_object.include_true        = False
    # what was this app_state.file_filter_object      = filter_object


    # doing a multiple one is a bit more work.
    # have to define both and use check file to combine,
    multiple_filter_object            = file_filters.FFMultipleFilters(  )


    filter_object                     = file_filters.FFNameStartsWith(  )
    filter_object.list_of_starts_with = [ "_",   ]
    filter_object.include_true        = False

    multiple_filter_object.filter_object_list.append( filter_object )

    filter_object                     = file_filters.FFNameStartsWith(  )
    filter_object.list_of_starts_with = [ "a",   ]
    filter_object.include_true        = False

    multiple_filter_object.filter_object_list.append( filter_object )


    def check_file( self, file_name, src_dir, dest_dir = "dest_dir defaulted" ):

        print( f"check_file external****  >>{self}<<, \n    >>{file_name}<<, \n    >>{src_dir}<<", flush = True)
        # reject if either filter fails

        dest_dir = ""
        filter_0   = self.filter_object_list[0].check_file(  file_name, src_dir, dest_dir )
        if not filter_0:
            return False

        filter_1   = self.filter_object_list[1].check_file(  file_name, src_dir, dest_dir )
        if not filter_1:
            return False

        return True

    # various experiments
    # multiple_filter_object.check_file   = check_file              # could not get to work
    #multiple_filter_object.check_file_implemented   = check_file   # did get to work
    multiple_filter_object.set_check_file( check_file )             # testing -- seems to work





    # then as always ( but multiple )
    # app_state.file_filter_object        = multiple_filter_object




