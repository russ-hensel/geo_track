# -*- coding: utf-8 -*-

"""

Purpose:
    part of my ( rsh ) library of reusable code 
    a library module for multiple applications
    sometimes included with applications but not used
        as this make my source code management easier.
        
        
Line style generates linestyles and markers one by one for matplotlib
see class description and code 

todo
    !! names should be changed from camel case 



# history
    master in rsh_lib  -- move example here or this to examples
    last updated from:
    rsh_lib  july 2020




# D:\Russ\0000\python00\python3\_projects\solar_city_plot\line_style.py
D:\Russ\0000\python00\python3\_projects\smart_plug\line_style.py
D:\Russ\0000\python00\python3\_examples\Instructables\AdvDataLogging\Instruct1\line_style.py
D:\Russ\0000\python00\python3\_examples\Instructables\AdvDataLogging\line_style.py
D:\Russ\0000\python00\python3\_projects\AdvDataLogging\line_style.py
D:\Russ\0000\python00\python3\_projects\rshlib\line_style.py
D:\Russ\0000\python00\python3\_projects\AdvDataLogging\Instruct1\line_style.py



# see also

#  markerfacecolor
#  linewidth or lw
"""


class LineStyle():
    """
    dispenses row by row a tuple of row style types to
    help make it easy to tell graph lines apart
    use instead of mathplot defaults
    use:
        sys.path.append( "../rshlib" )
        import line_style

        self.line_style     = line_style.LineStyle()

        self.current_style  = self.lineStyle.getNextStyle()  # ( line, color, marker, width )
        .....plot(  x, y, label= alabel, linestyle = self.current_style[0],   color     = self.current_style[1],
                                         marker    = self.current_style[2] ,  linewidth = self.current_style[3]  )

        self.line_style.reset()      # for a new set
        !!consider changing to named tuple
    """
    # -----------------------------------------------
    def __init__(self ):
        """
        ideally number in each category is relatively prine
        """
        self.lines       = [  '-', '--', ':' ]  #   "-." "_" total of 4 ??
        self.line_ix     = 0
        self.max_line    = len( self.lines  )

        # pick colors that are easily distinguishable
        self.colors      = [ 'red', 'blue', 'cyan', 'green', 'black' ]   # want dark colors yellow and orange are light
        self.color_ix    = 0
        self.max_color   = len( self.colors  )

        self.markers     = [ 'o', 'x', '+', '*', 'h', 's', "d", "2" ]       # "1" ......23   "4"
        self.marker_ix   = 0
        self.max_marker  = len( self.markers  )

        # too wide messes up graphs small ones in particular
        self.widths      = [ 1, 2, 3, 4 ]       # "1" ......23   "4"
        self.max_width   = len( self.widths  )

        #  *>url  https://stackoverflow.com/questions/8409095/matplotlib-set-markers-for-individual-points-on-a-line

        self.reset()
    # -----------------------------------------------
    def reset( self, ):
        """
        reset for reuse from beginning

        """
        self.marker_ix   = 0
        self.color_ix    = 0
        self.line_ix     = 0
        self.width_ix    = 0

    # -----------------------------------------------
    def _getNextWidth_( self, ):
        """
        inside class use only,
        get next line style
        """

        ret       = self.widths[ self.width_ix ]
        self.width_ix  += 1
        if self.width_ix >= self.max_width:
            self.width_ix = 0
        return ret

    # -----------------------------------------------
    def _getNextLine_( self, ):
        """
        inside class use only,
        get next line style
        """
        ret       = self.lines[ self.line_ix ]
        self.line_ix  += 1
        if self.line_ix >= self.max_line:
            self.line_ix = 0
        return ret

    # -----------------------------------------------
    def _getNextColor_( self, ):
        """
        inside class use only,
        get next color style
        """
        ret       = self.colors[ self.color_ix ]
        self.color_ix  += 1
        if self.color_ix >= self.max_color:
            self.color_ix = 0
        return ret

    # -----------------------------------------------
    def _getNextMarker_( self, ):
        """
        inside class use only,
        get next marker style
        """
        ret       = self.markers[ self.marker_ix ]
        self.marker_ix  += 1
        if self.marker_ix >= self.max_marker:
            self.marker_ix = 0
        return ret

    # -----------------------------------------------
    def to_str( self,  ):
        ret_str    = ""
        ret_str    = f"{ret_str}\n    there are {self.max_line} linestyle {self.lines}"
        ret_str    = f"{ret_str}\n    there are {self.max_color} colors    {self.colors}"

        return ret_str
    # -----------------------------------------------
    def getNextStyle( self,  ):
        """
        get the next tuple: ( line, color, marker )
        return tuple see below !! change to named tuple ??
        """
        return ( self._getNextLine_() , self._getNextColor_(), self._getNextMarker_(), self._getNextWidth_()  )

# =========================== put a test ===================
 

# ------------------------------------------------
if __name__ == '__main__':
    """
    run the application as an object
    """
    test   = LineStyle()

    print( test.to_str())


    for ix in range(0,10 ):
        print(test.getNextStyle())
