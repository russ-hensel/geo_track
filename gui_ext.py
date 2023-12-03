#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Purpose:
    part of my ( rsh ) library of reusable code
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.

Various classes to extend tkinter functionality
     browsers
     message frames
     and styling of widgets

make a title property to set the title on the fly??

master in rsh_lib, gui_ext

us sys path for development, then copy over file and edit for git hub

sys.path.append( "../rshlib" )
import gui_ext

AppGlobal is needed to run this,
look for links
        .parameters
        .logger


"""

# perhaps lazy import better
import tkinter as tk
from   tkinter.filedialog import askopenfilename
from   tkinter.filedialog import askdirectory
# from   tkinter.messagebox import showinfo
import tkinter.ttk as ttk
from   tkinter            import messagebox

import os
#import  sys
#from   tkinter import ttk
#from   tkinter.scrolledtext import ScrolledText
# import pyperclip

from   app_global import AppGlobal
# for above to work need to have an AppGlobal in the dir
# where app was started, or provide another in this dir
# seems to work

#---------------------
def bring_to_top( root_frame  ):
    """
    What it says, read code
    """
    #rint( f"bring_to_top() {__name__}"  )

    # ---- ---- method one, did not work ?
    # self.root.attributes('-topmost', 1)
    # self.root.attributes('-topmost', 0)  # else it will stay on top as a pain

    # method 2
    root_frame.iconify()
    root_frame.update()
    root_frame.deiconify()

#---------------------
def set_icon( root_frame, icon_fn  ):
    """
    What it says, read code -- tested in linux, may be differnt in win see my apps
    if it fails kill the consol and restart
    """
    img         = tk.PhotoImage( file = icon_fn )
    root_frame.wm_iconphoto( False, img )

#---------------------
def minimize_gui( root_frame  ):
    """
    What it says, read code
    """
    #rint( f"bring_to_top() {__name__}"  )

    # method 2
    root_frame.iconify()
    #root_frame.update()
    #root_frame.deiconify()

#---------------------
def about(  controller  ):
    """
    interfaces with controller and called back from gui
    What it says, read code
            url   =  r"comming soon not at http://www.opencircuits.com/TBD"
        __, mem_msg   = cls.show_process_memory( )
        msg  = f"{cls.controller.app_name}  version:{cls.controller.version} \n  by Russ Hensel\n  Memory in use {mem_msg} \n  Check <Help> or \n     {url} \n     for more info."
        messagebox.showinfo( "About", msg,  )   #   tried ng: width=20  icon = "spark_plug_white.ico"

    """
    __, mem_msg = AppGlobal.show_process_memory( )
    msg         = ( f"{ controller.app_name}  version:{ controller.app_version}"
                    f"\n  by Russ Hensel"
                    f"\n  Memory in use {mem_msg} "
                    f"\n  Check <Help> or "
                    f"\n  {controller.app_url} \n"
                   )

    messagebox.showinfo( "About", msg,  )   #   tried ng: width=20  icon = "spark_plug_white.ico"


# -----------------------------------------
class FileBrowseWidget( tk.Frame ):
    """
    let user pick a file name on their computer
    not sure why making it into a widget is a good idea but here goes
    this is a widget that both holds a filename
    and lets you browse to a file
    how is it different from just a couple of widgets
    in your frame ... more reusable ?
    better looking or what
    see graph_smart_plug gui for a use
    !! code is duplicated in 2 guis, this should be fixed

    Tkinter Dialogs — Python 3.9.6 documentation
    https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog

    need an example interface to this

    build it and keep a reference
        a_bw     = FileBrowseWidget( a_parent )
    get the text from it
        a_bw.get_text()     and set_text()

    use some instance variables to set browse behaviour
        a_bw.initialdir    = "./",
        a_bw.title         = "Select file for db",
        a_bw.filetypes     = (("database files","*.db"),("all files","*.*"))

    """
    def __init__(self, parent, entry_width  = None, ):
        super(  ).__init__( parent,
                            width           = 60,
                            height          = 20,

                            # bg ="red",
                            bg = "gray", )

        if entry_width is None:
            entry_width = 100

        a_widget      = tk.Label( self, text="Get File Name:", anchor = "e")
        a_widget.grid( row = 1, column = 0, sticky = tk.N + tk.S )
        AppGlobal.gui_style.style_widget( a_widget )
        a_widget.config( width  = 35 )
        self.label_widget = a_widget        # use for access say with config er ?

        self.a_string_var = tk.StringVar()

        self.entry_1      = tk.Entry( self ,
                                      width         = entry_width,
                                      text          = "bound",
                                      textvariable  = self.a_string_var )
        #AppGlobal.gui_style.style_widget( self.entry_1 )
        self.entry_1.grid( row=1, column=1 , sticky = tk.N + tk.S )

        self.button_2     = tk.Button( self, text = "Browse...", command = self.browse )
        #AppGlobal.gui_style.style_widget(  self.button_2 )
        self.button_2.grid( row=1, column=3 )

        self.initialdir    = "./"
        self.title         = "Select file for db"
        self.filetypes     = ( ("all files","*.*"), ("database files","*.db"),)

    # ------------------------------------------
    def browse( self ):
        """
        browse for a file name
        return full path or "" if no file chosen
        """
        tk.Tk().withdraw()
        filename     = askopenfilename(  initialdir   = self.initialdir,
                                         title        = self.title ,
                                         filetypes    = self.filetypes )

        if filename == "":
            return

        self.set_text( filename )
        #rint( f"get_text = {self.get_text()}", flush = True )

    # ------------------------------------------
    def set_text( self, a_string ):
        """
        get the text from the entry
        """
        self.a_string_var.set( a_string )

    # ------------------------------------------
    def get_text( self, ):
        """
        get the text from the entry
        """
        a_string   =  self.a_string_var.get(  )
        return a_string

# -----------------------------------------
class DirBrowseWidget( tk.Frame ):
    """
    let user pick a directory name on their computer
    Tkinter Dialogs — Python 3.9.6 documentation
    https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog

    test in /test/test_browse
    """
    def __init__(self,
                   parent,
                   initialdir   = None,
                   browse_title = None,
                   width        = 60,
                   height       = 20):

        super(  ).__init__( parent, width = width, height = height, bg ="red")
        a_widget      = tk.Label( self, text="Get Directory Name:", anchor = "e" )
        #AppGlobal.gui_style.style_widget(  a_widget )
        a_widget.grid( row = 1, column = 0, sticky = tk.N + tk.S )
        a_widget.config( width  = 35 )
        self.label_widget  = a_widget

        self.a_string_var  = tk.StringVar()

        self.entry_1       = tk.Entry( self ,
                                      width         = 100,
                                      text          = "bound",
                                      textvariable  = self.a_string_var ) #  height = 20 ng

        #AppGlobal.gui_style.style_widget( self.entry_1 )
        self.entry_1.grid( row = 1, column = 1, sticky = tk.N + tk.S )

        self.button_2 = tk.Button( self, text = "Browse...", command = self.browse )
        AppGlobal.gui_style.style_widget(  self.button_2 )
        self.button_2.grid( row = 1, column = 3 )

        self.initialdir    = initialdir     # part of interface perhaps
        self.browse_title  = browse_title   # part of interface perhaps

    # ------------------------------------------
    def browse( self ):
        """
        browse for a file name
        return full path or "" if no file chosen
        """

        # initialdir=expanduser(pathvar.get()),
        # (parent=root,
        #                           initialdir="/path/to/start",
        #                           title='Please select a directory')

        tk.Tk().withdraw()
        dirname   = askdirectory( initialdir = self.initialdir,
                                  title      = self.browse_title )
        #rint( f" dir name >{dirname}< {type(dirname)}" )
        if dirname != "":
            self.set_text( dirname )
        #rint( f"get_text = {self.get_text()}", flush = True )

    # ------------------------------------------
    def set_text( self, a_string ):
        """
        get the text from the entry
        """
        self.a_string_var.set( a_string )

    # ------------------------------------------
    def get_text( self, ):
        """
        get the text from the entry
        """
        a_string   =  self.a_string_var.get(  )
        return a_string

# ----------------------------------------
class MessageFrame( tk.Frame ):
    """

    need to add or make new class to be an edit window
         get rid of buttons
         get all text programatically
         make ctrl-c -v work
    message frame used in so many apps

        a_frame            = gui_ext.MessageFrame( parent,  )
        self.message_frame = a_frame
        return a_frame

    Interface
         functions
         self.max_lines
         self.msg_text
         self.button_widgets
         do_clear_button()
         print_string()


    """
    def __init__(self, parent, gui_style = None ):
        #super( BrowseWidget, self ).__init__( parent, width=60, height=20, bg ="red")
        super(  ).__init__( parent, width = 60, height = 20, bg ="yellow")
        self.max_lines          = 10000      # part of interface
        self.gui_style          = gui_style
        self.button_widgets     = []

        a_frame          = self._make_message_frame( parent,  )

    # ------------------------------------------
    def _make_message_frame( self, parent, default_scroll = True  ):
        """
        default_scroll is new
        make the message frame
        return of i_frame is just self
        why is parent not used !!
        """
#        color   = "black"   # this may need a bit of rework -- looks like not used
        #iframe  = tk.Frame( parent, width=300, height=800,
        #    bg ="blue", relief = tk.RAISED, borderwidth=1,  )
        iframe  = self

        # bframe is for the buttons on the left
        bframe  = tk.Frame( iframe, bg = "white", width=30  )
            # width=300, height=800, bg ="blue", relief=RAISED, borderwidth=1,  )
        bframe.grid( row=0, column=0, sticky = tk.N + tk.S )

        text0   = tk.Text( iframe , width=50, height = 20  )

        s_text0 = tk.Scrollbar( iframe  )
        s_text0.grid( row=0, column=2, sticky = tk.N + tk.S )

        s_text0.config( command=text0.yview )
        text0.config( yscrollcommand = s_text0.set )

        text0.grid( row=0, column=1, sticky = tk.N + tk.S + tk.E + tk.W  )

        self.msg_text  = text0      # really a widget i think

        iframe.grid_columnconfigure( 1, weight=1 )
        iframe.grid_rowconfigure(    0, weight=1 )

        # now into the button frame bframe

        # spacer
        s_frame = tk.Frame( bframe, bg ="green", height=20 ) # width=30  )
        s_frame.grid( row=0, column=0  )
        row_ix   = 0

        # ---- Clear button
        b_clear = tk.Button( bframe , width=10, height=2, text = "Clear" )
        b_clear.bind( "<Button-1>", self.do_clear_button )
        # if self.gui_style:
        #     self.gui_style.style_button( b_clear )
        b_clear.grid( row=row_ix, column=0   )

        self.button_widgets.append( b_clear )
        row_ix   += 1

        # ---- Copy selection
        a_widget = tk.Button( bframe , width=10, height=2, text = "Cop Selection",
                            command = self.copy_selection)
        # b_temp.bind( "<Button-1>", self.doButtonText )
        # if self.gui_style:
        #     self.gui_style.style_button( a_widget )
        a_widget.grid( row=row_ix, column=0   )
        self.button_widgets.append( a_widget )
        row_ix   += 1

        #-----
        a_widget = tk.Button( bframe , width=10, height=2, text =  "Copy All" )
        a_widget.bind( "<Button-1>", self.do_copy_button )
        # if self.gui_style:
        #     self.gui_style.style_button( a_widget )
        a_widget.grid( row = row_ix, column = 0   )
        self.button_widgets.append( a_widget )
        row_ix += 1

        # -------------
        self.cb_scroll_var  = tk.IntVar()  # for check box in reciev frame
        a_widget = tk.Checkbutton( bframe,
                                   width    = 7,
                                   height   = 2,
                                   text     = "A Scroll",
                                   variable = self.cb_scroll_var,
                                   command  = self.do_auto_scroll )

        a_widget.grid( row=row_ix, column=0   )
        self.button_widgets.append( a_widget )

        row_ix += 1
        self.cb_scroll_var.set( default_scroll ) # was AppGlobal.parameters.default_scroll )

        return iframe

    # ------------------------------------------
    def do_auto_scroll( self, auto = True  ):
        """
        still configured so needed, but will not work ??
        pass, not needed, place holder see
        """
        print( "do_auto_scroll fix !!" )

    # ------------------------------------------
    def do_clear_button( self, event):
        """
        for the clear button
        clear the message area
        """
        self.clear_message_area()

    # ------------------------------------------
    def clear_message_area( self,   ):
        """
        what it says.....message area sometimes rec or send
        """
        self.msg_text.delete( 1.0, tk.END )

    # ------------------------------------------
    def get_all_text( self, ):
        """
        copy All text to the clipboard
        !! seems commented out
        """
        #rint( " do_copy_button -- this is all  ")
        #data  = self.msg_text.get( 1.0, tk.END )
        data = "is this the error"
        return data

    # ------------------------------------------
    def do_copy_button( self, event ):
        """
        copy All text to the clipboard
        """
        #rint( " do_copy_button -- this is all  ")
        data  = self.msg_text.get( 1.0, tk.END )
        pyperclip.copy( data )

    # ------------------------------------------
    def copy_selection( self, ):
        """
        copy selected  text to the clipboard
        """
        try:
            data  = self.msg_text.get( "sel.first", "sel.last" )
            pyperclip.copy( data )
        except Exception as exception:  # if no selection
            pass

    # ---------------  end of button actions and class
    # ---------------------------------------
    def print_string( self, a_string,
                     plus_newline    = True,
                     title           = "",
                     clear           = False,
                     update_now      = False ):
        """

        msg_frame.print( a_string _  )
        print to message area, with scrolling and
        log if we are configured for it
        should we have a prefix, or just do in the call?? or gui
        parameters.gui_text_log_fn    = False  # "gui_text.log"       # a file name or something false

        parameters.log_gui_text       = False # True or false to log text
        parameters.log_gui_text_level = 10    # logging level for above

        a_string,
        plus_newline,
        title = "",
        clear = False,
        update_now = False
        plus_newline

        """
        if  AppGlobal.parameters.gui_text_log_fn:
            # for now open close.... later perhaps improve
            with open( AppGlobal.parameters.gui_text_log_fn, "a"  ) as a_file:
                a_file.write( a_string )   # do we need \n check
                #rint(   a_string )

        if  AppGlobal.parameters.log_gui_text:
            AppGlobal.logger.log( AppGlobal.parameters.log_gui_text_level, a_string, )

        if clear:
            self.clear_message_area()

        if  title != "":
            self.msg_text.insert( tk.END, title, )

        if plus_newline:
            a_string = a_string + "\n"

        # now the meat
        self.msg_text.insert( tk.END, a_string, )      # this is going wrong, why how

        # limit the number of lines
        try:
            numlines = int( self.msg_text.index('end - 1 line').split('.')[0] )
                # !! beware int( None ) how could it happen ?? it did this is new
        except Exception as exception:
            # look in logs to find
            msg  = f"MessageFrame, indexing exception {exception}"
            AppGlobal.logger.error( msg )
            print( msg )
            numlines = 0

        if numlines > self.max_lines:
            cut  = int( numlines/2  )    # lines to keep/remove
            self.msg_text.delete( 1.0, str( cut ) + ".0" )               # remove excess text
#            msg     = "Delete from test area at " + str( cut )
#            self.logger.info( msg )

        # auto scroll
        if self.cb_scroll_var.get():
            self.msg_text.see( tk.END )

        if update_now:
            AppGlobal.gui.root.update()
            print( "!! self.root not valid here ")

    # ---------------------------------------
    def display_string( self, a_string, update_now = False ):
        """
        !! we may phase out for print_string
        print to message area, with scrolling and
        log if we are configured for it

        parameters.gui_text_log_fn    = False  # "gui_text.log"
                                               # a file name or something false

        parameters.log_gui_text       = False # True or false to log text
        parameters.log_gui_text_level = 10    # logging level for above

        !! add parameter clear_msg = True or false

        """
        #rint( "debug for display_string")
        if  AppGlobal.parameters.gui_text_log_fn:
            # for now open close.... later perhaps improve
            with open( AppGlobal.parameters.gui_text_log_fn, "a"  ) as a_file:
                a_file.write( a_string )   # do we need \n check
                #rint(   a_string )

        if  AppGlobal.parameters.log_gui_text:
            AppGlobal.logger.log( AppGlobal.parameters.log_gui_text_level, a_string, )

        self.msg_text.insert( tk.END, a_string, )      # this is going wrong, why how
        try:
            numlines = int( self.msg_text.index( 'end - 1 line' ).split('.')[0] )
                # !! beware int( None ) how could it happen ?? it did this is new
        except Exception as exception:
        # Catch the custom exception -- !! to broad execpt
            AppGlobal.logger.error( str( exception ) )
            print( exception )
            numlines = 0
        if numlines > self.max_lines:
            cut  = int( numlines/2  )    # lines to keep/remove
            self.msg_text.delete( 1.0, str( cut ) + ".0" )               # remove excess text
#            msg     = "Delete from test area at " + str( cut )
#            self.logger.info( msg )

        if self.cb_scroll_var.get():
            self.msg_text.see( tk.END )

        if update_now:
            AppGlobal.gui.root.update()
            print( "!! self.root not valid here ")

# ----------------------------------------
class ListboxScroll( ):
    """
    scrolling listbox with title and utility functions
    master in rsh_lib, gui_ext

    consider making descandant of Frame

    note that self.   hold components for possible use

    so far single selection
    How to interface
        use functions
            .....
        access
            self.listbox       to access any pure listbox attributes
            self.outer_frame   to place the frame

    """
    def __init__( self, parent_frame, a_title = "a title", width = None, height = None ):
        """
        if title is None do not construct that part

        """
        self.version        = "2021_08_04"
        self.parent         = parent_frame
        self.title          = a_title
        self.click_function = None     # set later or externally
        self.frame          = None     # the frame this is in use xxx.frame
        self.listbox        = None     # the listbox
        self.outer_frame    = None

        if width is None:
            width = 100

        if height is None:
            height = 100

        self._make_titled_listbox_( width, height )

    # ----------------------------------------
    # """
    # functions needed
    # set command  -- just a property ... no needs function could make a propeety @
    # inset_row
    # """
    # ----------------------------------------
    def insert_row( self, value ):
        """
        what is says
        """
        self.listbox.insert(  tk.END, value )

     # ----------------------------------------
    def clear_rows( self,  ):
        """
        what is says
        """
        self.listbox.delete( 0, tk.END )

    # ----------------------------------------
    def set_values( self, values ):
        """
        what is says
        can we use to clear set list without using insert row
        """
        #self.listbox.configure( values )
        # clear
        #for

    # ----------------------------------------
    def set_width( self, width ):
        """
        what is says -- read
        """
        # label seems to be the controlling thing
        self.label_widget.configure( width = width )

    # ----------------------------------------
    def set_height( self, height ):
        """
        what is says -- read
        """
        # label seems to be the controlling thing
        self.listbox.configure( height = height )
        print( "!! implement set_height if not working" )

    # ----------------------------------------
    def set_click_function( self, a_function ):
        """
        what is says -- would bind be better
        we want an index or contents of row or both need
        more work here
        """
        self.click_function =  a_function

    # ------------------
    def _click_function( self, event ):
        """
        what is says -- would bind be better -- on the list box?, search
        we want an index or contents of row or both need
        more work here
        """
        if self.click_function is None:
            print( "ListboxScroll -- click_function not set" )
        else:
            # sending the selection get, but perhaps should
            #    send the event and let click function ....!!!
            # a_key   = event.widget.selection_get()
            #rint( a_key )
            # self.click_function( a_key )
            self.click_function( event )

    # ------------------
    def get_row_text( self, a_index ):
        """
        if ix not valid then ?? return None

        """
        if self.listbox.size() >= a_index:
            a_value  = self.listbox.get( a_index )
        else:
            a_value  = None

        return a_value

    # ------------------
    def get_selected_ix( self ):
        """
        return 0 based selection -1 if nothing
        assumes in single select mode
        """
        selected_ix   = self.listbox.curselection()

        if selected_ix == tuple(  ):
            selected_ix  = -1
        else:
            selected_ix  =  selected_ix[0]   # since we allow only 1 selection

        return selected_ix

    # ----------------------------------------
    def _make_titled_listbox_( self, width, height  ):
        """
        make a frame ( at top will become self.outer_frame )
        in it a listbox ( self.listbox )
        and a scrollbar
        and a label


        for snips and snippets?
        return ( famelike_thing, listbox_thing)  ?? make a class, better access to components
        """
        a_frame       = tk.Frame( self.parent, width = 1000 )

        # new sept  2022 dos it help or break

        a_frame.grid_rowconfigure(    0, weight = 0 )
        a_frame.grid_rowconfigure(    1, weight = 1 )
        a_frame.grid_rowconfigure(    1, weight = 1 )

        a_frame.grid_columnconfigure( 0, weight = 1 )
        a_frame.grid_columnconfigure( 1, weight = 0 )



        a_label = tk.Label( a_frame, text = self.title, width = width )
        a_label.grid( column = 0, row = 0, sticky=( tk.N, tk.E, tk.W) )
        self.label_widget  = a_label

        a_listbox     = tk.Listbox( a_frame, height = 5 )
        self.listbox  = a_listbox
        a_listbox.grid( column = 0, row = 1, sticky=( tk.N, tk.W, tk.E, tk.S ) )

        a_listbox.bind( "<<ListboxSelect>>", self._click_function  )

        a_scrollbar = tk.Scrollbar( a_frame,
                                    orient    = tk.VERTICAL,
                                    command   = a_listbox.yview)

        a_scrollbar.grid( column=1, row=1, sticky = ( tk.N, tk.W, tk.E, tk.S ) )   # (tk.N, tk.S)
        a_listbox[ 'yscrollcommand'] = a_scrollbar.set

        # for overall widget
        self.set_width( width  )
        self.set_height( height )

        self.listbox     = a_listbox
        self.frame       = a_frame
        self.outer_frame = a_frame

        return a_frame

# -----------------------------------
class PlaceInGrid( ):
    """
    called sequentially to help layout grids in a row and column format
    columnspan=2, rowspan=2
    add columnspan to place  make it increment in direction we are moving ....??

    to do
    add column span row span -- keep delta ? delta is span in direction, but may need both ?
    add setup for stickyness ??

    placer    = gui_ext.PlaceInGrid( 99,  by_rows = True )
    placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

    """
    def __init__( self,  a_max = 0, by_rows = True  ):
        """

        Args:
                a_max, may want to change to by name and default to 0 which is unlimited
                by_rows  --- require name ?? default

        """
        self.max      = a_max
        self.ix_row   = 0
        self.ix_col   = 0     # ix_col   += 1 to move across one
        self.sticky   = tk.W + tk.E  + tk.N + tk.S
        self.by_rows  = by_rows
        if by_rows:
            self.function =  self._place_down_row_
        else:
            self.function =  self._place_across_col_

    # -----------------------------------
    def place( self,
               a_widget,
               columnspan   = None,
               rowspan      = None,
               sticky       = None  ):
        """
        move row or column by delta grid spacings after pacing control
        what is row span vs deltac
        args:
            widget     -> the widget being placed
            columnspan -> the column span
            rowspan    -> the rowspan
            sticky     -> temporary override of sticky via argument
        """
        if columnspan is None:
            columnspan = 1

        if rowspan is None:
            rowspan    = 1

        #app_global.print_debug( f"row,co = {self.ix_row}, {self.ix_col}" )
        self.function( a_widget,  columnspan = columnspan, rowspan = rowspan, sticky = sticky )

    # -----------------------------------
    def _place_down_row_( self, a_widget, columnspan, rowspan, sticky = None ):
        """
        one of the value intended for self.function
        does its name
        not much tested
        need to add sticky
        """
        #print( "_place_down_row_ still need to make sticky stick !!")
        if sticky is None:
            self.sticky = sticky

        #rint( f"_place_down_row_ row = {self.ix_row} col = {self.ix_col}"  )
        a_widget.grid( row          = self.ix_row,
                      column        = self.ix_col,
                      rowspan       = rowspan,
                      sticky        = sticky,  )

        self.ix_row += rowspan
        if ( self.max > 0  ) and ( self.ix_row >= self.max ):
            print( f"hit max row {self.max}"  )
            self.ix_col    += 1
            self.ix_row     = 0

    # -----------------------------------
#    delta_row_col( delta_row, delta_col )
#    add a span argument
    # -----------------------------------
    def new_column( self, delta = 1,  ):
        """
        start a new column in row 0
        for going down columns not aacross

        """
        self.ix_row     = 0
        self.ix_col     += delta

    # -----------------------------------
    def new_row( self, delta_row = 1,  ):
        """
        start a new row in col 0
        !! also for col
        """
        self.ix_row     += delta_row
        self.ix_col      = 0

    # -----------------------------------
    def set_row( self, row,  ):
        """
        what if beyond max
        """
        self.ix_row = row

    # -----------------------------------
    def set_col( self,  col ):
        """
        what it says, why not just the property

        """
        self.ix_col = col

    # -----------------------------------
    def _place_across_col_( self, a_widget, *, columnspan,  rowspan, sticky, ):
        """
        what it says
        one of the value intended for self.function
        args:
            widget     -> the widget being placed
            columnspan -> the column span
            rowspan    -> the rowspan
            sticky     -> temporary override of sticky via argument
        """
#        print( f"_place_across_col_ row = {self.ix_row} col = {self.ix_col}"  )
        # defaulting should be done in place
        # if columnspan is None:
        #     columnspan = 1

        # if rowspan is None:
        #     rowspan = 1

        if sticky is None:
            sticky = self.sticky

        #rint( f"_place_across_col_ ({self.ix_col}, {self.ix_row})"
        #                               f"columnspan = {columnspan}" )

        a_widget.grid( row          = self.ix_row,
                       column       = self.ix_col,
                       columnspan   = columnspan,
                       rowspan      = rowspan,
                       sticky       = sticky,  )

        self.ix_col += columnspan
        if ( self.max > 0  ) and ( self.ix_col >= self.max ):
            print( f"hit max row {self.max}"  )
            self.ix_row += 1
            self.ix_col  = 0

        #print("_place_across_col_",  self.ix_row, self.ix_col  )

"""
GUI utilities, right now for gui build later ?

module or object or mix,

i tend to go with objects so we will do an
instantiated object


import gui_util

self.a_gui_util    = gui_util.GuiUtil()
self.a_gui_util.style_button( a_widget )

"""

# ======================= begin class ====================
class GuiStyle( ):
    """
    for consistent styles in the gui from structured notes now in
        rhsutil master and copy to each project
    gui utilities for the application
    another AppGlobal thing
     str>><class 'tkscrolledframe.widget.ScrolledFrame'><<
          repr >><tkscrolledframe.widget.ScrolledFrame object .!




    You can use a string specifying the proportion of red, green and blue in hexadecimal digits.
    For example, "#fff" is white, "#000000" is black, "#000fff000" is pure green, and "#00ffff"
    is pure cyan (green plus blue).
    You can also use any locally defined standard color name.
    The colors "white", "black", "red", "green", "blue", "cyan", "yellow", and "magenta" will always be available.

    paint net
        save as
            save button
              hover    e3f1fb
              capture  e1e1e1

    """
    def __init__( self, style_type = None, font = None ):
        """
        register with AppGlobal: a requirement

        """
        AppGlobal.gui_style  = self   #!! not int AppGlobal but use as a_gui_util

        self.widget_style_dispactch_dict   = {} # used in imports

        #rint( f"init GuiStyle" )

        if style_type == "linux":  # getting self not defined ??
            import linux_style_type
            linux_style_type.set_style_type( self )

        elif style_type == "none":  # getting self not defined ??
            import none_style_type
            none_style_type.set_style_type( self )

        else:
            import windows_style_type
            windows_style_type.set_style_type( self )

    # ------------------------------------------
    def make_styles_from_parameters( self, a_parameter = None ):
        pass  # ?? and idea

    # ------------------------------------------
    def make_styles_from_widget( self, a_widget ):
        """
        ?? an idea
        """
        pass

    # ------------------------------------------
    def style_widget( self, a_widget ):
        """
        what it says   !! do we need ** seem to work without it
        returns:
            mutates the widget
        !! possibly use isinstance, but may need to be applied in
            just the right order for now use type
        !! change to dict type of dsipatch  ...
            started see self.style_dispacth_dict ... then put in dict use one function
        """
        widget_type = type( a_widget )

        if  widget_type  == tk.Label:
            self.style_label( a_widget )
        # elif  widget_type == class( 'tkinter.Button' ):

        elif  widget_type == tk.Button:
            #rint( "  type widget tk.Button" )
            self.style_button( a_widget )

        elif  widget_type == tk.Entry:
            #rint( "  type widget tk.Entry" )
            self.style_entry( a_widget )

        elif  widget_type == tk.Frame:
            #rint( "  type widget tk.Entry" )
            self.style_frame( a_widget )

        elif  widget_type == tk.LabelFrame:
            #rint( "  type widget tk.Entry" )
            self.style_labelframe( a_widget )

        elif  widget_type == tk.Checkbutton:
            #rint( "  type widget tk.Entry" )
            self.style_checkbutton( a_widget )

        elif  widget_type == ttk.Combobox:
            #rint( "  type widget tk.Entry" )
            self.style_combobox( a_widget )

        else:
            #rint( "******************** no dispacth for this type widget" )
            print( f".style_widget -- no dispatch  str>>{widget_type}<<"
                   f"   repr >>{repr( a_widget)}<<" )

    # ------------------------------------------
    def style_button( self, a_widget ):
        """
        what it says   !! do we need ** seem to work without it
        returns:
            mutates the button
            add height ??
        """
        a_widget.config( self.button_dict )
        #print( "problem  with fg in styling look into " )

        # if True:    # old style without dict  -- configure or config
        #     pass
        #     # for testing without dict windows only green and red seem to ever show
        #     a_widget.configure( activebackground ='red' )
        #     a_widget.configure( activeforeground ='blue' )
        #     a_widget.configure( bg               ='green' )
        #     a_widget.configure( fg               ='yellow' )
        #     a_widget.configure( highlightcolor   ='orange' )


    # ------------------------------------------
    def style_frame( self, a_widget ):
        """
        what it says
        returns:
            mutates the frame
        """
        a_widget.config( self.frame_dict )

    # ------------------------------------------
    def style_labelframe( self, a_widget ):
        """
        what it says
        returns:
            mutates a_widget

        """
        print( "running style_labelframe")
        a_widget.config( self.labelframe_dict )

    # ------------------------------------------
    def style_tabp( self, a_widget ):
        """
        what it says
        returns:
            mutates the tab page
        """
        a_widget.config( self.tabp_dict )

    # ------------------------------------------
    def style_label( self, a_widget ):
        """
        what it says
        returns:
            mutates the label
        """
        a_widget.config( self.label_dict )

    # ------------------------------------------
    def style_checkbox( self, a_widget ):
        """
        what it says
        returns:
            mutates the label
        """
        a_widget.config( self.checkbox_dict )

    # ------------------------------------------
    def style_checkbutton( self, a_widget ):
        """
        what it says
        returns:
            mutates the label
        """
        a_widget.config( self.checkbutton_dict )

    # ------------------------------------------
    def style_combobox( self, a_widget ):
        """
        what it says
        returns:
            mutates the widget ... but combo boxes are special
        """
        print( "style_combobox implementation problems" )
        #a_widget.config( self.combobox_dict )

    # ------------------------------------------
    def style_entry( self, a_widget ):
        """
        what it says
        returns:
            mutates the widget = an entry
        """
        a_widget.config( self.entry_dict )

    # ------------------------------------------
    def style_radio_button( self, a_widget ):
        """
        what it says
        returns:
            mutates the widget = an entry

            activeforeground    The foreground color when the mouse is over the radiobutton.
            anchor              If the widget inhabits a space larger than it needs,
                                this option specifies where the radiobutton will sit in that space.
                                The default is anchor=CENTER.
            bg                  The normal background color behind the indicator and label.
            bitmap              To display a monochrome image on a radiobutton,
                                set this option to a bitmap.

        """
        #rint( "style_radio_button" )
        a_widget.config( self.radio_button_dict )

# --------------------------------------
class TitledFrame(  ):
    """
    new not tested
    About this class.....
    make a color coded frame ( two frames one above the other )
    with a title in the top one and color coded
    see ex_tk_frame.py for the master
    """
    #----------- init -----------
    def __init__( self, a_parent_frame,
                  a_title,
                  a_title_color,
                  button_width = 10,
                  button_height = 2 ):
        """
        Usual init see class doc string
        add to gui_ext !!
        """
        a_frame      = tk.Frame( a_parent_frame,
                                 # bg ="red",
                                 bg = "gray", )

        a_frame.rowconfigure(    0, weight= 1 )
        a_frame.rowconfigure(    1, weight= 1 )

        a_frame.columnconfigure( 0, weight= 1 )
        #master.columnconfigure( 1, weight= 1 )
        self.frame      = a_frame
        p_frame         = a_frame

        a_frame  = tk.Frame( p_frame,   bg = a_title_color, )
            # padx = 2, pady = 2, relief= tk.GROOVE, )
        a_frame.grid( row = 0,  column = 0 ,sticky = tk.E + tk.W )
        self.top_inner_frame    = a_frame

        a_label             = tk.Label( a_frame,
                                        text    = a_title,
                                        bg      = a_title_color ,  )
                                     #   relief = RAISED,  )
        a_label.grid( row = 0, column = 0, )
            # columnspan = 1, sticky = tk.W + tk.E )

        a_frame  = tk.Frame( p_frame,   )
            # bg = "blue", )  # use neutral color or the title color
            # padx = 2, pady = 2, relief= tk.GROOVE, )
        a_frame.grid( row = 1,  column = 0,sticky = tk.E + tk.W )
        self.bottom_inner_frame    = a_frame

        self.button_width  = button_width
        self.button_height = button_height
        self.button_row    = 0
        self.button_column = 0

    #----------------------------------------------------------------------
    def make_button( self, button_text = "default text", command = None ):
        """
        !! have function make the button with the command
        !! may not be best way to do, may just want to return inner frame
        """
        a_button = tk.Button( self.bottom_inner_frame ,
                             width     = self.button_width,
                             height    = self.button_height,
                             text      = button_text )
        a_button.grid( row  = self.button_row, column = self.button_column )
        self.button_column += 1

        if command is not None:
            a_button.config( command = command  )

        return a_button

#----------------------------------------------------------------------
def make_titled_listbox( parent_frame, a_title ):
    """
    for snips and snippets?
    return ( famelike_thing, listbox_thing)  ?? make a class, better access to components
    widget like built in its own frame
    """
    a_frame      = tk.Frame(parent_frame)
    a_listbox    = tk.Listbox( a_frame, height = 5 )
    a_listbox.grid( column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S) )
    s = tk.Scrollbar( a_frame, orient=tk.VERTICAL, command=a_listbox.yview)
    s.grid( column=1, row = 1, sticky = (tk.N, tk.S ))
    a_listbox['yscrollcommand'] = s.set
    a_label = tk.Label( a_frame, text= a_title )
    a_label.grid( column=0, row=0, sticky=( tk.N, tk.E, tk.W) )
    #  tk.Sizegrip().grid(column=1, row=1, sticky=(tk.S, tk.E)) size grip not appropriate here
    a_frame.grid_columnconfigure( 0, weight=1 )
    a_frame.grid_rowconfigure(    0, weight=0 )
    a_frame.grid_rowconfigure(    1, weight=1 )
    return ( a_frame, a_listbox )

# both of these in use !! why or explain

    #----------------------------------------------------------------------
    def make_button( self, button_text = "default text", command = None ):
        """
        !! have function make the button with the command
        or is this just unreachable
        """
        a_button = tk.Button( self.bottom_inner_frame ,
                             width      = self.button_width,
                             height     = self.button_height,
                             text       = button_text )
        a_button.grid( row  = self.button_row, column = self.button_column )
        self.button_column += 1

        if command is not None:
            a_button.config( command = command  )

        return a_button

"""

see ex_ttk_treview as well


# { ----  generally all imports at top ---- }

import sys
import dis
import os
import tkinter as tk
import tkinter.ttk as ttk
from   tkinter.messagebox import showinfo

import ex_helpers       # this has rouines to help in showing examples


# {---- files may contain helper functions that help with the example
# but are not really part of them,
# an eample here, not a particularlly useful one does not begin with ex_
# ----}
"""
#----------------------------------------
# ----  class ... actually for real work, will move master to.....

class FileTreeview( tk.Frame ):
    """
    see also ex_ttk_treeview.py

    Add:
        columns for date and size
        ability to sort
        ability to filter
        callbacks
        multiple selections
        update
        ...

    """

    def __init__(self, master, path):
        tk.Frame.__init__(self, master)

        self.config( bg = "red")
        treeview        = tk.Treeview(self)
        self.treeview   = treeview
        ysb             = tk.Scrollbar(self, orient='vertical',    command = treeview.yview )
        xsb             = tk.Scrollbar(self, orient='horizontal',  command = treeview.xview )

        treeview.configure( yscroll=ysb.set, xscroll=xsb.set)
        treeview.heading('#0', text = path, anchor = 'w')    #0   = index to col heading

        abspath     = os.path.abspath(path)
        root_node   = treeview.insert( '', 'end', text=abspath, open=True )

        # consider wait cursor...
        print( f"for init call to process_dir root_node = {root_node}, abspath = {abspath} please wait a bit.....")
        self.process_directory( root_node, abspath )

        treeview.grid(row=0, column=0, sticky = "nsew")
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')

        self.rowconfigure(    0, weight= 1 )
        self.columnconfigure( 0, weight= 1 )

        treeview.bind( "<<TreeviewSelect>>", self.on_select )

    # ----------------------------------
    def on_select_cb( self, full_path, full_path_list = None,   event = None ):
        """


        """
        print( f"on_select_cb:")
        print( f"full_path {full_path}, full_path_list: {full_path_list} event: {event}")

    # ----------------------------------
    def on_select( self, event ):
        """
        from: ex_working_from_web may be below


        """
        item     = self.treeview.identify( 'item', event.x, event.y )
        cur_item = self.treeview.focus()
        #rint( f" self.treeview.item(cur_item) =  {self.treeview.item(cur_item)}" )

        #while True:
        full_path_list   = []
        for ix in range( 20 ): # limit on while True  do some other way

            if cur_item =="":
                #rint( "cur_item is empty string" )
                break   # perhaps throw exception
            else:
                #rint( f"cur_item  = {repr(cur_item)}")
                #rint( f" self.treeview.item(cur_item) =  {self.treeview.item(cur_item)}" )
                this_text     = self.treeview.item(cur_item)["text"]
                #full_path_list.append(this_text)
                full_path_list.insert( 0, this_text)
                #rint( f"this_text = {this_text}")
                cur_item    = self.treeview.parent( cur_item )
            #rint( full_path_list )

        full_path  = "\\".join( full_path_list )
        #rint( f"File Treeview on_select: this is the full_path ={full_path}" )
        self.on_select_cb( full_path, full_path_list = full_path_list,   event = event )

    # ----------------------------------
    def filter_file_cb( self, p, path, isdir ):
        """
        use as callback for file filtering, try to use file_filters
        return True for ok
        """
        return True



    # ----------------------------------
    def process_directory(self, parent, path ):
        """
        parent  -- determines the location of the insert is a node int the treevie see oid and
        initial call
        path -- directory, path full? to build
        populate the directories with files and call recursivelly to get
        all subdirectories, this can take a lot of memory and possibly
        time
        does not check for a refresh
        """
        #rint( f"process_directory path = {path}")

        for p in os.listdir(path):
            abspath     = os.path.join( path, p )
            isdir       = os.path.isdir( abspath )
            include_ok  = self.filter_file_cb( p, path, isdir )

            oid       = self.treeview.insert( parent, 'end', text=p, open=False )

            """
            tree.insert('', 'end',text="1",values=('1','C++'))
            tree.insert('', 'end',text="2",values=('2', 'Java'))
            tree.insert('', 'end',text="3",values=('3', 'Python'))

            search on python ttk treeview insert text and values
            """

            if isdir:
                self.process_directory( oid, abspath )

# ---- ex_file_treeview
# ----------------------------------------
