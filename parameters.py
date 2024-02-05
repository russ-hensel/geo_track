# -*- coding: utf-8 -*-


"""
    parameters    for   geo_track
    some junk and unimplemented parms, !! clean up
    unfortunately this is a moving target, will try to keep documentation up to date
    choose_mode is the first method as you may use it most often to change
    modes  .... start with new_user_mode, you can then mess with it or copy it
    or other parts of the parameter file to make new modes


    Search:


"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    main.main()
# --------------------

import os
import logging

# ---- local imports
from   app_global import AppGlobal
# "gui_with_qt"   gui_style
import running_on

# ========================================
class Parameters( ):
    """
    manages parameter values: use like ini file but it is code
    """
    # -------
    def choose_mode( self ):
        """
        typically choose one mode
            and if you wish add the plus_test_mode
            if you comment all out all modes you get the default mode which should
            run, perhaps not in the way you wan
        """
        self.mode_tk()
        #self.mode_qt()

        #self.new_user_mode()
        #self.millhouse_1_mode()
        #self.russ_1_mode()

        # --- add on for testing, use as desired edit mode for your needs
        #self.plus_test_mode()

    #  -------
    def mode_tk( self ):
        """
        mode that uses tk ( and ttk ) as the gui widget set
        """
        self.mode               = "mode_tk"

        # self.gui_style          = "gui_with_tabs"       # "gui_with_qt":   "gui_with_tabs,   see clip_board.py
        self.gui_module         = "gui_with_tabs"       #  gui_with_tabs  "gui_qt"

        self.gui_theme_type     = "ttkthemes"
        self.gui_ttk_theme      = "plastik"
        self.logging_level      = logging.DEBUG

        self.poll_delta_t       = 100

        # ----- snip or example files
#        self.snip_file_fn       = r"snips_file_test.txt"
#        self.snip_file_fn       = r"snip_files_nov_18.txt"
#        self._read_snip_files_( self.snip_file_fn )

        # ----- snippets
        self.snippets_fn        = "./snipsand/snippetts_example.txt"
        self.snippets_sort      = True

    # ---- ---->> More methods:  one for each mode
    # -------
    def new_user_mode( self ):
        """
        a mode for the new user, pretty much empty,
        a new user may experiment here.
        """
        self.mode               = "mode new_user"

    # -------
    def russ_1_mode( self ):
        """
        russ: first mode for theProf -- not documented
        """
        self.mode               = "Russ_1"

        self.win_geometry       = '1500x800+20+20'     # width x height position  x, y
        self.win_geometry       = '1200x800+40+40'     # width x height position  x, y


        self.logging_level      = logging.DEBUG

        # ----- snip or example files

#        self.snippets_fn        = [ "./snipsand/snippetts_1.txt", "./snipsand/snippetts_1.txt" ]
             # multiple snippet files
        self.snippets_sort      = True

        # ================== snippets ============================
        self.snippets_sort      = True                # sort snippes on key, else in file order
        self.snippets_fn        = "./snipsand/snippetts_1.txt"

        # ================== snips ============================
        self.snip_file_sort     = True                # sort make them easier to find in the GUI

        # next:  this is prepended to a snip file prior to opening the file
        #        so you can easily keep the snip files in a place you find convenient.
        self.snip_file_path     = r"C:\Russ\0000\python00\python3\_examples"
        #
          # path prepended to all snip files
        self.snip_file_fn       = "./snipsand/snip_files_russ.txt"

        self.snip_editor       = r"C:\apps\Anaconda3\Scripts\thonny.exe"
            # editor used for opening snip files

    # -------
    def millhouse_1_mode( self ):
        """
        russ: first mode for millhouse -- not documented
        """
        self.mode               = "millhouse_1"

        self.logging_level      = logging.DEBUG
        self.logging_level      = logging.INFO
        # ----- snip or example files




    # -------
    def plus_test_mode( self ):
        """
        scratch mode to add tests to other modes, not a mode by itself
        an add on mode
        """
        self.mode               = self.mode + " + test"  # change with care

        self.logging_level      = logging.DEBUG

        self.snippets_fn        = ["./snipsand/snippetts_test.txt",
                                   "./snipsand/snippetts_example.txt" ,
                                   "./snipsand/snippetts_1.txt"]

        #self.snippets_fn        = "./snipsand/snippetts_test.txt"
    # -------
    def running_on_tweaks(self,  ):
        """
        not a mode, a tweak to other modes , see documentation
        you need to customize this for your own computers, what you may
            find here are customizations for russ and his computers
        use running on tweaks as a more sophisticated
            version of os_tweaks and computer name tweaks which
        may replace them
        this is computer name tweaks code,
            !! find run_on on which uses os or put computer name under this
        """
        self.os_tweaks()

        computer_id    =   self.running_on.computer_id

        if computer_id == "smithers":
            self.win_geometry       = '1450x700+20+20'      # width x height position
            self.ex_editor          =  r"D:\apps\Notepad++\notepad++.exe"
            self.db_file_name       =  "smithers_db.db"

        elif computer_id == "millhouse":
            self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"
            #self.win_geometry   = '1300x600+20+20'
            self.db_file_name       =  "millhouse_db.db"

        elif computer_id == "theprof":
            self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"
            self.db_file_name       =  "the_prof_db.db"
            self.snip_file_path     = r"D:\Russ\0000\python00\python3\_examples"
            #self.win_geometry       = '1800x700+50+20'      # width x height position

        elif computer_id == "bulldog":
            self.ex_editor          =  r"gedit"
            self.db_file_name       =  "bulldog_db.db"

        elif computer_id == "bulldog-mint-russ":
            self.ex_editor          =  r"xed"
            self.db_file_name       =  "bulldog_db.db"

        else:
            print( f"In parameters: no special settings for computer_id {computer_id}" )
            if self.running_on.os_is_win:
                self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"
            else:
                self.ex_editor          =  r"leafpad"    # linux raspberry pi maybe

    # -------
    def os_tweaks( self ):
        """
        this is an subroutine to tweak the default settings of "default_mode"
        for particular operating systems
        you may need to mess with this based on your os setup
        """
        if  self.os_win:
            pass     # if everything is commented out
            # self.icon               = r"./clipboard_b.ico"
            #     #  very dark greenhouse this has issues on rasPi
            # self.icon               = r"./clipboard_b_red_GGV_icon.ico"
            #     #  looks same as clipboard_b_red_gimp.ico
            # self.icon               = r"./clipboard_b_red_gimp.ico"    # pretty visible -- make black version -- cannot get gimp to do it

            #self.icon              = None                    #  default gui icon

            # self.gui_style          = "none"  # or None
            #self.gui_style          = None  #"windows"
            #self.gui_style          = "windows"
        else:
            pass
            #self.gui_style          = "linux"
            self.icon               = r"./geo_icon_red.png"   #  geo_icon_red.png
    # -------
    def computer_name_tweaksxxxx( self ):
        """
        this is an subroutine to tweak the default settings of "default_mode"
        for particular computers.  Put in settings for you computer if you wish
        these are for my computers, add what you want ( or nothing ) for your computes
        !! use computer name or id ??
        """
        print(self.computername, flush=True)

        if self.computername == "smithers":
            self.win_geometry       = '1250x700+20+20'      # width x height position
            self.ex_editor          =  r"c:\apps\Notepad++\notepad++.exe"    # russ win 10 smithers

        elif self.computername == "millhouse":
            self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"    # russ win 10 millhouse
            self.win_geometry       = '1300x700+150+5'          # width x height position
            self.pylogging_fn       = "millhouse.py_log"   # file name for the python logging

            # need to associate with extension -- say a dict
            self.snip_file_command  = r"C:\apps\Notepad++\notepad++.exe"  #russwin10   !! implement

        elif self.computername  == "theprof":
            self.ex_editor          =  r"c:\apps\Notepad++\notepad++.exe"    # russ win 10 smithers

    # -------
    def __init__( self, ):
        """
        Init for instance, usually not modified, except perhaps debug stuff
        ( if any )... but use plus_test_mode()
        may be down in listing because it should not be messed with.
        """
        AppGlobal.parameters       = self   # register as a global
        self.mode_default()
        self.running_on_tweaks()
        self.choose_mode()

        #rint( self ) # for debugging

    # ------->> default mode, always call
    def mode_default( self ):
        """
        sets up pretty much all settings
        documents the meaning of the modes
        call first, then override as necessary
        good chance these settings will at least let the app run
        """
        self.mode              = "default"
            # name your config, it will show in app tilte
            # may be changed later in parameter init

        #--------------- automatic settings -----------------
        self.running_on   = running_on.RunningOn
        self.running_on.gather_data()

        # some of the next all?? should be moved over to RunningOn
        self.running_on.log_me( logger = None, logger_level = 10, print_flag = False )

        # this is the path to the main.py program
        self.py_path                   = self.running_on.py_path

        self.set_default_path_here     = True
            # to make app location the default path in the app, Think True may always be best.
            # above may be tricky to reset, but we may have the original dir in running on
        # no easy way to override this ??
        if  self.set_default_path_here:     # Now change the directory to location of this file

            py_path    = self.running_on.py_path

            print( f"Directory: (  >>{os.getcwd()}<< switch if not '' to >>{py_path}<<")
            if py_path != "":
                os.chdir( py_path )

        # so we know our os  could be "linux" or our_os == "linux2"  "darwin"....
        self.our_os             = self.running_on.our_os
        self.os_win             = self.running_on.os_win          # boolean True if some version of windows
        self.computername       = self.running_on.computername    # a name of the computer if we can get it
        # directory where app was opened, not where it resides
        self.opening_dir        = self.running_on.opening_dir     # the opening dir befor anyone changes it

        self.platform           = self.our_os           #  redundant

        # ---- appearance -- remove all old gui_style soon?
        self.win_geometry       = '1500x800+20+20'     # width x height position  x, y
        self.win_geometry       = '1500x800+20+20'     # width x height position  x, y

        # but do they use the same units ?
        self.qt_width           = 1200
        self.qt_height          = 500
        self.qt_xpos            = 50
        self.qt_ypos            = 50

        self.tk_win_geo         = f"{self.qt_width}x{self.qt_height}+{self.qt_xpos}+{self.qt_ypos}"
        print( f"self.tk_win_geo {self.tk_win_geo}")

        # icon for running app -- not used in linux (name of a file )
        self.icon               = r"geo_icon.png" # png does not work
        self.icon               = r"geo_icon.ico" # png --gimp--> ico

        # self.gui_style          = "gui_with_qt"         # "gui_with_qt":   "gui_with_tabs,   see clip_board.py
        # self.gui_module         = "gui_qt"          #  gui_with_tabs  "gui_qt"

        self.gui_theme_type     = "ttkthemes"
        self.gui_ttk_theme      = "plastik"     #
            # "blue"  "adapta" arc aquativo "plastik"

        # self.gui_theme_type     = "ttk"   # valid values see gui_with_tabs
        # self.gui_ttk_theme      = "alt"       # anything valid for above see gui_with_tabs
        # for none or ttk
        #style.theme_use("clam")  # clam   10
        # style.theme_use("alt")  # clam    5
        #style.theme_use("classic")  # clam   15
        #style.theme_use("xpnative")  # clam   15

        self.id_color           = "blue"                # to id the app - not implemented yet

        # some of this may be moved to style_types or just not used tk only
        self.bn_color_active    = "gray"
            # color for buttons -- may not be implemented -- use bn to match tkinter api
        self.bn_color_active    = "#E1E1E1"   # color for buttons --
            # may not be implemented -- use bn to match tkinter api

        self.bg_color_frame     = "yellow"   # "black"  # "#F0F0F0"
            #    "#F0F0F0" seems to be a default light gray "gray" is darker

        # ---- gui defaults

        self.default_sort       = "filename"    # see gui.py init and sort frame

        # ---- logging
        self.pylogging_fn       = "app.py_log"   # file name for the python logging
        self.logging_level      = logging.DEBUG        # may be very verbose
        #self.logging_level      = logging.INFO
        #self.logging_level      = logging.INFO

        self.logger_id          = "gt"         # id of app in logging file

        self.gui_text_log_fn    = None   # for edit window if None then no logging
        #self.gui_text_log_fn    = "gui_log.log"

        self.log_gui_text       = False # this is for gui_ext message area
                                             # goes to normal log file  not special one

        # ---- file names

        # this is the name of a program: its executable with path info.
        # to be used in opening an external editor
        self.ex_editor                  =  r"D:\apps\Notepad++\notepad++.exe"    # russ win 10

        # control button for editing the readme file
        self.readme_fn                  = "readme_rsh.txt"   # or None to supress in gui
        self.default_filelist_fn        = "default_file_filelist.txt"
        self.default_photo_points_fn    = "default_photo_points.csv"
        self.default_kmz_fn             = "default_kmz.kmz"
        self.default_html_fn            = "default_map.html"

        # may not be best for text help file
        self.help_file       =  "./help/help.txt"   #  >>. this is the path to our main .py file self.py_path + "/" +
        #self.help_file       =  "http://www.opencircuits.com/Python_Smart_ClipBoard"
            # can be url or a local file -- change for clipboard !!

        self.help_fn            = self.help_file    # old phase out  !!

        self.default_browse_fn  = r"D:/PhotosRaw/2023/aferica/phone/africa_3023/safarie/PXL_20230919_163207438.jpg"
        self.default_browse_fn  = r"/mnt/WIN_D/Russ/0000/python00/python3/_projects/geo_track/test/karen_photos/20220301_155128.jpg"
        #self.default_browse_fn  = r"/mnt/WIN_D/PhotosRaw/2023/karen_photos/20220208_135039.jpg"

        self.irfanview_fn               = "D:/apps/IrfanView/i_view32.exe"
        self.irfanview_fn               = "D:/apps/IrfanView/i_view64.exe"


        self.line_join         = "\r\n"   # cr lf see cmd_processor
                                          # use when joining lines this is windows?
        self.line_join         = "\n"     #


        #---------------------------------------------------
        self.poll_delta_t      = 200      # 200 ok at least on win longer does not fix linux prob
            # how often we poll for clip changes, in ms,
            # think my computer works well as low as 10ms
    # -----------------------------------
    def __str__( self,   ):
        """
        sometimes it is hard to see where values have come out this may help if printed.
        not complete, add as needed -- compare across applications and code above
        """
        a_str = f">>>>>>>>>>* parameters (some) *<<<<<<<<<<<<"
        a_str = f"{a_str}\n   mode                      {self.mode}"
        a_str = f"{a_str}\n   computer_id               {self.running_on.computer_id}"

        a_str = f"{a_str}\n   logger_id                 {self.logger_id}"
        a_str = f"{a_str}\n   logging_level             {self.logging_level}"
        a_str = f"{a_str}\n   pylogging_fn              {self.pylogging_fn}"
        a_str = f"{a_str}\n   gui_text_log_fn           {self.gui_text_log_fn}"

        a_str = f"{a_str}\n   readme_fn                 {self.readme_fn}"
        a_str = f"{a_str}\n   help_file                 {self.help_file}"
        a_str = f"{a_str}\n   default_filelist_fn       {self.default_filelist_fn}"
        a_str = f"{a_str}\n   default_photo_points_fn   {self.default_photo_points_fn}"


        a_str = f"{a_str}\n   ex_editor                 {self.ex_editor}"

        a_str = f"{a_str}\n   line_join                 {self.line_join}"

        a_str = f"{a_str}\n   win_geometry              {self.win_geometry}"
        a_str = f"{a_str}\n   icon                      {self.icon}"
        a_str = f"{a_str}\n   gui_style                 {self.gui_style}"
        a_str = f"{a_str}\n   id_color                  {self.id_color}"

        a_str = f"{a_str}\n   computername              {self.computername}"
        a_str = f"{a_str}\n   our_os                    {self.our_os}"

        #---- sort into above

        a_str = f"{a_str}\n   py_path                   {self.py_path}"
        a_str = f"{a_str}\n   set_default_path_here     {self.set_default_path_here}"

        a_str = f"{a_str}\n   poll_delta_t              {self.poll_delta_t}"

        a_str = f"{a_str}\n   and so much more... \n\n"

        return a_str

# ---- eof ==============================



