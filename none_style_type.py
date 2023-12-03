# -*- coding: utf-8 -*-
"""
Purpose:
    part of my ( rsh ) library of reusable code 
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.
"""


import tkinter as Tk


#import  sys
#from   tkinter import ttk
#from   tkinter.scrolledtext import ScrolledText


def set_style_type( parent ):
    """
    see gui_ext.GuiStyle
    !! do the individual var need to be part of parent ??

    """
    # ------------------------------------------
    #def _set_style_values( parent,    ):
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
    # but there are things called themes, look for more doc
    # parent.btn_color     = parent.parameters.btn_color
    # parent.bkg_color     = parent.parameters.bkg_color
    # #parent.text_color    = "white"

    # ---- button




    parent.tk_button_borderwidth  =  5
                        #
    #parent.tk_button_

    parent.button_dict      = {  "bg":             None,
                               "fg":               None,
                               "activebackground": None,
                               "relief":           None,
                               "borderwidth":      None,
                               "font":             None,
                            }

    parent.widget_style_dispactch_dict[ Tk.Label ] = parent.button_dict
        # is ok if we dispatch on type, by not instance

    # ---- checkbutton
    parent.tk_checkbutton_bg            = "gray"   #
    parent.tk_checkbutton_fg            = "blue"
    parent.tk_checkbutton_ab            = "green"
    parent.tk_checkbutton_borderwidth   = 5
    parent.tk_checkbutton_relief        = Tk.RAISED

    parent.checkbutton_dict   = {  "bg":               parent.tk_checkbutton_bg,
                           "relief":           parent.tk_checkbutton_relief,
                           "borderwidth":      parent.tk_checkbutton_borderwidth,
                             # "fg":               parent.tk_frame_bg,    # not a known option win10
                             # "activebackground": parent.tk_frame_bg,    # not a known option win10
                            }


    # ---- frame
    parent.tk_frame_bg            = None   #
    parent.tk_frame_fg            = None
    parent.tk_frame_ab            = None
    parent.tk_frame_borderwidth   = None
    parent.tk_frame_relief        = None

    parent.frame_dict   = {  "bg":               parent.tk_frame_bg,
                             "relief":           parent.tk_frame_relief,
                             "borderwidth":      parent.tk_frame_borderwidth,
                             # "fg":               parent.tk_frame_bg,    # not a known option win10
                             # "activebackground": parent.tk_frame_bg,    # not a known option win10
                            }

    # ---- tab pages tabp


    parent.tabp_dict   = {  "bg":               None,
                             # "fg":               parent.tk_tabp_bg,    # not a known option win10
                             # "activebackground": parent.tk_tabp_bg,    # not a known option win10
                            }

    # ---- label




    parent.label_dict   = {  "bg":               None,
                             "borderwidth":      None,
                             "font":             None,

                             # "fg":               parent.tk_tabp_bg,    # not a known option win10
                             # "activebackground": parent.tk_tabp_bg,    # not a known option win10
                            }

    # ---- checkbox


    parent.checkbox_dict   = {  "bg":               None,
                             # "fg":               parent.tk_checkbox_bg,    # not a known option win10
                             # "activebackground": parent.tk_checkboxbg,    # not a known option win10
                            }

    # ---- entry


    parent.entry_dict   = {  "bg":               None,
                             # "fg":               parent.tk_entry_bg,    # not a known option win10
                             # "activebackground": parent.tk_entry_bg,    # not a known option win10
                            }

    # ---- combobox   may need setting with ttk styles ......


    parent.combobox_dict   = {  'selectbackground':              None,
                             # "fg":               parent.tk_combobox_bg,    # not a known option win10
                             # "activebackground": parent.tk_combobox_bg,    # not a known option win10
                            }

    #parent.button_padding   = { "padx": 3, "pady": 3, }  # for use with palcement


    # ---- radio button    ......


    parent.radio_button_dict       = {  # 'selectbackground':           parent.tk_radio_button_bg,
                                       "font":                        None, }

                             # "fg":               parent.tk_combobox_bg,    # not a known option win10
                             # "activebackground": parent.tk_combobox_bg,    # not a known option win10
                            #}








