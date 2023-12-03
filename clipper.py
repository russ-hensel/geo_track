# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 17:15:30 2023

@author: russ


could build polling ..... into this
for now leave in clipboard app

  #self.old_clip       = ""          # old value of info in clipboard
                                                # may be transformed -
                                                # checked to see if clipboad changed
        #self.undo_clip      = ""          # old value never transformed for undo
            !! register with app global ??

"""
import abc
from   app_global import AppGlobal

"""
uses

new_clip  = pyperclip.paste()

pyperclip.copy( ret_text  )


"""

def make_clipper( clip_type ):
    """
    make a clipper for various modules that might be available

    Parameters
        clip_type : see code

    Returns
        mutates AppGlobal

    """
    if  clip_type == "pyperclip":
         clipper    = PyperCliper()

    elif clip_type == "qt":      # really qt5, but may change for other versions
        clipper    = QtCliper(  )

    # elif clip_type == "null":  #
    #     clipper    = NullCliper()

    else:
        print( "clipper none!!!!!!!!!! -- make it print calls ")
        clipper    = None
    AppGlobal._clipper   = clipper

    return clipper

# ---------------
class ABCCliper( abc.ABC ):
    """
    will be a clipper ... this one for pyperclip
    interface includes ?? and the public methods
        self.new_clip    ?? read only see set_text ( change to property ?? )
        self.old_clip
    """
    #----------- init -----------
    def __init__(self,  ):
        """
        See class doc
        """
        self._clipper              = None     # replace with implementation ... private
        self.new_clip              = None
        self.old_clip              = None     # is read, think should not be written?
        self.undo_clip             = None     # meant to be capture in get_text, and not set_text_stelth

    # --------------------------------------------------
    def __str__( self ):
        """
        the usual, read
        """
        line_begin  = "\n    "  # formatting aid

        a_str       =  "\n\n"
        a_str       = f"{a_str}\n>>>>>>>>>>* clipper  *<<<<<<<<<<<<"
        a_str       = f"{a_str}{line_begin}self._clipper            >{self._clipper}<"
        a_str       = f"{a_str}{line_begin}self.new_clip            >{self.new_clip}<"
        a_str       = f"{a_str}{line_begin}self.old_clip            >{self.old_clip}<"
        a_str       = f"{a_str}{line_begin}self.undo_clip           >{self.undo_clip}<"
        # a_str       = f"{a_str}{line_begin}self._clipper             >{self._clipper}<"
        return a_str

    # -----------------------------------
    def set_text( self, a_string ):
        """
        set text into the clipoard
        will trigger changed -- unless a_string is None

        what it says, read
        """
        self.old_clip     = None
        self.set_clipper_text( a_string )
        #self._clipper.copy( a_string )

    # -----------------------------------
    def set_text_stelth( self, a_string ):
        """
        but do not flag as new
        add a stelth flag and combine with set_text ??

        what it says, read
        """
        self.old_clip     = a_string
        # self._clipper.copy( a_string )
        self.set_clipper_text( a_string )
        #self.undo_clip    is not set,

    # -----------------------------------
    def get_changed_text( self, ):
        """
        return None unless text has changed
        what it says, read
        """
        ret          = None
        new_clip     = self.get_clipper_text()
        if ( new_clip != "" ) and ( new_clip is not None ):   # really a new text clip
            if new_clip != self.old_clip:
                #rint( "\n\n new clip ------" )
                # do we need this logging at all, drop for now -- could have even lower
                #     than debug
                # new_clip_log   = new_clip   # !! seem to have too much \n...
                # old_clip_log   = self.old_clip
                # msg    = ( f">>>>>>>> polling clip change:"
                #            f"\nnew: {len(new_clip)} >>{new_clip}<<"
                #            f"\nold: {len(self.old_clip)} >>{self.old_clip}<<\n"
                #          )
                # self.logger.debug( msg  )
                #rint( msg )

                self.undo_clip   = new_clip
    #                    new_clip_b       = str( new_clip.encode( 'ascii', 'ignore') )
                           # some uni just does not seem to work
    #                    self.logger.info( "new_clip = " +  new_clip_b  )
                self.old_clip    = new_clip
                ret = new_clip

        return ret

# ---------------
class PyperCliper( ABCCliper  ):
    """
    will be a clipper ... this one for pyperclip
    """
    #----------- init -----------
    def __init__(self,  ):
        """
        See class doc
        """
        super().__init__()
        import pyperclip
        #rint( pyperclip )
        self._clipper               = pyperclip
        #rint( f"created PyperClipper {self}")

    # -----------------------------------
    def get_clipper_text( self, ):
        """
        copy text from self._clipper, just facade to clipper

        """
        text     = self._clipper.paste()
        return text

    # -----------------------------------
    def set_clipper_text( self, a_string ):
        """
        copy text from self._clipper, just facade to clipper
        """
        self._clipper.copy( a_string )

# -----------------------------------
class QtCliper( ABCCliper ):
    """
    implementation for QT
    """
    #----------- init -----------
    def __init__(self,   ):
        """
        See class doc for ABCCliper
        """
        super().__init__()
        from PyQt5.QtWidgets import QApplication
        self._clipper               = QApplication.clipboard()
        #rint( f"__init__ self._clipper >{self._clipper}<"  )

    # -----------------------------------
    def get_clipper_text( self, ):
        """
        copy text from self.clipper, just facade to clipper

        """
        text       = self._clipper.text()
        #rint( f"get_clipper_text >{text}<")
        return text

    # -----------------------------------
    def set_clipper_text( self, a_string ):
        """
        copy text from self.clipper, just facade to clipper

        """
        self._clipper.setText( a_string )

# ===================== eof ==========


