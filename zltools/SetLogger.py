def _get_logger(self) :
    import logging
    import os
    g = logging.getLogger ( '[.FoldersInfo.]' )
    d = os.path.abspath ( self.log_path )
    h = logging.FileHandler ( os.path.join ( d, self.log_name ) )

    m = logging.Formatter ( '%(asctime)-26s %(name)-16s %(levelname)-8s %(message)s' )
    h.setFormatter ( m )

    g.addHandler ( h )
    g.setLevel ( logging.INFO )
    return g