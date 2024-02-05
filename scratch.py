    # ------------------------------------------


   # -----------------------------------------
   def get_long_lat_filter_function( self,  ):


  # ------------------------------
  def _sort_filter_gpx_data( self, gpx_data ):




    # ----------------------------------
    def main( self ):
        """

        """
        pass  # just create should be enouth ?
        print( "this  ")












  # ------------------------------
  def gui_make_map_from_gpx_file ( self, ):
      """
      Purpose
          what is says
          this is old version which does not make photoPlus points

      Arg
          use file_name from gui for directory

      """
      start_time = time.time()
      AppGlobal.gui.clear_message_area()
      file_name    = self.gui.get_browse()
      msg     = f"Make map from *.GPX file using file {file_name}"
      AppGlobal.gui.write_gui( msg )

      try:
          gpx          = self._gpx_from_gpxfile( file_name )
          self._gpx_to_map( gpx )

      except app_exceptions.ReturnToGui  as an_except:
          msg  = f"File Load failed, {an_except.why}"
          print( msg )
          AppGlobal.gui.write_gui( msg )

      except app_exceptions.ApplicationError  as an_except:
          msg  = f"File Load failed, {an_except.why}"
          print( msg )
          AppGlobal.gui.write_gui( msg )

      end_time    = time.time()
      run_time    = round( end_time - start_time, 2 )
      msg         = f"End of Make Map from GPX file... run time {run_time} sec"
      print( msg )
      AppGlobal.gui.write_gui( msg )



    def _gpx_from_gpxfile( self,  file_name ):
        """
        required in vers 2023 12 03.01
            file_name needs to be a *.gpx file name
        returns
            gpx
        """
        # next migh be a function ??
        # chdek none
        if file_name is None:
            msg   = "File name is None, so cannot be processed to make a gpx"
            self.gui.write_gui( msg )
            raise app_exceptions.ReturnToGui( msg )

        # check extension
        file_path    = pathlib.Path( file_name )

        if file_path.suffix != ".gpx":  # consider lower
            msg   = f"File name {file_name} is a not gpx file, so cannot be processed to make a gpx"
            self.gui.write_gui( msg )
            raise app_exceptions.ReturnToGui( msg )

        # check exist
        if not file_path.exists():
            msg   = f"File name {file_name} is not a file that exists, so cannot be processed to make a gpx"
            self.gui.write_gui( msg )
            raise app_exceptions.ReturnToGui( msg )

        with open( file_path, 'r' ) as readFile:
            gpx = gpxpy.parse( readFile )

        msg    = f"Made gpx object from {file_name}"
        print( msg )
        self.gui.write_gui( msg )

        return gpx