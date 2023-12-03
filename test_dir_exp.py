# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:10:25 2023

@author: russ
"""

import sys

sys.path.append(  "../rshlib" )
sys.path.append(  "/media/sf_0000/python00/python3/_projects/rshlib" )


import file_filters
import dir_tree_explore

# create filter



#-------- file
file_filter_obj     = file_filters.FFExtList( ["db", "pdf", "ods" ],
                                             include_true = True,
                                             use_lower    = True )



#--------- directory
dir_filter_obj      = file_filters.DFAll()



# dir_filter_obj      = file_filters.DFNameStartsWith( [ "old" ],
#                                                      include_true   = False, #exclued iem in lis
#                                                     )


print( dir_filter_obj .demo_filter )



dir_tree_explorer   = dir_tree_explore.DirTreeExplorer()


dir_tree_explorer.file_filter        = file_filter_obj
dir_tree_explorer.directory_filter   = dir_filter_obj
dir_tree_explorer.max_dir_depth      = 0      # 0 is unlimited


start_search_at         = r"D:/Russ/0000/Utility"
start_search_at         = r"D:/Russ/0000/Farm"


dir_tree_explorer.explore_dir( start_search_at )

a_list    = dir_tree_explorer.file_list


print( a_list )