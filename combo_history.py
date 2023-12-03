# -*- coding: utf-8 -*-
"""
Purpose:
    part of my ( rsh ) library of reusable code 
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.
"""

# ---- imports
import  tkinter as tk

#from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font

#from demopanels import MsgPanel, SeeDismissPanel


import sys
sys.path.append( r"D:\Russ\0000\python00\python3\_examples" )
import ex_helpers



# ----------------------------------------
# class ExClass(object):
class ComboboxHistory( ttk.Combobox ):
    """
    combo box with a ddl of its history


    """

    # ----------------------------------------
    def __init__( self, parent, values = None, width  = None ):
        pass
        super().__init__( parent, values = values, width = width )
        """
          app, values=[
                                             "January",
                                             "February",
                                             "March",
                                             "April" ], width = 100 )

        """
        self.the_values    = values    # may already be available in widget
        self.get_var       = tk.StringVar()
        self.max_history   = 15

        self.config( height = self.max_history )

        self.config( textvariable  =  self.get_var )
        self.bind("<<ComboboxSelected>>", self.cb_selected )
        self.bind('<Return>', self.enter_event )   # return = enter key

    # ----------------------------------------
    def enter_event( self,  event ):
        """
        a function to explore events, not all may work

        """
        print( f"enter_event -> {event}")

    # ------------------------------
    def __str__( self ):

        a_str   = f"{self.__class__.__name__}: name = {self.name}"

        a_str   = f"{a_str}\n      xxx = {self._value_r}"
        # a_str   = f"{a_str}\n      cap        value = {self._value_c}"
        return a_str

    # ------------------------------
    def cb_selected_2( self,  evt ):
        """
        call back see which control attached to above
        should be on change or any value selected in the combobox

        """
        print( "cb_selected_2() replace with your callback" )

    # ------------------------------
    def cb_selected( self,  event ):
        """
        call back see which control attached to above
        should be on change or any value selected in the combobox

        """
        msg   = f"cb_selected >{event}<"
        print( msg )

        msg = f"cb_selected value is via get >{ self.get( ) }<"
        print( msg )

        msg = f"cb_selected value is via variable get >{ self.get_var.get( ) }<"
        print( msg )

        self.cb_selected_2( event )

    # --------------
    def get_text( self ):
        """
        Purpose:
            get the current text and add it to the history


        """
        current_text   = self.get().strip()
        print( f"get_text  current_text {current_text}" )
        if current_text == self.the_values[0]:
            return current_text

        self.the_values.insert( 0, current_text)

        if len( self.the_values  ) > self.max_history:
            self.the_values   = self.the_values[ :self.max_history ]   # or mutate it

        self.config( values = self.the_values )

        return current_text

# ----------------------------------------
def cb_for_get( event_or_object ):

        """
        call back see which control attached to above
        should be on change or any value selected in the combobox

        """
        msg   = f"cb_selected >{event_or_object}<"
        print( msg )

        a_widget   = event_or_object.widget
        msg = f"cb_selected value is via get >{ a_widget.widget.get( ) }<"
        print( msg )

        msg = f"cb_selected value is via variable get >{ a_widget.get_var.get( ) }<"
        print( msg )




# ----------------------------------------
def ex_combobox_history():
    ex_name  = "ex_of_a_class"
    print( f"{ex_helpers.begin_example( ex_combobox_history )}"
            "\n    see also introspection perhaps some should be there "
                )
    root = tk.Tk()
    root.geometry('700x100')  # w x h

    a_frame  = root

    ix_row   = 0
    ix_col   = 0

    labelTop       = tk.Label( a_frame, text = "Choose or type your favourite month")
    labelTop.grid( column= ix_col, row = ix_row )


    ix_col     += 1
    a_widget   = ComboboxHistory( a_frame, values=[
                                        "January",
                                        "February",
                                        "March",
                                        "April" ], width = 50 )


    a_widget.grid( column = ix_col, row = ix_row )
    a_widget.current( 2 )   # 0 is none selected ?

    combo_history_widget   = a_widget
    # comb_var      = tk.StringVar()
    # a_widget['state'] = 'readonly'

    # # set valus outside of declaration
    # a_widget.config( values = [ "one", "two", "three"] )


    #To re-enable editing the combobox, you use the 'normal' state like this
    #combobox['state'] = 'normal'

    # a_widget.config( textvariable  =  comb_var )   # use get, but works better in a class
    ix_row     = 2
    ix_col     = 0
    a_widget = ttk.Entry( a_frame ,    text = f"ttk.button" )
    #a_widget.configure( width        = 20, )
    a_widget.grid( row = ix_row, column = ix_col    )

    ix_col     += 1
    a_widget = ttk.Button( a_frame ,    text = f"ttk.button",  command = combo_history_widget.get_text  )
    a_widget.configure( width        = 20, )
    a_widget.grid( row = ix_row, column = ix_col    )

    # can we stop it from being edited ?
    # a_widget.bind( "<<ComboboxSelected>>", cb_function )

    root.mainloop()


    ex_helpers.end_example( ex_name )


ex_combobox_history()










