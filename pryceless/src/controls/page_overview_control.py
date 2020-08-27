'''
Created on 23.08.2020

@author: mthoma
'''
import tkinter as tk
from tkinter.ttk import Treeview, Style
from typing import List
from abc import ABC, abstractmethod

class PageOverviewControlObserver(ABC):

    @abstractmethod
    def on_page_selected(self, page_id:str) -> None:
        '''
        Is called after a page has been selected.
        page_id -> id of the selected page
        if the root element is selected None will be returned.
        '''
    
class PageOverviewControl(object):
    '''
    classdocs
    '''
    __root_id: str = 'pages'
    
    __observers: List[PageOverviewControlObserver] = []
    
    __overview: Treeview = None
    
    __inserted: List[str] = []
    
    def __init__(self, master:tk.Frame):
        '''
        Constructor

        '''
        self.__overview = Treeview(master=master, selectmode='browse')
        self.__overview.pack(fill=tk.BOTH, side=tk.BOTTOM)
        self.__overview.insert('', 0, self.__root_id, text='Pages')
        self.__overview.item(self.__root_id, open=True)
        #self.__overview.bind('<<TreeviewSelect>>', self.__notifiy_observer)
        
        self.__overview.bind('<Button-1>', self.__notifiy_observer)
        
    def insert_page(self, page_id:str, page_name:str):
        
        self.__inserted.append(page_id)
        
        self.__overview.insert(self.__root_id, 'end', page_id, text=page_name)
        self.__overview.item(page_id, open=True)
        
    def remove_page(self, page_id:str):
        
        self.__remove(page_id)
        self.__inserted.remove(page_id)
        
    def __remove(self, tag_id):
        self.__overview.delete(tag_id)
        
    def remove_all(self):
        
        for page_id in self.__inserted:
            self.__remove(page_id)
            
        self.__inserted.clear()
        
    def add_obeserver(self, observer:PageOverviewControlObserver):
        
        self.__observers.append(observer)
        
    def remove_observer(self, observer:PageOverviewControlObserver):
        
        self.__observers.remove(observer)
        
    def __notifiy_observer(self, event):  # @UnusedVariable
        
        page_id = self.__overview.focus()
        
        if page_id == self.__root_id or page_id == '':
            page_id = None
            
        for observer in self.__observers:
            observer.on_page_selected(page_id)