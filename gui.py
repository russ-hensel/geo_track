# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:34:55 2022

@author: russ
"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    main.main()
# -----------

import tkinter as tk
import logging
from   tkinter   import ttk
from   functools import partial
#import pprint

from   tkcalendar import Calendar, DateEntry
#import types
import datetime


# from   tkinter.scrolledtext import ScrolledText
# ----- local
#import gui_tk_edit
import gui_ttk_ext
from   app_global import AppGlobal

# ---- end imports

STICKY_ALL          = tk.N + tk.S + tk.E + tk.W

# -----------------------------------
def extract_long_lat(  data   ):
    """
    parse to get numeric after equal sign else ret None
    read it
    """
    data    = data.strip()
    splits  = data.split( "=" )
    if len( splits ) > 1:
        data  = splits[1].strip()

    try:
        data  = float( data )
    except:
        data  = None

    #rint( f"data    {data}" )

    return data

#--------------------------------------
class GUI(  ):
    """
    a class that implements a tab interface
    at one time called:
    __init__
        _build_gui
            build_it
               makes pages
                    pages ....

    restart
        self._finish_gui( )


    """
    #  ----------------------
    def __init__( self,   ):
        AppGlobal.gui       = self
        self.controller     = AppGlobal.controller
        self.parameters     = AppGlobal.parameters
        self.logger         = logging.getLogger( AppGlobal.logger_id + ".gui")
        self.logger.info("in class GUI init for the clip_board gui_with_tabs")
           # logger not currently used by her

        self.text_in        = None    # init later
        self.text_out       = None    # used in controller? set below

        #self.default_button = 0   # buttons not currently used at all
        self.root           = gui_ttk_ext.make_root( self.parameters )

        # define here or in the panel with waring??

        self._polling_pause    = None
        self.polling_pause_on( False )

        #self.double_buttons    = double_buttons_tk.DoubleButtons( self )
        #self.button_var        = self.double_buttons.button_var   # keeps all buttons in one group
#        self.button_var.set( self.controller.parameters.rb_num_on )

        self.root.title( f"{self.controller.app_name} mode: {AppGlobal.parameters.mode} " +
                         f" version: {self.controller.version}" )

        self.root.grid_rowconfigure(    0, weight=0 )
        self.root.grid_rowconfigure(    1, weight=0 )
        self.root.grid_rowconfigure(    2, weight=0 )
        # moving to frame placement
        # self.root.grid_rowconfigure(    3, weight=1 )
        # self.root.grid_rowconfigure(    4, weight=1 )

        self.root.grid_columnconfigure( 0, weight=1 )
        #self.root.grid_columnconfigure( 1, weight=1 )

        self._build_gui()

   # --------------------------
    def root_destroy( self,   ):
        """
        what it says, read
        used by controller

        """
        self.root.destroy()
        #self.gui.root.destroy()           # make gui.root_destroy()

   # --------------------------
    def polling_pause_on( self, pause = False ):
        """
        what it says, read

        """
        self._polling_pause =  pause
        print( f"self._polling_pause >{self._polling_pause}<")

    # -------------------------------------
    def run( self, polling_function   ):
        """
        run the gui and start polling
        read
        """
        msg       = "gui.run: mainloop comming up..."
        print( msg )
        # next may be in gui ext
        self.root.attributes( '-topmost', True  )
        self.root.attributes( '-topmost', False )

        self.polling_function = polling_function  # --- arguments --zip

        # next could be a polling 0 then poling or nothing
        # but must be somethings ending with call to _polling
        self.root.after( self.parameters.poll_delta_t , self._polling )
        self.root.mainloop()

        # # next cannot work because it blocks
        # while True:
        #     self.root.after( self.parameters.poll_delta_t , polling_function )

    # -------------------------------------
    def _polling ( self,    ):
        """
        continue polling from run()
        if ok factor out polling de
        """
        #rint( "_polling" )
        if  not self._polling_pause:
            self.polling_function( )
        # else:
        #     #rint( f"_polling  self._polling_pause{self._polling_pause}")
        self.root.after( self.parameters.poll_delta_t , self._polling  )
    # ---- gui build ----------------------------
    # -------------------------------------
    def _build_gui( self,   ):
        """
        link to a gui build
        """
            # !! add more info here

        self._menu( self.root )

        # ----- set up root for resizing
        # self.root.grid_rowconfigure(    1, weight = 1 )
        # self.root.grid_columnconfigure( 1, weight = 1  )

        # self.root.grid_rowconfigure(    2, weight = 1 )
        # self.root.grid_columnconfigure( 2, weight = 1  )

        placer = gui_ttk_ext.PlaceInGrid(  0, True )

        # placement.place( a_frame )

        a_frame    = self._make_browse( self.root )
        placer.place( a_frame, sticky = STICKY_ALL )

        a_frame    = self._make_main_frame( self.root )
        placer.place( a_frame, sticky = STICKY_ALL )

        a_frame    = self._make_date_filter_frame( self.root )
        placer.place( a_frame, sticky = STICKY_ALL )

        a_frame    = self._make_lat_long_frame( self.root )
        placer.place( a_frame, sticky = STICKY_ALL )

        a_frame    = self._make_sort_frame( self.root )
        placer.place( a_frame, sticky = STICKY_ALL )

        a_frame    = self._make_output_frame( self.root )
        placer.place( a_frame, sticky = STICKY_ALL )

        # ---- message frame
        a_frame              = self._make_message_frame( self.root )
        placer.new_row()
        placer.place( a_frame, sticky = STICKY_ALL )

        self.root.geometry( self.controller.parameters.win_geometry )


        gui_ttk_ext.set_icon(  self.root,  self.parameters.icon )



        #gui_ttk_ext.bring_to_top( self.root )

    #---------------------
    def _menu (self, parent ) :
        """
        adds a menu bar to the parent
        returns:
            nothing
        """
        # ---- configuration
        menubar    = tk.Menu( parent )
        # !! some of these could use partial instead
        a_menu     = tk.Menu( menubar, tearoff = 0)

        a_menu.add_command( label   = "Show Parameters",
                            command = self.show_parms )

        a_menu.add_command( label   = "Edit Parameters File",
                            command = self.controller.os_open_parmfile )

        if self.parameters.readme_fn is not None:
            a_menu.add_command( label   = "Edit Readme",
                                command = self.controller.os_open_readme )

        if self.parameters.gui_text_log_fn:
            a_menu.add_command( label   = "Edit Gui Log",
                                command = self.controller.os_open_gui_log )

        a_menu.add_command( label   = "Edit Log File",
                            command = self.controller.os_open_logfile )

        a_menu.add_command( label   = "Restart",
                            command = self.controller.restart )

        menubar.add_cascade( label  = "Configuration",   menu = a_menu )

        # ---- About ---- help
        a_menu = tk.Menu( menubar, tearoff = 0 )

        # change to partial ??
        a_menu.add_command( label   = "Show General Help",
                            command = self.controller.os_open_help )

        # # partial to open other help
        # help_function    = partial( AppGlobal.os_open_txt_file, "./help/command.txt" )
        # a_menu.add_command( label   = "Show Command Help",
        #                     command = help_function )

        # partial to open other help
        open_other_help    = partial( AppGlobal.os_open_txt_file, "./help/other_help.txt" )
        a_menu.add_command( label   = "Show Other Help",
                            command = open_other_help )

        a_menu.add_command( label   = "Show Tab Page Help",
                            command = self.controller.open_tabp_help )

        help_function    = partial( AppGlobal.os_open_txt_file, "./readme_rsh.txt" )
        a_menu.add_command( label   = "Show Developer Notes",
                            command = help_function )

        a_menu.add_command( label   = "About...",
                            command = self.open_about )

        menubar.add_cascade( label  = "Help", menu = a_menu )

        parent.config( menu = menubar )

    # ------------------------------------------
    def _make_message_frame( self, parent,  ):
        """
        make the message frame for user feedback
        """
        a_frame              = gui_ttk_ext.MessageFrame( parent,  )

        self.message_frame   = a_frame
        return a_frame

    # ------------------------------------------
    def _make_browse( self, parent,  ):
        """
            parent   a frame to be the parent of widgets
        returns
            a_frame  a frame for caller to place
        """
        #a_frame     = tk.Frame( parent )
        a_frame     = ttk.LabelFrame(  parent,
                            text      = "Base file for operations ",  )
        # --------
        ix_col_max      = 10
        placer          = gui_ttk_ext.PlaceInGrid( a_max = ix_col_max, by_rows = False )
        button_width    = 20

        #-----------------------
        a_widget   =  ttk.Label( a_frame,
                              text     = "Input From",
                              justify  = tk.LEFT,
                              anchor   = tk.E,  )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        #-----------------------
        widget_var          = tk.IntVar()
        values              = [ "DirScan", "GPXfile",  "FileList", "PhotoPoints",
                                "btMap from a FileList File",
                                "btKMZ from a FileList File",
                                "btMap from a Directory",
                                "btKMZ from a Directory",
                                "btMap from *.GPX file",
                                "btOpen Default Ffl",
                                "btOpen Browse File",
                               ]
        a_widget            = ttk.Combobox( a_frame,   values = values,  )
        a_widget.set( values[0] )
        #placer.new_row()
        placer.place(  a_widget, columnspan = 1,   rowspan = None, sticky = None )
        self.input_option_widget    = a_widget  # f"a_widget.get()  {a_widget.get()}" )  get_input_option

        # ---- browse file
        a_bw               = gui_ttk_ext.FileBrowseWidget( a_frame )
        a_bw.initialdir    = "./",
        a_bw.title         = "Select picture file",
        a_bw.filetypes     = (("all files","*.*"), ("GPX file","*.gpx"), )
        a_bw.set_text( AppGlobal.parameters.default_browse_fn )
        #placer.new_row()
        placer.place( a_bw, sticky = STICKY_ALL, columnspan = 1 )
        self.widget_browse = a_bw

        #-----------------------
        a_widget   =  ttk.Label( a_frame,
                              text     = "Dir Recursion \nLimit",
                              justify  = tk.LEFT,
                              anchor   = tk.E,  )
        placer.new_row()
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        widget_var          = tk.IntVar()
        values              = [ 0, 1, 2 ]
        a_widget            = ttk.Combobox( a_frame,
                                            values = values,    )
        a_widget.set( 0 )

        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        self.infran_option_widget    = a_widget  # f"a_widget.get()  {a_widget.get()}" )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Edit Input" )
        a_widget.config( command = self.edit_input_file )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        return a_frame

    # ------------------------------------------
    def _make_date_filter_frame( self, parent,  ):
        """
            parent   a frame to be the parent of widgets
        returns
            a_frame  a frame for caller to place
        """
        #a_frame     = tk.Frame( parent )
        a_frame     = ttk.LabelFrame(  parent,
                            text      = "Base file for operations ",  )
        # --------
        ix_col_max      = 10
        placer          = gui_ttk_ext.PlaceInGrid( a_max = 10, by_rows = False )


        a_frame     = ttk.LabelFrame(  parent,
                            text      = "Date Filtering",
                            height    = 5
                            )
        placer          = gui_ttk_ext.PlaceInGrid( a_max = 10, by_rows = False )
        # ---- begin geo/data point options, consider a titled box
        self.NO_SORT    = 0
        self.DATE_SORT  = 1
        self.FN_SORT    = 2


        # ---- start date controls
        placer.new_row()
        # placer.ix_col  += 1
        #-----------------------
        widget_var          = tk.IntVar()
        a_widget            = ttk.Checkbutton( a_frame, text="Use Dates",   variable = widget_var,
                                               # justify  = tk.RIGHT,)  #command=cb_cb
                                               # allign = tk.E
                                               # anchor = "e"  # ng in ttk
                                               )

        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        self.date_cb_var    = widget_var

        #-----------------------
        a_widget   =  ttk.Label( a_frame,
                              text     = "Start Date",
                              justify  = tk.RIGHT,
                              anchor   = tk.E,  )

        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        cal    = DateEntry(    a_frame,
                               width=12,
                               background       = 'darkblue',
                               foreground       = 'white',
                               borderwidth      = 2,
                               year             = 2010,
                               bordercolor      = "red",
                               showweeknumbers  = False,
                               )
        date_pattern   = "yyyy/mm-dd"

        cal.configure( bordercolor = "blue" )
        cal.configure( foreground  = "red" )
        cal.configure( date_pattern = "yyyy/mm/dd" )   # does not do what I expected

        cal.set_date( datetime.datetime.now() )

        placer.place( cal, )   #sticky = STICKY_ALL )
        self.cal_start   = cal

        # ---- end date
        a_widget   =  ttk.Label( a_frame,
                              text     = "End Date",
                              justify  = tk.LEFT,
                              anchor   = tk.E,  )
        #placer.new_row()
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        cal    = DateEntry(    a_frame,
                               width=12,
                               background       = 'darkblue',
                               foreground       = 'white',
                               borderwidth      = 2,
                               year             = 2010,
                               bordercolor      = "red",
                               showweeknumbers  = False,
                               )
        date_pattern   = "yyyy/mm-dd"

        cal.configure( bordercolor = "blue" )
        cal.configure( foreground  = "red" )

        cal.configure( date_pattern = "yyyy/mm/dd" )   # does not do what I expected

        cal.set_date( datetime.datetime.now() )

        placer.place( cal, )   #sticky = STICKY_ALL )
        self.cal_end   = cal

        return a_frame

    # ------------------------------------------
    def _make_sort_frame( self, parent,  ):
        """
        !!  some of the drop down lists are coupled, can not so far figure out why
            parent   a frame to be the parent of widgets
        returns
            a_frame  a frame for caller to place
        """
        #a_frame     = tk.Frame( parent )
        a_frame     = ttk.LabelFrame(  parent,
                            text      = "Sorting",
                            height    = 5
                            )
        placer          = gui_ttk_ext.PlaceInGrid( a_max = 10, by_rows = False )
        # ---- begin geo/data point options, consider a titled box
        self.NO_SORT    = 0
        self.DATE_SORT  = 1
        self.FN_SORT    = 2


        # ---- sort radiobuttons and more
        placer.new_row()
        widget_var          = tk.IntVar()
        a_widget            = ttk.Radiobutton( a_frame, text ="No Sort",
                                      variable = widget_var,
                                      value    = self.NO_SORT, )

        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        #--------
        a_widget            = ttk.Radiobutton( a_frame, text ="Date Sort",
                                      variable = widget_var,
                                      value    = self.DATE_SORT, )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        #--------
        a_widget      = ttk.Radiobutton( a_frame, text ="FileName Sort",
                                      variable = widget_var,
                                      value    = self.FN_SORT, )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        self.sort_rb_var   = widget_var

        #-----------------------
        widget_var          = tk.IntVar()
        a_widget            = ttk.Checkbutton( a_frame, text ="Add to Default FileList File",   variable = widget_var,
                                               # justify  = tk.RIGHT,)  #command=cb_cb
                                               )

        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        self.add_to_dffl_cb_var    = widget_var

        # #-----------------------
        # a_widget   =  ttk.Label( a_frame,
        #                       text     = "Dir Recursion \nLimit",
        #                       justify  = tk.LEFT,
        #                       anchor   = tk.E,  )
        # placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        #-----------------------
        widget_var          = tk.IntVar()
        values              = [ 0, 1, 2 ]
        a_widget            = ttk.Combobox( a_frame,
                                            text="Dir Recursion \nLimit", # does not show
                                            values = values,
                                               )
        a_widget.set( 0 )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        self.recur_limit_cb_widget    = a_widget  # f"a_widget.get()  {a_widget.get()}" ) gets text
        self.recur_limit_var          = widget_var

        return a_frame

    # ------------------------------------------
    def _make_lat_long_frame( self, parent,  ):
        """
        !!  some of the drop down lists are coupled, can not so far figure out why
            parent   a frame to be the parent of widgets
        returns
            a_frame  a frame for caller to place
        """
        #a_frame     = tk.Frame( parent )
        a_frame     = ttk.LabelFrame(  parent,
                            text      = "Lat Long Filter",
                            height    = 5    )
        width_long_lat  = 50
        values_long     = (
            ["Ignore",
             "Australia,      Sydney          =  -33.8688",
             "Brazil,         Rio de Janeiro  =  -22.9068",
             "Canada,         Toronto         =  43.6532",
             "China,          Beijing         =  39.9042",
             "France,         Paris           =  48.8566",
             "India,          Mumbai          =  19.076",
             "Japan,          Tokyo           =  35.6895",
             "South Africa,   Johannesburg    =  -26.2041",
             "United Kingdom, London          =  51.5074",
             "USA,     AZ     Phoenix         =  33.4484",
             "USA,     CA     Los Angeles     =  34.0522",
             "USA,     CA     San Diego       =  32.7157",
             "USA,     CA     San Jose        =  37.3382",
             "USA,     CA     San Francisco   =  37.7749",
             "USA,     CO     Denver          =  39.7392",
             "USA,     FL     Jacksonville    =  30.3322",
             "USA,     IL     Chicago         =  41.8781",
             "USA,     IN     Indianapolis    =  39.7684",
             "USA,     NC     Charlotte       =  35.2271",
             "USA,     NY     New York City   =  40.7128",
             "USA,     OH     Columbus        =  39.9612",
             "USA,     PA     Philadelphia    =  39.9526",
             "USA,     TX     Houston         =  29.7604",
             "USA,     TX     San Antonio     =  29.4241",
             "USA,     TX     Dallas          =  32.7767",
             "USA,     TX     Austin          =  30.25",
             "USA,     TX     Fort Worth      =  32.7555",
             "USA,     TX     El Paso         =  31.7619",
             "USA,     WA     Seattle         =  47.6062"  ]
            )
        values_lat      = (
            [ "Ignore",
              "Australia:      Sydney          = 151.2093",
              "Brazil:         Rio de Janeiro  = -43.1729",
              "Canada:         Toronto         = -79.3832",
              "China:          Beijing         = 116.4074",
              "France:         Paris           =   2.3522",
              "India:          Mumbai          =   72.8777",
              "Japan:          Tokyo           =   139.6917",
              "South Africa:   Johannesburg  =   28.0473",
              "United Kingdom: London  =   -0.1278",
              "USA:    AZ,     Phoenix  =   -112.074",
              "USA:    CA,     Los Angeles  =   -118.2437",
              "USA:    CA,     San Diego  =   -117.1611",
              "USA:    CA,     San Jose  =   -121.8863",
              "USA:    CA,     San Francisco  =   -122.4194",
              "USA:    CO,     Denver  =   -104.9903",
              "USA:    FL,     Jacksonville  =   -81.6557",
              "USA:    IL,     Chicago  =   -87.6298",
              "USA:    IN,     Indianapolis  =   -86.1581",
              "USA:    NC,     Charlotte  =   -80.8431",
              "USA:    NY,     New York City  =   -74.006",
              "USA:    OH,     Columbus  =   -82.9988",
              "USA:    PA,     Philadelphia  =   -75.1652",
              "USA:    TX,     Houston  =   -95.3698",
              "USA:    TX,     San Antonio  =   -98.4936",
              "USA:    TX,     Dallas  =   -96.797",
              "USA:    TX,     Austin  =   -97.75",
              "USA:    TX,     Fort Worth  =   -97.3308",
              "USA:    TX,     El Paso  =   -106.485",
              "USA:    WA,     Seattle  =   -122.3321" ]
            )

        # --------
        ix_col_max      = 10
        placer          = gui_ttk_ext.PlaceInGrid( a_max = ix_col_max, by_rows = False )
        button_width    = 20

        #     ---------
        placer.new_row()

        # ---- Min Long
        widget_var          = tk.IntVar()
        a_widget            = ttk.Label( a_frame, text="Min Long",
                                               # justify  = tk.RIGHT,)  #command=cb_cb
                                               # allign = tk.E
                                               # anchor = "e"  # ng in ttk
                                               )

        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        self.max_long_check_varb    = widget_var

        #-----------------------
        widget_var          = tk.IntVar()




        #values     = ["0", "1", "2", "3", "4", "5", "6", "7"]

        a_widget            = ttk.Combobox( a_frame,
                                            text   ="min long", # does not show
                                            width  = width_long_lat,
                                            values = values_long,
                                               )
        a_widget.set( values_long[0] )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        self.min_long_comb_widget    = a_widget  # f"a_widget.get()

        #---- Max Long
        widget_var          = tk.IntVar()
        a_widget            = ttk.Label( a_frame, text="Max Long",
                                               )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        #self.min_lat_check_var    = widget_var

        #-----------------------
        widget_var          = tk.IntVar()

        a_widget            = ttk.Combobox( a_frame,
                                            text="zxzx", # does not show
                                            width  = width_long_lat,
                                            values = values_long,
                                               )
        a_widget.set( values_long[0] )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        #self.min_lat_comb_widget    = a_widget  # f"a_widget.get()  {a_widget.get()}" )
        self.max_long_comb_widget    = a_widget

        # ---- Min Lat
        widget_var          = tk.IntVar()
        a_widget            = ttk.Label( a_frame, text="Min Lat",
                                               # justify  = tk.RIGHT,)  #command=cb_cb
                                               )
        placer.new_row()
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        #self.max_lat_check_var    = widget_var

        #-----------------------
        widget_var          = tk.IntVar()
        values     = values_lat
        a_widget            = ttk.Combobox( a_frame,
                                            text="zxzdddx", # does not show
                                            width  = width_long_lat,
                                            values = values,
                                               )
        a_widget.set( values[0] )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        self.min_lat_comb_widget    = a_widget  # f"a_widget.get()  {a_widget.get()}" )

        #---- Max Lat
        #widget_var          = tk.IntVar()
        a_widget            = ttk.Label( a_frame, text="Max Lat",
                                               # justify  = tk.RIGHT,)  #command=cb_cb
                                               # allign = tk.E
                                               # anchor = "e"  # ng in ttk
                                               )

        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        self.max_lat_check_var    = widget_var

        #-----------------------
        widget_var      = tk.IntVar()

        values          = values_lat
        a_widget        = ttk.Combobox( a_frame,
                                            text="min lat", # does not show may link
                                            width  = width_long_lat,
                                            values = values,
                                               )
        a_widget.set( values[0] )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        self.max_lat_comb_widget    = a_widget  # f"a_widget.get()  {a_widget.get()}" )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Clear Long, Lat" )
        a_widget.config( command = self.clear_lat_long )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        return a_frame

    # ------------------------------------------
    def _make_output_frame( self, parent,  ):
        """
            parent   a frame to be the parent of widgets
        returns
            a_frame  a frame for caller to place
        """
        #a_frame     = ttk.Frame( parent )
        a_frame     = ttk.LabelFrame(  parent, text = "Output Options", )
        # --------
        ix_col_max  = 10
        placer      = gui_ttk_ext.PlaceInGrid( a_max = ix_col_max, by_rows = False )

        # a_widget            = ttk.Radiobutton( a_frame,
        #                                text        = "Use Groups",
        #                                #variable    = self.use_what_var,
        #                                #value       = self.use_group_rb,
        #                                # command     = self.controller.group_check_button_clicked
        #                                )

        # placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        # ----
        button_width = 20

        # ---- Checkbuttons
        #-----------------------
        widget_var          = tk.IntVar()
        a_widget            = ttk.Checkbutton( a_frame, text ="KMZ=GoogleEarth",   variable = widget_var,
                                              ) # justify  = tk.RIGHT,)  #command=cb_cb  )

        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        self.google_earth_var   = widget_var

        #-----------------------
        widget_var          = tk.IntVar()
        a_widget            = ttk.Checkbutton( a_frame, text ="GPX=Map",   variable = widget_var,
                                              ) # justify  = tk.RIGHT,)  #command=cb_cb  )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        #self.add_to_dffl_cb_var    = widget_var
        self.folium_var   = widget_var

        #-----------------------
        widget_var          = tk.IntVar()
        a_widget            = ttk.Checkbutton( a_frame, text ="FileListFile",   variable = widget_var,
                                              ) # justify  = tk.RIGHT,)  #command=cb_cb  )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        #self.add_to_dffl_cb_var    = widget_var

        #-----------------------
        widget_var          = tk.IntVar()
        a_widget            = ttk.Checkbutton( a_frame, text ="PhotoPoints",   variable = widget_var,
                                              )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )
        #self.add_to_dffl_cb_var    = widget_var

        # ---- Buttons
        # kmx
        a_widget = ttk.Button( a_frame , width = button_width,  text = "Edit" )
        a_widget.config( command = AppGlobal.controller.edit_kmz )
        placer.new_row()
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        # map folium gpx
        a_widget = ttk.Button( a_frame , width = button_width,  text = "Edit" )
        a_widget.config( command = AppGlobal.controller.edit_map )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        # filelist
        a_widget = ttk.Button( a_frame , width = button_width,  text = "Edit" )
        a_widget.config( command = AppGlobal.controller.edit_filelist )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Edit" )
        a_widget.config( command = AppGlobal.controller.edit_photo_points )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )


        a_widget = ttk.Button( a_frame , width = button_width,  text = "Go..." )
        a_widget.config( command = AppGlobal.controller.input_and_go )
        placer.ix_col += 1  # not effective need a filler !!
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        return a_frame

    # ------------------------------------------
    def _make_main_frame( self, parent,  ):
        """
            parent   a frame to be the parent of widgets
        returns
            a_frame  a frame for caller to place
        """
        #a_frame     = ttk.Frame( parent, height = 100 )  # height not currently effective
        a_frame     = ttk.LabelFrame(  parent,
                             text      = "ttk.LabelFrame",
                           )
        # --------
        ix_col_max  = 10
        placer      = gui_ttk_ext.PlaceInGrid( a_max = ix_col_max, by_rows = False )

        # ---- Buttons
        button_width = 20

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Map from a FileList File" )
        a_widget.config( command = AppGlobal.controller.gui_make_map_from_filelist )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "KMZ from a FileList File" )
        a_widget.config( command = AppGlobal.controller.gui_make_kmz_from_filelist )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Map from a Directory" )
        a_widget.config( command = AppGlobal.controller.gui_make_map_from_dir )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "KMZ from a Directory" )
        a_widget.config( command = AppGlobal.controller.gui_make_kmz_from_dir )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Map from *.GPX file" )
        a_widget.config( command = AppGlobal.controller.gui_make_map_from_gpx_file )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Open Default Ffl" )
        a_widget.config( command = AppGlobal.controller.gui_open_dffl )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Open Browse File" )
        a_widget.config( command = AppGlobal.controller.gui_open_browse_file )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

         # ---- new row infranview
        placer.new_row()
        a_widget = ttk.Button( a_frame , width = button_width,  text = "Infranview" )
        a_widget.config( command = AppGlobal.controller.gui_open_irfanview )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Picture Frame" )
        a_widget.config( command = AppGlobal.controller.gui_open_dffl )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        placer.new_row()

        a_widget = ttk.Button( a_frame , width = button_width,  text = "test_gets" )
        a_widget.config( command = self.test_some_gets )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Test>Makeup GPX" )
        a_widget.config( command = AppGlobal.controller.makeup_gpx )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        a_widget = ttk.Button( a_frame , width = button_width,  text = "Test 2" )
        a_widget.config( command = AppGlobal.controller.test2 )
        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        return a_frame

    # ---- gets ----------------------------
    # --------------------------
    def test_some_gets( self ):
        """
        read me
        """
        msg    = f"get_input_option  >{self.get_input_option()}<"
        print( msg )
        msg    = f"get_min_long  >{self.get_min_long()}<"
        print( msg )
        msg    = f"get_max_long  >{self.get_max_long()}<"
        print( msg )
        msg    = f"get_min_lat  >{self.get_min_lat()}<"
        print( msg )
        msg    = f"get_max_lat >{self.get_max_lat()}<"
        print( msg )

    # --------------------------
    def get_output_google( self ):
        """
        What it says, return bool true if output desired
        """
        get_it    = self.google_earth_var.get()
        return get_it

    # --------------------------
    def get_output_folium( self ):
        """
        What it says, return bool true if output desired
        """
        get_it    = self.folium_var.get()
        return get_it

    # --------------------------
    def get_add_to_dffl ( self,   ):
        """
        what it says, read
        """
        data    = self.add_to_dffl_cb_var.get()
        return  data

    # --------------------------
    def get_min_long( self ):
        """
        What it says, return float or None
        """
        data    = self.min_long_comb_widget.get()
        data    = extract_long_lat( data )
        return data

    # --------------------------
    def get_max_long( self ):
        """
        What it says, return float or None
        """
        return extract_long_lat( self.max_long_comb_widget.get() )

    # --------------------------
    def get_min_lat( self ):
        """
        What it says, return float or None
        """
        return extract_long_lat( self.min_lat_comb_widget.get() )

    # --------------------------
    def get_max_lat( self ):
        """
        What it says, return float or None
        """
        return extract_long_lat( self.max_lat_comb_widget.get() )

    # --------------------------
    def clear_lat_long( self,   ):
        """
        what it says, read
        """
        value_0 = "Ignore"
        self.max_lat_comb_widget.set(  value_0 )
        self.max_long_comb_widget.set( value_0 )
        self.min_lat_comb_widget.set(  value_0 )
        self.min_long_comb_widget.set( value_0 )

    # --------------------------
    def get_input_option( self ):
        """
        string more or less enum
        """
        return self.input_option_widget.get()

    # --------------------------
    def get_recur_limit( self,   ):
        """
        what it says, read

        """
        data    = int( self.recur_limit_cb_widget.get() )
        return  data

   # --------------------------
    def get_start_date( self,   ):
        """
        what it says, read
        file_name   = AppGlobal.gui.get_browse()
        """
        data  = self.cal_start.get_date()
        return  data

   # --------------------------
    def get_end_date( self,   ):
        """
        what it says, read
        file_name   = AppGlobal.gui.get_browse()
        """
        data  = self.cal_end.get_date()
        return  data

    # --------------------------
    def get_use_dates( self,   ):
        """
        what it says, read
        return
            bool true if use date filter
        """
        data  = self.date_cb_var.get()
        return  data

    # --------------------------
    def clear_use_dates( self,   ):
        """
        what it says, read
        return
            bool true if use date filter
        """
        msg   = " still needs implementation"
        self.write_gui( msg )
        print( msg )
        data  = self.date_cb_var.get()
        return  data

   # --------------------------
    def get_browse( self,   ):
        """
        what it says, read
        file_name   = AppGlobal.gui.get_browse()
        """
        file_name     = self.widget_browse.get_text()
        return file_name

   # --------------------------
    def get_sort_rb_index( self,   ):
        """
        what it says, read
        used by controller
        """
        rb_index   = self.sort_rb_var.get(  )
        print( f"rb indes is {rb_index}" )
        return rb_index

    # --------------------------
    def get_info( self ):
        """
        needs doc -- left over from notebook demo, delete ?

        """
        msg         =  "get_info\n"
        # #msg    =  f"{msg}{(self.nb ).tab( self.nb.select(), "text" )}"
        # nb_frame    = self.a_notebook.select()

        # msg         = f"{msg}nb_frame{nb_frame} \n"
        # msg         =  f"{msg}text on the tab{self.a_notebook.tab( nb_frame, 'text' )}\n"
        # # same more compact
        # msg         = ( f"{msg}text on the tab: "
        #                 f"{self.a_notebook.tab( self.a_notebook.select(), 'text' )}\n" )
        return msg

    # ---- actions --------------------------
    # --------------------------
    def bring_to_top( self ):
        """
        what it says, read
        """
        gui_ttk_ext.bring_to_top( self.root )

    # --------------------------
    def edit_input_file( self ):
        """
        what it says, read
        """
        file_name    = self.get_browse()
        msg          = f"edit_input_file later check file type of {file_name} and perhaps existance.... "
        print( msg )
        AppGlobal.os_open_txt_file( file_name  )

   # # ------------------------------------------
   #  def _make_test_frame( self, parent_frame,  ):
   #      """
   #      what it says, read
   #      """
   #      a_frame  = tk.LabelFrame(   parent_frame,
   #                         #bg        = self.parameters.bg_color_frame,
   #                         text      = "Test Items",
   #                         #bd        = 2,
   #                         height    = 50,
   #                         width     = 200
   #                         )

   #      ix_row        = 2
   #      ix_col        = 0

   #      # -------- "Edit Dev\nNotes"
   #      self.dbl_buttons.ix_rb_index    += 1
   #      ix_col                          += 1

   #      self.make_and_place_transform_buttons_3 (   a_frame,    text = "Edit Dev\nNotes",
   #                                                  ix_row = ix_row, ix_col = ix_col,
   #                                 button_var       = self.button_var,
   #                                 button_command   = AppGlobal.controller.bcb_edit_dev_notes,
   #                                 rb_index         = self.dbl_buttons.ix_rb_index )
   #      # -------- sage
   #      self.dbl_buttons.ix_rb_index    += 1
   #      ix_col                          += 1

   #      self.make_and_place_transform_buttons_3 ( a_frame,
   #                                 text             = "Sage",
   #                                 ix_row           = ix_row,
   #                                 ix_col           = ix_col,
   #                                 button_var       = self.button_var,
   #                                 button_command   = AppGlobal.cmd_processor.transform_sage,
   #                                 rb_index         = self.dbl_buttons.ix_rb_index )
   #      #self.controller.dispatch_dict[ix_rb_index]  = self.controller.cmd_processor.transform_sage

   #      #-------- test -----
   #      self.dbl_buttons.ix_rb_index   += 1
   #      ix_col             += 1
   #      #self.test_rb        = self.dbl_buttons.ix_rb_index

   #      self.make_and_place_transform_buttons_3 ( a_frame,    text = "test",
   #                                 ix_row           = ix_row, ix_col = ix_col,
   #                                 button_var       = self.button_var,
   #                                 button_command   = AppGlobal.cmd_processor.transform_to_camel,
   #                                 rb_index         = self.dbl_buttons.ix_rb_indexself.dbl_buttons.ix_rb_index
   #                                  )



   #      #-------- user_pages ------
   #      self.dbl_buttons.ix_rb_index         += 1
   #      ix_col                   += 1
   #      #self.sage_rb             = self.dbl_buttons.ix_rb_index

   #      self.make_and_place_transform_buttons_3 ( a_frame,
   #                                  text = "UserPage",
   #                                  ix_row           = ix_row,
   #                                  ix_col           = ix_col,
   #                                  button_var       = self.button_var,
   #                                  button_command   = AppGlobal.cmd_processor.transform_user_pages,
   #                                  rb_index         = self.dbl_buttons.ix_rb_index )

   #      #-------- user_pages ------
   #      self.dbl_buttons.ix_rb_index         += 1
   #      ix_col                   += 1
   #      #self.sage_rb             = self.dbl_buttons.ix_rb_index

   #      self.make_and_place_transform_buttons_3 ( a_frame,
   #                                  text = "UserPage",
   #                                  ix_row           = ix_row,
   #                                  ix_col           = ix_col,
   #                                  button_var       = self.button_var,
   #                                  button_command   = AppGlobal.cmd_processor.transform_user_pages,
   #                                  rb_index         = self.dbl_buttons.ix_rb_index )

   #      return a_frame

    # --------------------------
    def on_changed( self, event ):
        """
        for debug delete ? -- us for tabpage help in future

        """
        # could be done at any time
        self.tap_page_help_fn   = self.a_notebook.tab( self.a_notebook.select(), 'text' ) + ".txt"
        print( f"tap_page_help_fn  >>{self.tap_page_help_fn}<< "
               "for tabpage on_changed need to remove spaces" )
        #rint( f"on_changed  {event} for tabpage" )
        #rint( self.get_info() )

    #----------------------------------------------------------------------
    def open_about( self,  ):
        """
        what it says, read
        """
        gui_ttk_ext.about( AppGlobal.controller )

    # --------------------------
    def iconify( self ):
        """
        what it says, read
            used by controller
        """
        self.root.iconify()

    # ---------------------
    def print_info( self ):
        """
        for debug, drop ? use __str__

        """
        msg     = self.get_info()
        print( msg )

    #----------------------------------------------------------------------
    def show_parms(self, ):
        """
        what it says, read
        """
        msg     = f"{AppGlobal.parameters}"
        title   = "Parameters"
        #rint( msg )
        self.write_gui_wt( title, msg )

    # ------------------------------------------
    def clear_message_area( self,   ):
        """
        what it says
        """
        self.message_frame.clear_message_area()

    #----------------------------------------------------------------------
    def write_gui_wt(self, title, a_string ):
        """
        write to gui with a title.
        title     the title
        a_string  additional stuff to write
        make a better function with title = ""  ??
        title the string with some extra formatting
        clear and write string to input area
        """
        self.write_gui( f" =============== {title} ==> \n{a_string}"  )

    #----------------------------------------------------------------------
    def write_gui(self, a_string ):
        """
        clear and write string to display area
        leave it disabled
        !! should not use, this should be in gui_ext  enable disable
        should be where
        """
        self.message_frame.print_string( a_string )

        # self.text_in['state'] = 'normal'       # normal or disabled
        # self.text_in.delete( 1.0, tk.END )
        # self.text_in.insert( tk.END, a_string )
        # self.text_in['state'] = 'disabled'
        if  AppGlobal.parameters.gui_text_log_fn:
            a_string    = "\n" + a_string.replace( "\r", "" )  # is this fix of double spacing??
                                                               # seems to work
                                                               # may need initial \n  --- see above
            with open( AppGlobal.parameters.gui_text_log_fn, "a"  ) as a_file:
                a_file.write( a_string )   # do we need \n check

    # both of these in use !! why or explain

# ---- eof ================== eof ====================




