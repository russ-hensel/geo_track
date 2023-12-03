# -*- coding: utf-8 -*-
"""


but see make_file_filters.py





build file filters for other apps,
perhaps common use cases

may 2023 begin

look for code in backup directory_processor  file_processor file finder ....
    various copy to git ....


"""
"""

for git part 1 and 2


# ------------------ file filter
# app_state.dir_filter_object       = file_filters.DFAll()   # default to DFAll() else you can

filter_object                     = file_filters.FFNameStartsWith(  )

filter_object.list_of_starts_with = [ "_", "readme_rsh" ]
filter_object.include_true        = False
app_state.file_filter_object      = filter_object


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

# ------------------ dir filter
# app_state.dir_filter_object       = file_filters.DFAll()   # default to DFAll() else you can

filter_object                     = file_filters.DFNameStartsWith(  )
filter_object.list_of_starts_with = [ "old", "_", "."]
filter_object.include_true        = False


app_state.dir_filter_object       = filter_object   #

app_state.do_src_dest_match       = False   # default to True, you can change -- check source dest tails match

app_state.max_dir_depth           = 0   # default to -1   -1 is not limit to depth else what it says

#app_state.minus_dir                = 0    # default to 0 not sure what it means


#app_state.simulate_mode_flag    = self.parameters.simulate_mode_flag   # default in parameters -- True, no actually copy simulate

#app_state.log_skipped_flag      = self.parameters.log_skipped_flag     # default in parameters -- True, log when skipping a file

# # then as always ( but multiple )
# app_state.file_filter_object        = multiple_filter_object
a_file_filter, a_dir_filter         = make_file_filters.make_rshlib_for_git()

app_state.file_filter_object        = a_file_filter
app_state.dir_filter_object         = a_dir_filter

# ------------------ dir filter
# app_state.dir_filter_object       = file_filters.DFAll()   # default to DFAll() else you can

# filter_object                     = file_filters.DFNameStartsWith(  )
# filter_object.list_of_starts_with = [ "old", "_", "."]
# filter_object.include_true        = False


# app_state.dir_filter_object       = filter_object   #

app_state.do_src_dest_match         = False   # default to True, you can change -- check source dest tails match

app_state.max_dir_depth             = 0   # default to -1   -1 is not limit to depth else what it says

#app_state.minus_dir                = 0    # default to 0 not sure what it means


#app_state.simulate_mode_flag    = self.parameters.simulate_mode_flag   # default in parameters -- True, no actually copy simulate

#app_state.log_skipped_flag      = self.parameters.log_skipped_flag     # default in parameters -- True, log when skipping a file


# run it


"""
import file_filters

#----------------------------------------------
def make_backup_for_python():
    """

    File Filter   startsWith
        exclude
            "."               ide files, hidden  ( none ?)
            "scratch"         my scratch code


            *.log    but not with this filter

            *.vsis   what? but not with this filter

    use lower case   = True

    -----------------
    Dir Filter
        exclude
            "_"      __pycache
            "."      ide files

    use with ? depth = 0

    a_file_filter, a_dir_filter, depth   = file_fillter_builders.make_backup_for_python()

    """

    depth   = -1   # -1 is no limit


    # ---- directory filter
    a_dir_filter                        = file_filters.DFNameStartsWith( [ "_", "." ] )

    a_dir_filter.include_true           = False

    a_dir_filter.filter_description     = "a dir filter for python backup"

    #a_dir_filter.tail_only             = true

    a_dir_filter.demo_dir_names         =  [ "test",
                                                "old",
                                                "png.rar",
                                                r"g:\rat\Old",
                                                r"g:\rat\_reading",
                                                r"g:\rat\Oldish",
                                                r"g:\rat\.Rldish",
                                                "__pycache__",
                                                r"/etc",
                                                "_something"]


    #a_file_filter    = file_filters.FFAll()     #FFExtList(   )
    a_file_filter                    = file_filters.FFNameStartsWith( [  ".", "scratch",  ]  )

    a_file_filter.filter_description     = "a file filter for python backup"

    a_file_filter.include_true      = False

    a_file_filter.demo_file_names   =  [ "readme_rsh.txt",
                                             "readme.txt",
                                             "png.rar",
                                             ".joe.png",
                                             "code.py",
                                             "Xmen.txt",
                                             "__init__.py"]



    return a_file_filter, a_dir_filter, depth

# a_file_filter, a_dir_filter =  make_current_python_project_copy()



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
