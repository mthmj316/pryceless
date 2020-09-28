'''
Created on 04.08.2020

@author: mthoma
'''
from gi import overrides
from typing import List

from gui.abs_html_page_config_ui import ABSHTMLPageConfigUI
from scripts.html_element import HTMLElement
import tkinter as tk
from tkinter.ttk import Treeview
import tkinter.ttk as ttk
from utils.observer import Observer


class HTMLPageConfigUI(tk.Frame, ABSHTMLPageConfigUI):
    '''
    classdocs
    '''
    
    __observers: List[Observer] = []
    __tree: Treeview = None
    
    def __init__(self, master):
        '''
        Constructor
        '''        
        self.__tree = ttk.Treeview(master)
    
    @overrides(ABSHTMLPageConfigUI)   
    def insert(self, tag:HTMLElement)->None:
        pass
    
    @overrides(ABSHTMLPageConfigUI)    
    def remove(self, tag:HTMLElement)->None:
        pass

    @overrides(ABSHTMLPageConfigUI)
    def update(self, tag:HTMLElement) -> None:
        '''
        '''
        pass
    
    @overrides(ABSHTMLPageConfigUI)    
    def clear(self) -> None:
        '''
        '''
        pass
    
    @overrides(ABSHTMLPageConfigUI)  
    def move(self, tag: HTMLElement) -> None:
        '''
        '''
        pass

    @overrides(ABSHTMLPageConfigUI)
    def get_selected(self) -> str:
        '''
        Returns the id of the selected html tag
        '''
        pass     

    @overrides(ABSHTMLPageConfigUI)
    def register(self, observer: Observer) -> None:
        self.__observers.append(observer)
        
    @overrides(ABSHTMLPageConfigUI)
    def unregister(self, observer:Observer)->None:
        self.__observers.remove(observer)
        
    @overrides(ABSHTMLPageConfigUI) 
    def notify(self)->None:
        
        for observer in self.__observers:
            observer.update(self)   
        
'''

def __init__(self, master=None, **kw):
        ttk.Treeview.__init__(self, master, **kw)

        self._curfocus = None
        self._inplace_widgets = {}
        self._inplace_widgets_show = {}
        self._inplace_vars = {}
        self._header_clicked = False
        self._header_dragged = False

        # Wheel events?
        self.bind('<<TreeviewSelect>>', self.check_focus)
        self.bind('<4>', lambda e: self.after_idle(self.__updateWnds))
        self.bind('<5>', lambda e: self.after_idle(self.__updateWnds))
        self.bind('<KeyRelease>', self.check_focus)
        self.bind('<Home>', functools.partial(self.__on_key_press, 'Home'))
        self.bind('<End>', functools.partial(self.__on_key_press, 'End'))
        self.bind('<Button-1>', self.__on_button1)
        self.bind('<ButtonRelease-1>', self.__on_button1_release)
        self.bind('<Motion>', self.__on_mouse_motion)
        self.bind('<Configure>', lambda e: self.after_idle(self.__updateWnds)) 


import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

tree["columns"]=("one","two","three")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.column("one", width=150, minwidth=150, stretch=tk.NO)
tree.column("two", width=400, minwidth=200)
tree.column("three", width=80, minwidth=50, stretch=tk.NO)


tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Date modified",anchor=tk.W)
tree.heading("two", text="Type",anchor=tk.W)
tree.heading("three", text="Size",anchor=tk.W)


# Level 1
folder1=tree.insert("", 1, "", text="Folder 1", values=("23-Jun-17 11:05","File folder",""))
tree.insert("", 2, "", text="text_file.txt", values=("23-Jun-17 11:25","TXT file","1 KB"))
# Level 2
tree.insert(folder1, "end", "", text="photo1.png", values=("23-Jun-17 11:28","PNG file","2.6 KB"))
tree.insert(folder1, "end", "", text="photo2.png", values=("23-Jun-17 11:29","PNG file","3.2 KB"))
tree.insert(folder1, "end", "", text="photo3.png", values=("23-Jun-17 11:30","PNG file","3.1 KB"))

tree.pack(side=tk.TOP,fill=tk.X)     
'''
        