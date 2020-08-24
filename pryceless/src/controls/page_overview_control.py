'''
Created on 23.08.2020

@author: mthoma
'''
import tkinter as tk
from tkinter import StringVar
from tkinter.ttk import Treeview

class PageOverviewControl(object):
    '''
    classdocs
    '''
    def __init__(self, master:tk.Frame, header:str):
        '''
        Constructor

        '''
        label_text_var = StringVar()
        
        header_label = tk.Label(master=master, textvariable=label_text_var)
        label_text_var.set(header)
        header_label.propagate(False)
        
        header_label.pack(side=tk.TOP, anchor=tk.W)
        
        overview = Treeview(master=master)
        overview.pack(fill=tk.BOTH, side=tk.BOTTOM)
        overview.propagate(False)
        
        overview.insert('', 0, 'project', text='Pages')
        