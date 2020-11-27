'''
Created on 04.08.2020

@author: mthoma
'''
from datetime import datetime

from main_window.main_window_cntlr import MainWindowCNTLR
from utils.logger import log_enter_func, log_leave_func, log_set_var


VERSION = ' v0.3'

if __name__ == '__main__':
    
    log_enter_func('application', '__main__')
    
    title = ''.join(['Pryceless', VERSION, ' (2020-',str(datetime.now().year), ')'])
                
    log_set_var('application', '__main__', 'title', title)
    
    main_window = MainWindowCNTLR()
    main_window.show(title)
        
    log_leave_func('application', '__main__')