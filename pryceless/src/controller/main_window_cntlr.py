'''
Created on 04.08.2020

@author: mthoma
'''
from model.main_window_mo import MainWindowMO
from gui.main_window_ui import MainWindowUI

class MainWindowCNTLR(object):
    '''
    classdocs
    '''

    __model: MainWindowMO = MainWindowMO()
    __ui: MainWindowUI = MainWindowUI()

    def __init__(self, params):
        '''
        Constructor
        '''
        
        