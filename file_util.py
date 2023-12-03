# -*- coding: utf-8 -*-
"""
Purpose:
    part of my ( rsh ) library of reusable code 
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.
"""

from pathlib import Path

# ----------------------------------------
def increment_extension( a_path, new_ext = None ):
    """
    rename file in a_path  .... increment its extension
    good to 90ish files
    increments first 2 characters in extension ( if not numbers, extends the extensin )
    read the code
    the file itself need to exist makes sence that it should
    nameing here sucks
    will do a rename of the original file to a higher number
        original file will be gone under original name

    arguments:
        a_path    an existing file's path object
        new_ext   a new extension for the numbered rename of the file no . vis not .vis
            ?? should I look and strip
            if None will increment on the current extension

    return:
        mutated file system,
        and new extenson or None if fails

    include file_util
    file_util.increment_extension( a_path )

    """
    if not a_path.exists():
        #?? perhaps an exception
        return None   # cannot increment a non existant file

    # next for debug
    a_path_less_suffix   = Path.joinpath( a_path.parent, a_path.stem )
    print( f"a_path_less_suffix   {a_path_less_suffix}" )

    if isinstance( new_ext, str ) and new_ext.startswith( "." ):
        msg   = f"new_ext  >{new_ext}< starts with a . -- we will remove for now"
        print( msg )
        new_ext         = new_ext[1:]

    if new_ext is None:
        suffix          = a_path.suffix
        num             = suffix[ 1:3 ]   # skip . get next two char
        suffix_suffix   = suffix[ 3: ]
    else:
        suffix          = new_ext          # bak  ->  00bak
        num             = 0
        suffix_suffix   = new_ext

    try:
        num            = int( num )
    except Exception as a_exception:           # !! be more specific for nan
        num            = 0
        suffix_suffix  = suffix[ 1:]
        #rint( f"no num at first 2 car in extension set suffix_suffix to {suffix_suffix}" )

    while True:
        num = num + 1
        if num > 98:
            raise Exception( )  # fix for which one

        new_suffix         = f".{num:0>2}{suffix_suffix}"   #  add . pad suffix for new suffix
        #rint( new_suffix )

        a_rename_path      = a_path.with_suffix(  new_suffix  )  # setup for rename

        if a_rename_path.exists():
            pass
            # loop again because this file is already taken
        else:
            #rint( a_rename_path )
            a_path.rename( a_rename_path )
            return ( num, str( a_rename_path ) )
            # break
    return ( num, str( a_rename_path ) )  # think this is a fail or what

# ------------------- helper
def find_directory( a_path, do_resolve = False ):
    """
    given a path find the directory ( which is the path if it exists )
    if not a directory move up one level and see if that

    see rshlib

    Returns:
        path of the directory or None


    """
    if a_path.exists() and a_path.is_dir():
        if do_resolve:
            # un-necessary to have 2 steps, just if you want to debug
            a_r_path    = a_path.resolve( )
            a_path      = a_r_path
        return a_path

    # strip one level and check again

    a_new_path  = a_path.parent
    #rint( f"a_new_path = {a_new_path}" )
    if a_new_path.exists() and a_new_path.is_dir():
        # un-necessary to have 2 steps, just if you want to debug
        a_r_path    = a_new_path.resolve( )
        a_new_path      = a_r_path
        return a_new_path
    # else return None
    return None   # to make pylint happy

# -----------------------------------------
class FileDeleter( ):

    """
    a_file_deleter    = FileDeleter( )
    a_file_deleter.do_delete_empty( a_path )

    what_deleted     = a_file_deleter.delete_list

    ?? consider adding an output print function to display the progress

    """
    def __init__(self,   ):
        """
        what it says, read

        """
        ...
        self.reset( None )

    # ----------------------------------------
    def reset( self, a_path ):
        """
        reset for reuse


        """
        self.current_depth   = 0
        self.top_path        = a_path
        self.delete_list     = []

    # ----------------------------------------
    def do_delete_empty( self, a_path ):
        """
        start and do the delete process

        """
        self.reset( a_path )
        self._delete_empty_dir_from( a_path )

    # ----------------------------------------
    def add_to_delete_list( self, a_path ):
        """
        what it says, read

        """
        resolved   = a_path.resolve( )
        self.delete_list.append( resolved )

    # ----------------------------------------
    def _delete_empty_dir_from( self, a_path ):
        """
        starting at a_path recurse to bottom and delete
        all empty directories on the way up
        return True if now empty
        """
        print( f"\n\njust_entered delete_dir_from for {a_path}  depth = {self.current_depth }" )
        #found_sub_dir       = True
        is_empty            = True    # change as soon as we cannot deletes a sub or find a file
        # dir_paths           = []
        file_paths          = []
        dir_paths           = []
        ix_paths            = 0
        #found_sub_dir       = False
        self.current_depth += 1
        for child in a_path.iterdir():
            ix_paths  += 1
            if child.is_dir():
                if  self._delete_empty_dir_from( child ):

                    print( f"dir empty >>{child}<<   delete *****************")
                    child.rmdir()
                    self.add_to_delete_list( child )
                    #  is_empty  unchanged
                    print( f"{child} is dir {child.is_dir()} and exists {child.exists()}" )
                    #found_sub_dir   = True
                    dir_paths.append( child )
                else:
                    print( "dir not empty++++++++++++")
                    is_empty   = False
            else:
                file_paths.append( child )
                is_empty  = False   # because we have a file

        self.current_depth -= 1
        #rint( f"file_paths   {file_paths}")
        #rint( f"dir_paths   {dir_paths}")
        #rint( f"ix_paths    {ix_paths}")
        #rint( f"exit {a_path}")

        return is_empty




