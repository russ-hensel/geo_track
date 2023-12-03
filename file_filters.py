# -*- coding: utf-8 -*-
"""
Purpose:
    part of my ( rsh ) library of reusable code
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.

file_filters.py
file filters for directory exploration and backup and other uses of file selection

status:
    re factored from backup -- used in backup now, some working
    see tests for guide to use
    ** add abc ??
    has tests   ./tests

    Use:   see tests and each header and each demo
    file_filters.FFAll( )



used:
    backup
    filefinder
    structured notes
    ????

Ideas

    add fnmatch  .... module
    use regular expressions

    Python fnmatch Module Examples.

Docs:

    Python File Filters - SageMath for Undergraduates
    https://sagemathnotes.miraheze.org/wiki/Python_File_Filters#Example_Setup


"""

import os
import time
import operator
import datetime
import pathlib
# import src_stats
import stat

# -----------  file filter objects  FF_ -------------

#
# !! make so filters can filter on file size and date

# really should start with abc or with protocol -- used abc

import abc

# from abc import ABC, abstractmethod


# =============== compare functions =========

def less_than_or_equal( arg_1, arg_2 ):
    """
    this function will set the maximun size of
    file to be processed.

    Similiar functions are easily defined

    """
    return arg_1 <= arg_2

# ---------------------------
def get_compare_funtion_name( a_function ):
    if a_function == less_than_or_equal:
        return "less_than_or_equal"
    else:
        return "unknown"

# ================= Class =======================
class FFabc( abc.ABC ):
    """
    abstract class, in process for all file filters

    interface:
        self.demo_file_names   -- may replace or append
        self.filter_name
        self.filter_description
        self.list_of_contains

        self.include_true
        self.use_lower

        demo_filter()


    """
    # ----------------------------------------
    def __init__( self, ):
        """
        the usual

        """
        self.demo_file_names   =  [ "readme_rsh.txt",
                                    "read.txt",
                                    "read.txx",
                                    "png.rar",
                                    "png.png",
                                    "./clipboard/clipboard.sync-conflict-20230318-174551-ABEGZZ4.py_log"

                                    "xmen.xxx",
                                    "xmen.bmp",
                                    "xmen.mp4",
                                    "xmen.txt",
                                    "Xmen.txt",
                                    "__init__.py"] # was tuple but would like to append

        self.filter_name          = "FFabc"         # class name
        self.filter_description   = "see name"
        self.list_of_contains     = None

        self.include_true         = None
        self.use_lower            = None

    #-------------------------------------------
    def __str__(self):
        """
        the usual, read

        """

        a_str   = f"{self.filter_name}"
        a_str   = f"{a_str}\n    function_description   = {self.filter_description} "
        # a_str   = f"{a_str}\n    list_of_starts_with    = {self.list_of_starts_with}"
        a_str   = f"{a_str}\n    self.include_true      = {self.include_true}"
        a_str   = f"{a_str}\n    self.use_lower         = {self.use_lower}"

        return a_str

    #-------------------------------------------
    def check_file( self, file_name, src_dir = None, dest_dir = None  ):
        """
        use as a callback
        this is the call that actually 'does' the filtering
        for arguments look were called.
        file_name         just the file name clean off path keep the extension,
                             this is not checked
                             Or full file_name with scr_dir blank
        src_dir           the source path or directory ( first part of
                            full file name, often not used )
                            If None then assume file_name is full and break it up
        dest_dir          where the file is to be copied to,
                              not normally use but give a uniform call signature
        """




        return 1/0      # because this is abstract

    #-------------------------------------------
    def demo_filter( self, out_func = None  ):
        """
        out_func  = None then accumulate to a return strign
        """
        ret_msg   = "This is a demo of the file filter:\n"

        for i_file_name in self.demo_file_names:
            check_result   = self.check_file( i_file_name )
            msg = f"    file filter for >>{i_file_name}<< is >>{check_result}<<\n"
            if out_func is None:
                ret_msg  += msg
            else:
                out_func( msg )

        return ret_msg

# ================= class AllFiles =========================
class FFAll( FFabc ):
    """
    this is a filter object which accepts all file names
    !! what if the file is a directory, they should not be see check_file

    to build
    a_filter    =  file_filters.FFAll()

    """
    def __init__( self,  ):
        self.filter_name      = "FFAll"         # class name
        self.filter_function  = "accept all files"   # description of the function
        super().__init__()

    #-------------------------------------------
    def check_file( self, file_name, src_dir = None, dest_dir = None  ):
        """
        this is the call that actually 'does' the filtering
        for arguments look were called.
        """
        return True

    #-------------------------------------------
    def __str__(self):
        return self.filter_name   + " function = " + self.filter_function

# ================= class =========================
class FFExtList( FFabc ):
    """
    this is a filter object which accepts all file names on a list of extensions.
    No dot in extension argument  sample:  filter_object  =
         directory_backup.FFExtList( ["bat", "py"]  )
    we lower case the extension use this when you create your list
    example

    filter_obj          = file_filters.FFExtList( ["txt", "py" ],
                                                 include_true = True,
                                                 use_lower = True )
    a_filter_function   = filter_obj.check_file

    list_of_extensions  and other include true use_lower can be used as interface in out

    """
    def __init__( self,
                  list_of_extensions,
                  include_true        = True,
                  use_lower           = True ):
        super().__init__()
        self.filter_name          = "FFExtList"         # class name
        self.filter_description   = "accept based on list of extensions "
            # description of the function
        self.list_of_extensions   = list_of_extensions  # better if a set
        self.include_true         = include_true
        self.use_lower            = use_lower

    #-------------------------------------------
    def check_file( self, file_name, src_dir = None, dest_dir = None  ):
        """
        this is the call that actually 'does' the filtering
        for arguments -- look were called.
        """
        splits     = file_name.split( "." )
        ext        = splits[-1]
        if self.use_lower:
            ext    = ext.lower()   # end one, could be several, fix case

        is_ok         = False
        if ext in self.list_of_extensions:
            is_ok = True

        if self.include_true:
            pass
        else:
            is_ok  = not is_ok

        #msg = f"FFExtList check_file >>{file_name}<< >>{src_dir}<< >>{is_ok}<<"
        #rint( msg )

        return is_ok

    #-------------------------------------------
    def __str__(self):
        """
        !! needs more

        """
        # return self.filter_name   + " function = " + self.filter_function
        a_str   = f"{self.filter_name}       function_description =  {self.filter_description} "
        a_str   = f"{a_str}\n    list_of_extensions     = {self.list_of_extensions}"
        a_str   = f"{a_str}\n    use_lower              = {self.use_lower}"

        a_str   = f"{a_str}\n    include_true           = {self.include_true}"

        return a_str

# ================= class =========================
class FFNameEquals( FFabc ):
    """
    equals, could inclue extension or not
    if not using extension !! what does basename eval to??
    """
    def __init__( self,
                 list_of_equals = None,
                 include_true   = True,
                 use_lower      = True,
                 use_extension  = True ):


        super().__init__()
        self.filter_name          = "FFNameEquals"         # class name
        # self.filter_function      = "see name"   # description of the function --- removed
        self.filter_description   = "see name"
        if list_of_equals is None:
            self.list_of_equals   = []
        else:
            self.list_of_equals   = list_of_equals  # better if a set??

        self.include_true         = include_true
        self.use_lower            = use_lower
        self.use_extension        = use_extension

    #-------------------------------------------
    def check_file( self, file_name, src_dir = None, dest_dir = None  ):
        """
        this is the call that actually 'does' the filtering
        for arguments -- look were called.
        we need to get full path and then shorten it down...
        does the file need to exist
        !! add include path ??

        """
        check_name        = file_name
        check_name        = os.path.basename( check_name )    # path is gone, extension still there

        if self.use_lower:
            check_name    = check_name.lower()

        if not self.use_extension:
            splits         = check_name.rsplit( "." )   # ok for multiple "." ??
            check_name     = splits[0]
        print( f"check name = { check_name }")
        equals_to = False
        for i_string in self.list_of_equals:
            if self.use_extension:
                if i_string == check_name:
                    equals_to = True
                    break
            else:
                basename = os.path.basename( i_string )
                if basename  == check_name:
                    equals_to = True
                    break

        #  is this logic correct for both must match and cannot match,
        #    check this and the extension filter
        # ?? can compute this ??
        if self.include_true:
            ret = equals_to
        else:
            ret = not equals_to

        return ret

   #-------------------------------------------
    def __str__(self):

        a_str   = f"{self.filter_name}       function_description =  {self.filter_description} "
        a_str   = f"{a_str}\n    list_of_equals         = {self.list_of_equals}"
        a_str   = f"{a_str}\n    use_extension          = {self.use_extension}"
        a_str   = f"{a_str}\n    self.include_true      = {self.include_true}"
        a_str   = f"{a_str}\n    self.use_lower         = {self.use_lower}"

        return a_str


# ================= class =========================
class FFNameContains( FFabc ):
    """
    what it says
    check the contents of the file name
    interface includes ( but some best used from initializer )
         filter_name
         filter_description
         include_true

    """
    def __init__( self, list_of_contains = None, include_true = True, use_lower = True ):
        super().__init__()
        self.filter_name          = "FFNameContains"         # class name
        self.filter_description   = "see name"
        if list_of_contains is None:
            self.list_of_contains = []
        else:
            self.list_of_contains = list_of_contains

        self.include_true         = include_true
        self.use_lower            = use_lower

        # test in particular for this filter
        self.demo_file_names.append( "./clipboard.sync-conflict-20230318-174551-ABEGZZ4.py_log" )

    #-------------------------------------------
    def check_file( self, file_name, src_dir = None, dest_dir = None  ):
        """
        this is the call that actually 'does' the filtering
        for arguments -- look were called.
        we need to get full path and then shorten it down...
        does the file need to exist

        """
        basename = os.path.basename( file_name )
            # !! is the file name the whole thing, does it
            #  include src_dir if no can this work?

        if self.use_lower:
            basename    = basename.lower()

        contains_flag = False
        for i_string in self.list_of_contains:
            #if basename.contains( i_string ):
            if i_string in basename:
                contains_flag = True
                break

        if self.include_true:
            ret = contains_flag
        else:
            ret = not contains_flag

        return ret

        #-------------------------------------------
        def __str__(self):

            a_str   = self.super().__str__()
            # a_str   = f"{a_str}\n    list_of_starts_with    = {self.list_of_starts_with}"
            a_str   = f"{a_str}\n    self.include_true      = {self.include_true}"
            a_str   = f"{a_str}\n    self.use_lower         = {self.use_lower}"

            return a_str

# =================
class FFNameStartsWith( FFabc ):
    """
    what it says
    check the beginning of the file name
    """
    def __init__( self, list_of_starts_with = None, include_true = True, use_lower = True ):
        super().__init__()
        self.filter_name          = "FFNameStartsWith"         # class name
        # self.filter_function      = "see name"   # description of the function --- removed
        self.filter_description   = "see name"
        if list_of_starts_with is None:
            self.list_of_starts_with = []
        else:
            self.list_of_starts_with  = list_of_starts_with  # better if a set

        self.include_true         = include_true
        self.use_lower            = use_lower

    #-------------------------------------------
    def check_file( self, file_name, src_dir = None, dest_dir = None  ):
        """
        this is the call that actually 'does' the filtering
        for arguments -- look were called.
        we need to get full path and then shorten it down...
        does the file need to exist

        """
        basename = os.path.basename( file_name )
            # !! is the file name the whole thing, does it
            #  include src_dir if no can this work?

        if self.use_lower:
            basename    = basename.lower()

        starts_with = False
        for i_string in self.list_of_starts_with:
            if basename.startswith( i_string ):
                starts_with = True
                break

        if self.include_true:
            ret = starts_with
        else:
            ret = not starts_with

        return ret

    #-------------------------------------------
    def __str__(self):
        """
        the usual, read

        """

        a_str   = f"{self.filter_name}       function_description =  {self.filter_description} "
        a_str   = f"{a_str}\n    list_of_starts_with    = {self.list_of_starts_with}"
        a_str   = f"{a_str}\n    self.include_true      = {self.include_true}"
        a_str   = f"{a_str}\n    self.use_lower         = {self.use_lower}"

        return a_str

# ================= class =========================
class FFSize( FFabc ):
    """
    This is a filter object which excludes/includes based on size  large files
    based on what criteria -- lets rebuild file name and get all file data


    """
    def __init__( self,  size,  compare_true_operator     ):
        self.filter_name            = "FFSize"
        self.filter_function        = f"exclude large files based on size = {size}"
        self.filter_description     = f"{self.filter_name} with function = {get_compare_funtion_name( compare_true_operator )} "
        self.size                   = size
        self.compare_true_operator  = compare_true_operator
        super().__init__()

    #-------------------------------------------
    def check_file( self, file_name, src_dir, dest_dir  ):
        """
        this function checks a file name, in this one
        Args: same as other FF
        doe we combine src_dir with file_name if present ?!!

        """
        print( "!! unfinished/tested")

        # src_stats   = os.stat( file_name )
        # msg         = f"in check_file src_stats {src_stats}"
        # print( msg )

        file_size          = os.stat( file_name ).st_size

        a_check    = self.compare_true_operator( file_size, self.size )

        return a_check

    #-------------------------------------------
    def __str__(self):

        a_str   = f"{self.filter_name}       function_description =  {self.filter_description} "
        a_str   = f"{a_str}\n    size                   = {self.size}"
        #a_str   = f"{a_str}\n    use_extension          = {self.use_extension}"
        #a_str   = f"{a_str}\n    self.include_true      = {self.include_true}"
        #a_str   = f"{a_str}\n    self.use_lower         = {self.use_lower}"

        return a_str

    #self.filter_name   + " function = " + self.filter_function

# ================= class =========================
class FFExcludeAll( FFabc ):
    """
    This is a filter object which excludes all files.  For debugging  --- but mostly make no sense

    """
    def __init__( self,  ):
        self.filter_name      = "FFExcludeAll"
        #self.filter_function  = "exclude all files, give debug info "
        self.filter_description   = "exclude all files, give debug info "

    #-------------------------------------------
    def check_file( self, file_name, src_dir = None, dest_dir = None  ):
        """
        this function checks a file name, in this one
        Args:
            file_name  full file name with path: D:/Russ/0000/python00
                  /python3/_projects/backup/TestSource/Sub0/Sub2/file2_2.txt
            src_dir    all source      path up to be not including final /
                D:/Russ/0000/python00/python3/_projects/backup/TestSource/Sub0/Sub2
            dest_dir   all destination path up to be not including final /
                D:/Russ/0000/python00/python3/_projects/backup/TestDest/TestSource/Sub0/Sub2<

        note we may have mixed /  and \
        """
        msg    = ( f"in check_file file_name {file_name} \n    src_dir >{src_dir}<\n"
                   f"   dest_dir >{dest_dir}<" )
        print( msg )

        src_stats          = os.stat( file_name )
        msg    = f"in check_file src_stats {src_stats}"
        print( msg )

        msg    = (     f"file name:             {file_name} \n" +
                        f"Size in bytes:        {src_stats[stat.ST_SIZE]} \n" +
                        f"Last access:          {time.ctime( src_stats[stat.ST_ATIME] ) } \n" +
                        f"Last modification:    {time.ctime( src_stats[stat.ST_MTIME] ) } \n" +
                        f"Last status:          {time.ctime( src_stats[stat.ST_CTIME] ) } \n" +
                        f"User id of the owner: {src_stats[stat.ST_UID]} \n" +
                        f"Group id of the owner:{src_stats[stat.ST_GID ]} \n" +

                        ""
                )

        print( msg )

        splits = file_name.split( "." )
        ext    = splits[-1].lower()   # end one, could be several??, fix case !!
        msg    = f"in check_file ext {ext}"
        print( msg )

        return False

# ================= class =========================
class FFADate( FFabc ):
    """
    !! looks like not done
    this is a filter object which accepts files with a single extension
    extension is not case sensitive
    for windows may be ok on others
    """
    def __init__( self, date_string = None ):
        self.filter_name      = "FFADate"
        self.filter_function  = "error extension not set"
        self.timestamp        = None
        super().__init__()
        if date_string is None:
            self.date_string      = ""
        else:
            self. date_string           = date_string

        self.relation         = operator.lt
           # default can be set file < adate
           #  <, < = !=    import operator f_op    = operator.lt
        self.set_date( date_string )

    #-------------------------------------------
    def set_date( self, date_string ):
        """
        what it says, read
        return
           mutates self.

        """
        a_format              = "%d/%m/%Y"
        self.timestamp        = time.mktime( datetime.datetime.strptime( date_string,
                                                            a_format ).timetuple() )
        self.date_string      = date_string
        self.set_filter_function()

    #-------------------------------------------
    def set_relation( self, a_relation ):
        """
        what it says, read


        """
        # looks like wip not working
        self.relation         =  a_relation
        self.set_filter_function()

    #-------------------------------------------
    def set_filter_function( self, ):
        """
        need doc, is used ??

        """
        # looks like wip
        self.filter_function  = ( "file date " + " relation " + str( self.relation )
                 + self.date_string + " files only" )

#    #-------------------------------------------
    def check_file( self, file_name, src_dir = None, dest_dir = None ):
        """
        usual sort of check file, read it
        """

        stats = os.stat( file_name )
        #rint "stats are",file1,stats[8]
        modified   = stats[8]
        print("in check file")
        a_check    = self.relation( modified, self.timestamp )
        #return True
        print( "Adate check " + file_name + " " + str( a_check ), flush = True )

        #return ( self.relation( modified, self.timestamp ) )
        return a_check

    #-------------------------------------------
    def __str__(self):

        if self.timestamp is None:
            self.filter_function  = "error extension not set"

        ret  = self.filter_name   + " function = " + self.filter_function
        return ret

# ================= class =========================
class FFMultipleFilters( FFabc ):
    """
    !!   mostly done

    see test

    """
    #-------------------------------------------
    def __init__( self,   ):
        super().__init__()
        self.filter_name         = "FFMultipleFilters"
        self.filter_description  = "combine multiple filters"
        self.filter_object_list  = []

    #-------------------------------------------
    def _check_file_implemented( self, file_name, src_dir, dest_dir  ):
        """
        this function needs to be replaced, my standard way of doing this
        seems to result in a function call without replace so we do it as in
        ?? can we change to a property
        """
        msg     =  ( f"***check_file_implemented internal stub should be replaced"
                     f"  >>{self}<<, \n    >>{file_name}<<, \n    >>{src_dir}<<" )
        print( msg, flush = True)

    #-------------------------------------------
    def set_check_file( self, check_file_function  ):
        """
        what it says, read
        ?? replace with a property
        """
        self._check_file_implemented  = check_file_function

    #-------------------------------------------
    def check_file( self, file_name, src_dir, dest_dir  ):
        """
        needs to be set from outside ...
        could consider call by key word
        see  check_file_implemented
        """
        msg     =   f"check_file internal >>{self}<<, \n    >>{file_name}<<, \n    >>{src_dir}<<"
        print( msg, flush = True)

    #-------------------------------------------
    def __str__(self):
        """
        basic, more work

        """
        a_indent   = "\n    "
        a_str      = f"{self.filter_name}       function_description =  {self.filter_description} "

        for ix, i_filter in enumerate( self.filter_object_list ):
            a_str   = f"{a_str}{a_indent}   {ix}    = {i_filter}"

            # a_str   = f"{a_str}\n    self.include_true      = {self.include_true}"
            # a_str   = f"{a_str}\n    self.use_lower         = {self.use_lower}"
        return a_str

# ---- Directories =========================
class DFabc( abc.ABC ):
    """
    this is a filter object which accepts all directory names
    leaving in dest_dir for now
    add filter name ??

    """
    def __init__( self,
         list_of_starts_with = None,
         include_true        = True,
         use_lower           = True,
         tail_only           = True,
         ):


        if list_of_starts_with is None:
            self.list_of_starts_with = []
        else:
            self.list_of_starts_with  = list_of_starts_with  # better if a set

        self.include_true         = include_true
        self.use_lower            = use_lower
        self.tail_only            = tail_only

        self.max_depth            = None    # new interface to pass arg
        """
        # pref to current set
        if max_depth is None:
            max_depth  = dir_filter.max_depth
            if max_depth is None:
                1/0

                ----
        # pref to filter
        if dir_filter.max_depth is not None:
            max_depth = dir_filter.max_depth
        """

        # have one for win one for unix
        self.demo_dir_names   =  ( "not finished yet ",
                                    r"f:\readme_rsh",
                                    r"g:\rat\old",
                                    r"g:\rat\Old",
                                    r"g:\rat\reading",
                                    r"g:\rat\Oldish",
                                    r"g:\rat\Rldish",
                                    r"/etc",   )



        #rint( "DFabc __init__" )

    #-------------------------------------------
    def demo_filter( self, out_func = None  ):
        """
        demo filter action
        out_func  = None then accumulate to a return string
                    jor print, or out to gui.....
        """
        ret_msg   = ""

        for i_dir_name in self.demo_dir_names:
            check_result   = self.check_dir( i_dir_name )
            msg = f"dir filter for >>{i_dir_name}<< is >>{check_result}<<\n"
            if out_func is None:
                ret_msg  += msg
            else:
                out_func( msg )

        return ret_msg

    #-------------------------------------------
    def check_dir( self,   src_dir = None, dest_dir = None  ):
        """
        this is the call that actually 'does' the filtering
        for arguments look were called.
        src_dir = this is the full path from a root or drive letter,
            no trailing / -- may not be normalized to / from \ so do it in functions
        """
        # msg       = f"DFAll check_dir 1 {src_dir}"
        # print( msg )
        # src_dir    = src_dir.replace( "\\", "/")
        # # if we want just the tail then
        # splits    = src_dir.rsplit( "/", 1 )
        # print( splits )
        # src_dir   = splits[1]
        # msg       = f"DFAll check_dir 2 {src_dir}"
        # print( msg )

        return True

    #-------------------------------------------
    def check_file( self, file_name, src_dir, dest_dir  ):
        """
        to unifiy with file filter
        needs to be set from outside ...
        could consider call by key word
        see  check_file_implemented
        """
        msg     =   ( f"check_file internal >>{self}<<, "
                      f"\n    >>{file_name}<<, "
                      f"\n    >>{src_dir}<<" )
        print( msg, flush = True)

        is_ok    = self.check_dir( src_dir, dest_dir )


        #sg    = f"in check_file file_name {file_name} \n
        #       src_dir >{src_dir}<\n    dest_dir >{dest_dir}<"

        return is_ok
# --------------------------
class DFAll( DFabc ):
    """
    this is a filter object which accepts all directory names
    leaving in dest_dir for now

    """
    def __init__( self,
                  list_of_starts_with = None,
                  include_true        = True,
                  use_lower           = True,
                  tail_only           = True,
                  ):
        """
        Arguments: see DFabc

        """
        super().__init__(  list_of_starts_with = list_of_starts_with,
                           include_true        = include_true,
                           use_lower           = use_lower,
                           tail_only           = tail_only,)


        self.filter_name         = "DFAll"         # class name
        self.filter_description  = "accept all directories "   # description of the function


    #-------------------------------------------
    def check_dir( self,   src_dir = None, dest_dir = None  ):
        """
        this is the call that actually 'does' the filtering
        for arguments look were called.
        src_dir = this is the full path from a root or drive letter,
            no trailing / -- may not be normalized to / from \ so do it in functions
        """
        # msg       = f"DFAll check_dir 1 {src_dir}"
        # print( msg )
        # src_dir    = src_dir.replace( "\\", "/")
        # # if we want just the tail then
        # splits    = src_dir.rsplit( "/", 1 )
        # print( splits )
        # src_dir   = splits[1]
        # msg       = f"DFAll check_dir 2 {src_dir}"
        # print( msg )

        return True

    #-------------------------------------------
    def __str__(self):
        return f"{self.filter_name}       function_description =  {self.filter_description} "

#-------------------------------------------
class DFNameStartsWith(  DFabc ):
    """
    directory filter -- very similar to file filter but think needs seperate code
    !! need to strip off the dir id like D:   may be a pathlib, or look for :
        ... prob not as tail_only = True



    """
    def __init__( self,
                  list_of_starts_with = None,
                  include_true        = True,
                  use_lower           = True,
                  tail_only           = True,
                  ):
        """

        Arguments:
            list_of_starts_with = list of strings that are to be used in checking
            include_true        = True True means include, passed the filter ok
                                      otherwise logic reversed
            use_lower           = True make lower case prior to check
            tail_only           = True only tail end, last peice of directory is checked



        """
        super().__init__( list_of_starts_with   = list_of_starts_with,
                            include_true        = include_true,
                            use_lower           = use_lower,
                            tail_only           = tail_only,)

        self.filter_name          = "DFNameStartsWith"         # class name
        self.filter_description   = "see name"     # description of the function

    #-------------------------------------------
    def check_dir( self, src_dir = None, dest_dir = None  ):
        """
        this is the call that actually 'does' the filtering
        for arguments -- look were called.

        """
        org_scr_dir    = src_dir
        #msg       = f"DFNameStartsWith check_dir 1 {src_dir}"
        #rint( msg )

        src_dir    = src_dir.replace( "\\", "/")

        if self.use_lower:
            src_dir    = src_dir.lower()

        # next sees to be able to be done in two ways
        if self.tail_only:
            # if we want just the tail then
            splits    = src_dir.rsplit( "/", 1 )
            #rint( splits )
            if len( splits ) > 1:
                src_dir     = splits[1]
            else:
                pass
                # src_dir     = ""   # so wrong
            #final_name  = src_dir
            # msg       = f"DFNameStartsWith check_dir 2 {src_dir}"
            #rint( msg )
            # discarding this
            # src_dir         = pathlib.PureWindowsPath( src_dir ).parts[-1]
        print( f"org_scr_dir {org_scr_dir} => src_dir >{src_dir}<")
        starts_with = False
        for i_string in self.list_of_starts_with:
            #rint( f"{i_string} starts with >{src_dir}< ??")
            if src_dir.startswith( i_string ):
                #rint( "starts_with True" )
                starts_with = True
                break
        #rint( f"self.include_true {self.include_true}")

        if self.include_true:
            ret = starts_with
        else:
            ret = not starts_with
        return ret

    #-------------------------------------------
    def __str__(self):
        a_str   = f"{self.filter_name}       function_description =  {self.filter_description} "
        # a_str   = f"{a_str}\n    list_of_starts_with    = {self.list_of_starts_with}"
        a_str   = f"{a_str}\n    include_true           = {self.include_true}"
        a_str   = f"{a_str}\n    use_lower              = {self.use_lower}"
        a_str   = f"{a_str}\n    tail_only              = {self.tail_only}"
        a_str   = f"{a_str}\n    list_of_starts_with    = {self.list_of_starts_with}"


        return a_str

# ================= class =========================
class DFMultipleFilters( FFabc ):
    """
    !!   mostly done

    see test

    """
    #-------------------------------------------
    def __init__( self,   ):
        self.filter_name         = "DFMultipleFilters"
        self.filter_description  = "combine multiple filters"
        self.filter_object_list  = []

    #-------------------------------------------
    def _check_dir_implemented( self, src_dir, dest_dir  ):
        """
        this function needs to be replaced, my standard way of doing this
        seems to result in a function call without replace so we do it as in
        ?? can we change to a property
        """
        msg     =  ( f"***check_file_implemented internal stub should be replaced"
                      f"  >>{self}<<, \n    >>{src_dir}<<, \n    >>{dest_dir}<<" )

        print( msg, flush = True)
        1/0

    #-------------------------------------------
    def set_check_dir( self, check_file_function  ):
        """
        what it says, read
        ?? replace with a property
        """
        print( "set_check_dir changing _check_file_implemented")
        self._check_dir_implemented  = check_file_function

    #-------------------------------------------
    def check_dir( self, src_dir, dest_dir  ):
        """
        needs to be set from outside ...
        could consider call by key word
        see  check_file_implemented
        """
        # msg     =   f"check_file internal >>{self}<<, \n    >>{src_dir}<<, \n    >>{dest_dir}<<"
        #rint( msg, flush = True)

        # this odd call seems to be required by the injection of the function externally
        ret  =self._check_dir_implemented( self      = self,
                                          src_dir   = src_dir,
                                          dest_dir  = dest_dir )

        return ret

    #-------------------------------------------
    def __str__(self):
        """
        basic, more work

        """
        a_indent   = "\n    "
        a_str      = f"{self.filter_name}       function_description =  {self.filter_description} "

        for ix, i_filter in enumerate( self.filter_object_list ):
            a_str   = f"{a_str}{a_indent}   {ix}    = {i_filter}"


        return a_str

# -----------  End Dir Filters   -------------

# ================= class =========================
class FDFMultipleFilters(   ):
    """
    file and dir filter use to make multiples
    do not want to use multiple inheret so
    will pull code from ansestors

    see test

    when making multiple filter need to be careful not to mix up logic in your head


    """
    #-------------------------------------------
    def __init__( self,   ):
        super().__init__()
        self.filter_name         = "FFMultipleFilters"
        self.filter_description  = "combine multiple filters"
        self.filter_object_list  = []

    #-------------------------------------------
    def _check_file_implemented( self, file_name, src_dir, dest_dir  ):
        """
        this function needs to be replaced, my standard way of doing this
        seems to result in a function call without replace so we do it as in
        ?? can we change to a property
        """
        msg     =  ( f"***check_file_implemented internal stub should be replaced"
                     f"  >>{self}<<, \n    >>{file_name}<<, \n    >>{src_dir}<<" )
        print( msg, flush = True)

    #-------------------------------------------
    def set_check_file( self, check_file_function  ):
        """
        what it says, read
        ?? replace with a property
        """
        self._check_file_implemented  = check_file_function

    #-------------------------------------------
    def check_file( self, file_name, src_dir, dest_dir  ):
        """
        needs to be set from outside ...
        could consider call by key word
        see  check_file_implemented
        """
        msg     =   f"check_file internal >>{self}<<, \n    >>{file_name}<<, \n    >>{src_dir}<<"
        print( msg, flush = True)

    #-------------------------------------------
    def check_dir( self,   src_dir = None, dest_dir = None  ):
        """
        this is the call that actually 'does' the filtering
        for arguments look were called.
        src_dir = this is the full path from a root or drive letter,
            no trailing / -- may not be normalized to / from \ so do it in functions
        """
        # msg       = f"DFAll check_dir 1 {src_dir}"
        # print( msg )
        # src_dir    = src_dir.replace( "\\", "/")
        # # if we want just the tail then
        # splits    = src_dir.rsplit( "/", 1 )
        # print( splits )
        # src_dir   = splits[1]
        # msg       = f"DFAll check_dir 2 {src_dir}"
        # print( msg )

        return True

    #-------------------------------------------
    def __str__(self):
        """
        basic, more work

        """
        a_indent   = "\n    "
        a_str      = f"{self.filter_name}       function_description =  {self.filter_description} "

        for ix, i_filter in enumerate( self.filter_object_list ):
            a_str   = f"{a_str}{a_indent}   {ix}    = {i_filter}"

            # a_str   = f"{a_str}\n    self.include_true      = {self.include_true}"
            # a_str   = f"{a_str}\n    self.use_lower         = {self.use_lower}"
        return a_str

    #-------------------------------------------
    def demo_filter( self, out_func = None  ):
        """
        out_func  = None then accumulate to a return strign
        """
        ret_msg   = ""

        for i_file_name in self.demo_file_names:
            check_result   = self.check_file( i_file_name )
            msg = f"file filter for >>{i_file_name}<< is >>{check_result}<<\n"
            if out_func is None:
                ret_msg  += msg
            else:
                out_func( msg )

        return ret_msg


# ==================== eof ============