'''
Created on 23.08.2020

@author: mthoma
'''
import tkinter as tk

class PageOverviewControl(object):
    '''
    classdocs
    '''
    def __init__(self, master:tk.Frame, header:str):
        '''
        Constructor
        '''
        
        print(master.winfo_reqwidth())
        
        
        header_frame = tk.Frame(master, bg='#231526', 
                                width=master.winfo_reqwidth(),
                                height=master.winfo_reqheight())
        
        header_frame.grid(row=0, column=0, rowspan=1, columnspan=1)
        header_frame.grid_propagate(False)
        
        header_label = tk.Label(master=header_frame, width=master.winfo_reqwidth())
        header_label.configure(text=header)
        header_label.grid(sticky=tk.W)
        header_label.grid_propagate(False)
        
        print(header_label.winfo_width())
        