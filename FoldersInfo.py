import os
from os.path import join, getsize
from zltools import SetLogger

class FoldersInfo():
    # log_path = 'C:\PycharmProjects\pythonProject\logs\\'
    log_name = 'FoldersInfo.log'
    def __init__(self,dir,limitSizeMb:int):
        g = SetLogger._get_logger(self.log_name)
        for root, dirs, files in os.walk ( dir ) :
            try :
                size = sum ( [ getsize ( join ( root, name ) ) for name in files ] ) / 1000000
                if size > limitSizeMb :
                    print ( root, "consumes", end=" " )
                    print ( size, end=" " )
                    print ( "MB in", len ( files ), "non-directory files" )
                    if 'CVS' in dirs :
                        dirs.remove ( 'CVS' )  # don't visit CVS directories
            except Exception as e :
                g.info(f'Error:{e},{root}')
                # print ( f'Error:{e},{root}' )

    # def _get_logger(self) :
    #     import logging
    #     g = logging.getLogger ( '[.FoldersInfo.]' )
    #     d = os.path.abspath(self.log_path)
    #     h = logging.FileHandler ( os.path.join ( d, self.log_name ) )
    #
    #     m = logging.Formatter ( '%(asctime)-26s %(name)-16s %(levelname)-8s %(message)s' )
    #     h.setFormatter ( m )
    #
    #     g.addHandler ( h )
    #     g.setLevel ( logging.INFO )
    #     return g

if __name__ == '__main__':
    dirs = 'C:/'
    FoldersInfo(dirs, 1000)