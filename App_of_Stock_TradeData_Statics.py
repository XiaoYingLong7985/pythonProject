import sys
import pyqtgraph as pg
from PyQt5 import QtGui,QtCore,QtWidgets
from threading import Thread
import logging
import inspect
import os

class MyLogging():

    def __init__(self):
        logger = self._get_logger()

    def _get_logger(self):
        logger = logging.getLogger ( '[APP_Stock_Statics]' )
        this_file = inspect.getfile ( inspect.currentframe () )
        dir_path = os.path.abspath ( os.path.dirname ( __file__ ) )
        handler = logging.FileHandler ( os.path.join ( dir_path, "APP_SSS.log" ) )
        formatter = logging.Formatter ( '%(asctime)s %(name)-12s %(levelname)-8s %(message)s' )
        handler.setFormatter ( formatter )
        logger.addHandler ( handler )
        logger.setLevel ( logging.INFO )
        return logger

