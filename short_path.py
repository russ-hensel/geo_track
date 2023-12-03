# -*- coding: utf-8 -*-
"""
Purpose:
    part of my ( rsh ) library of reusable code 
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.
"""

from pathlib import Path, WindowsPath, PosixPath



import os


import os
from   pathlib import _PosixFlavour
from   pathlib import _WindowsFlavour
import pathlib


class ShortPath:
    """
    not easy to subclass, this is the best I have found, use for
    now, test on linux, expect surprises
    oop - Subclass `pathlib.Path` fails - Stack Overflow
    https://stackoverflow.com/questions/29850801/subclass-pathlib-path-fails

    """

    def __init__(self, path, x = None ):
        self.path = pathlib.Path(path)
        self.base = None  # ;valid at time set or None
        ...

    def __getattr__(self, attr):
        return getattr(self.path, attr)

    # ------------------
    def set_base( self, base_for_path ):
        self.base    = Path( base_for_path )
        if self.base.exists():
            print( "base exists" )

        else:
            print( "base does not exists" )
            self.base  = None

    def get_short_name( self ):
        if self.base is None:
            return self.name

        if not self.name.startswith( self.base.name ):
            return self.name

        short_name = self.name[ 0:len( self.base.name )]

        return short_name

# class ShortPath( pathlib.Path ):
#     _flavour = type(pathlib.Path())._flavour


# class ShortPath(Path):
#     _flavour = _PosixFlavour() if os.name == 'posix' else _WindowsFlavour()

#     def __init__(self, *pathsegments: str):
#         super().__init__(*pathsegments)


# if os.name == 'posix':
#     base = PosixPath
# else:
#     base = WindowsPath

# class ShortPath(base):
#     def __init__(self, *pathsegments: str):
#         super().__init__(*pathsegments)



# class ShortPath(type(Path()), Path):  #
    # """
    # About this class.....
    # """
    # #----------- init -----------
    # def __init__(self, args ):
    #     """
    #     See class doc
    #     """
    #     #super().__init__( *args )
    #     #self.arg                   = arg
    #     # self._private              = 6
    #     # self.__mangled_private     = 9

    def __repr__(self):
        """
        the usual, read
        """
        return "ShortPath __repr__"

    # --------------------------------------------------
    def __str__( self ):
        """
        the usual, read
        """
        line_begin  = "\n    "  # formatting aid

        a_str       =  ""
        a_str       = f"{a_str}\n>>>>>>>>>>* ShortPath  *<<<<<<<<<<<<"
        a_str       = f"{a_str}{line_begin}self.name             >{self.name}<"  # {} recursive blows
        a_str       = f"{a_str}{line_begin}self.name             >{self.name}<"

        return a_str

    # -----------------------------------
    def _private(self):
        """
        what is says, read
        """
        ret_val = "_private"
        return ret_val



def test_short_path():
    #a_short_path    = ShortPath( r".\here.py" )

    a_short_path    = ShortPath( r"D:\Russ\0000\python00\python3\_projects\rshlib\file_filters.py" )


    print(f"a_short_path >{a_short_path}<")
    print(f"a_short_path.name >{a_short_path.name}<")
    a_short_path_r    = a_short_path.resolve()
    print(f"a_short_path_r... >{a_short_path_r}<")

    print( f"short_name    {a_short_path.get_short_name()}" )

    a_short_path.set_base( r"D:\Russ\0000\python00" )

    print( f"short_name    {a_short_path.get_short_name()}" )



test_short_path()


# ----------------------------------------
def show_path( a_string, resolve_it = False ):
    """
    helper to show path parts given a string name
    shows results of Pathlib attributes and functions
    this is also good example code for pathlib
    resolve_it = True will do most functions with the resolved file name
                 if the file does not exist then...
    """
    print( f"\nShow Path and its parts for a path built from {a_string} with resolve_it "
           "= {resolve_it} --------------" )
    a_path   = ShortPath( a_string )     # build from string
    print( f"a_path                 {a_path}" )

    if resolve_it:
        a_path   = a_path.resolve()
        print( f"a_path resolved to     {a_path}" )
        print(  "    --- if file does not reslove, nothing much happens")

    print( f"a_path                 {a_path}" )
    #-------------------------------+----------------
    print( f"a_path.name            {a_path.name}" )   #.name: the file name without any directory
    print( f"a_path.exists          {a_path.exists}" )
    print( f"a_path.parent          {a_path.parent}" )
    #-------------------------------+----------------
    # Get the Nth parent folder path mul_above = Path.cwd().parents[0]

    print( f"a_path.parents         {a_path.parents}" )
    print( f"len( a_path.parents )  {len(a_path.parents)}" )
    print( f"a_path.parents(2)      {a_path.parents[0]}" )   # may error out if does not exist
    #-------------------------------+----------------

    print( f"a_path.is_dir          {a_path.is_dir()}" )
    print( f"a_path.is_file         {a_path.is_file()}" )
    #-------------------------------+----------------
    print( f"a_path.name            {a_path.name}" )
        #.name: the file name without any directory
    print( f"a_path.stem            {a_path.stem}" )
        # .stem: the file name without the suffix
    print( f"a_path.suffix          {a_path.suffix}" )
        # .suffix: the file extension
    print( f"a_path.parts           {a_path.parts}" )
    print( f"a_path.anchor          {a_path.anchor}" )
        # the part of the path before the directories
    #-------------------------------+----------------

    #print( f"a_path.owner()          {a_path.owner()}")   # linux only
    print( f"a_path.stat()          {a_path.stat()}" )     # file must exist
    """
    # .parent: the directory containing the file, or the parent directory if path is a directory

    other mostly linux
    p.is_symlink()
    p.is_socket()
    p.is_fifo()
    p.is_block_device()
    p.is_char_device()
    p.owner()
    """

# ----------------------------------------
def ex_path_parts():
    """
    example code, see print and read code
    """
    ex_name  = "ex_path_parts"
    # print( f"{ex_helpers.begin_example( ex_name )} "
    #        f"\n    see parts of a path" )
    # see helper function show_path( ) for more pathlib example code

    show_path( r"./",       resolve_it  = True )
    show_path( r"D:\Russ\0000\python00\python3\_projects\rshlib\file_filters.py",       resolve_it  = True )


   # show_path( "ex_pathlib.pyxx", resolve_it  = True )


    # ex_helpers.end_example( ex_name )  # not part of example, marks end

# ex_path_parts()    # comment out this line to stop example from running

