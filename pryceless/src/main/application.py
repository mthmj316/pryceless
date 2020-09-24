'''
Created on 04.08.2020

@author: mthoma
'''
from main_window.main_window_cntlr import MainWindowCNTLR
from datetime import datetime

VERSION = ' v0.3'

if __name__ == '__main__':
    
    title = ''.join(['Pryceless', VERSION, ' (2020-',str(datetime.now().year), ')'])
    
    print('application    starting ' + title)
    
    main_window = MainWindowCNTLR()
    main_window.show(title)