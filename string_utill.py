# -*- coding: utf-8 -*-
"""
Purpose:
    part of my ( rsh ) library of reusable code
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.
"""

from pathlib import Path



# -----------------------------------------
class ColumnFormater( ):

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
        self.column_data   = []  # fill with tuples of the column dat
        self.column_specs  = []  # list of dicts as below in column order

        # a_spcec       =  { "width": 5,
        #                    "allign": "r",   # "l"
        #                     }

    # ----------------------------------------
    def get_default_spec(  self ):
        a_default_spec  =  { "width": 5,
                            "allign": "r",   # "l"
                             }
        return a_default_spec


    # ----------------------------------------
    def add_line( self, column_tuple  ):
        """
        what it says, read

        """
        pass
        self.column_data.append( column_tuple )
        # COULd check length against column specs

    # ----------------------------------------
    def add_column( self, column_spec ):
        """
        what it says, read

        """
        self.column_specs.append( column_spec )


    # ----------------------------------------
    def get_str( self,  ):
        """

        """

        a_str   = ""

        for i_line in self.column_data:
            a_str   = f"{a_str}\n"
            for ix_col, i_col_data in enumerate( i_line ):
                a_line  = ( i_col_data + "          " )[ 0: self.column_specs[ ix_col ]["width"] ]

        a_str   = f"{a_str} {a_line}"

            #for i_column_spec in self.column_specs
        return a_str

    #------------------
    def __str__( self, ):
        """
        Purpose:
           see title, what it says, read, for debug
        Return:
           a string of info about object
        Raises:
           none planned

        """
        newline  = "\n" + " " * 4
        a_str    = ""
        a_str    = f"{a_str}>>>>>>>>>>* ColumnFormatter (some values) *<<<<<<<<<<<<"
        #a_str    = ( f"{a_str}\n{self.__class__.__name__}: name = {self.name}" )
        # a_str    = f"super().__str__()"

        a_str    = f"{a_str}{newline}column_specs                {self.column_specs}"
        a_str    = f"{a_str}{newline}column_data                 {self.column_data}"

        # a_str    = f"{a_str}{newline}computer_id         {self.running_on.computer_id}"
        # a_str    = f"{a_str}{newline}logger_id           {self.logger_id}"

        return a_str



def test_column_formatter():
    """


    """
    a_column_formatter   = ColumnFormater()

    column_spec          = a_column_formatter.get_default_spec()
    a_column_formatter.add_column( column_spec )
    a_column_formatter.add_column( column_spec )

    a_line               = "name",   "john"
    a_column_formatter.add_line( a_line )
    a_line               = "name",   "sueellenjone"
    a_column_formatter.add_line( a_line )
    a_line               = "nm",   "johnthan"
    a_column_formatter.add_line( a_line )

    print( a_column_formatter )
    print( a_column_formatter.get_str() )


test_column_formatter()