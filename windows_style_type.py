# -*- coding: utf-8 -*-
"""
Purpose:
    part of my ( rsh ) library of reusable code 
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.
"""

import tkinter as Tk

STANDARD_NETURAL_BG =  "lightgray"    # use for things like frames to blend in
STANDARD_BUTTON_BG =   "gray"         # generally darker then STANDARD_NETURAL_BG
#STARNDAR_BUTTON_                      # FOR HOVER

# more in function

# ------------------------------------------
def set_style_type( parent,    ):
    """
    style values determine the color... values of items built
    this is just a beginning
    btn   or button  or bn

    https://stackoverflow.com/questions/4969543/colour-chart-for-tkinter-and-tix/6932500
    http://tephra.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
    bg  background
    fg  foreground

    """

    # --------- gui standards work on more have themes have in another object ?

    print( "running windows_style_type ")

    std_font             = ( "DejaVu Serif", 10 )
    std_borderwidth      = 5
    std_click_relief     = Tk.GROOVE, # Tk.SUNKEN   # for clickable things
    std_text_entry_bg    = "white"     # "blue" "green"

    # ---- button
    """
     )      # padx = 2, pady = 2,
    "solid",
    relief=FLAT )
    B2 = Tkinter.Button(top, text ="RAISED", relief=RAISED  relief=SUNKEN "GROOVE", RIDGE
    """
    # can next be made generic !!
    parent.button_dict      = { "bg":                STANDARD_BUTTON_BG,
                                "fg":               "black",
                                "activebackground": "lightgray",
                                "relief":            std_click_relief,
                                "borderwidth":       std_borderwidth,
                            }


    parent.widget_style_dispactch_dict[ Tk.Label ] = parent.button_dict
        # is ok if we dispatch on type, by not instance

    # ---- checkbutton
    parent.checkbutton_dict   = {    "bg":               "gray",
                                     "relief":           std_click_relief,
                                     "borderwidth":      std_borderwidth,
                             # "fg":               parent.tk_frame_bg,    # not a known option win10
                             # "activebackground": parent.tk_frame_bg,    # not a known option win10
                            }


    # ---- frame
    parent.frame_dict   = {    "bg":               STANDARD_NETURAL_BG,
                               "relief":           std_click_relief,
                               "borderwidth":      std_borderwidth,
                             # "fg":               parent.tk_frame_bg,    # not a known option win10
                             # "activebackground": parent.tk_frame_bg,    # not a known option win10
                            }

    # ---- tab pages tabp
    # parent.tk_tabp_bg  = "red"
    # parent.tk_tabp_fg  = "blue"
    # parent.tk_tabp_ab  = "green"

    parent.tabp_dict   = {  "bg":               "red",
                             # "fg":               parent.tk_tabp_bg,    # not a known option win10
                             # "activebackground": parent.tk_tabp_bg,    # not a known option win10
                            }

    # ---- label
    parent.label_dict   = {    "bg":               STANDARD_NETURAL_BG,
                               "borderwidth":      std_borderwidth,
                             # "fg":               parent.tk_tabp_bg,    # not a known option win10
                             # "activebackground": parent.tk_tabp_bg,    # not a known option win10
                            }

    # ---- labelframe
    parent.labelframe_dict   = {    "bg":               STANDARD_NETURAL_BG,
                                    "borderwidth":      std_borderwidth,
                                    "font":             std_font,
                             # "fg":               parent.tk_tabp_bg,    # not a known option win10
                             # "activebackground": parent.tk_tabp_bg,    # not a known option win10
                            }

    # ---- checkbox
    parent.checkbox_dict   = { "bg":               STANDARD_NETURAL_BG,    #"red",
                             # "fg":               parent.tk_checkbox_bg,    # not a known option win10
                             # "activebackground": parent.tk_checkboxbg,    # not a known option win10
                            }

    # ---- entry


    parent.entry_dict   = {  "bg":                std_text_entry_bg,
                             # "fg":               parent.tk_entry_bg,    # not a known option win10
                             # "activebackground": parent.tk_entry_bg,    # not a known option win10
                            }

    # ---- combobox   may need setting with ttk styles ......
    parent.tk_combobox_bg  = "red"
    parent.tk_combobox_fg  = "blue"
    parent.tk_combobox_ab  = "green"

    parent.combobox_dict   = {  'selectbackground':              parent.tk_combobox_bg,
                             # "fg":               parent.tk_combobox_bg,    # not a known option win10
                             # "activebackground": parent.tk_combobox_bg,    # not a known option win10
                            }

    parent.button_padding   = { "padx": 3, "pady": 3, }  # for use with palcement

    # ---- radio button    ......
    # fg    The color used to render the text.

    parent.radio_button_dict       = {  #'selectbackground':           parent.tk_radio_button_bg,
                                       # "font":                       parent.tk_radio_button_font,
                                       "highlightbackground":         STANDARD_NETURAL_BG,
                                       "bg":                          STANDARD_NETURAL_BG,

                                       }

                             # "fg":               parent.tk_combobox_bg,    # not a known option win10
                             # "activebackground": parent.tk_combobox_bg,    # not a known option win10
                            #}

