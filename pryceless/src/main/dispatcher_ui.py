'''
Created on 04.08.2020

@author: mthoma
'''
from main_window.main_window_cntlr import MainWindowCNTLR

__main_window: MainWindowCNTLR = None

def dispatch_main_window():
    
    global __main_window
    
    if __main_window == None:
        __main_window = MainWindowCNTLR()
    
    return __main_window
