def _get_logger(log_name) :
    import logging
    import os
    log_path = 'C:\PycharmProjects\pythonProject\logs/'
    g = logging.getLogger ( '[.FoldersInfo.]' )
    d = os.path.abspath ( log_path )
    h = logging.FileHandler ( os.path.join ( d, log_name ) )

    m = logging.Formatter ( '%(asctime)-26s %(name)-16s %(levelname)-8s %(message)s' )
    h.setFormatter ( m )

    g.addHandler ( h )
    g.setLevel ( logging.INFO )
    return g