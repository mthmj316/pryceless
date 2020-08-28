'''
Created on 23.08.2020

@author: mthoma
'''
import tkinter as tk
from tkinter.ttk import Treeview
from typing import List
from abc import ABC, abstractmethod

class PropertiesControlObserver(ABC):

    @abstractmethod
    def on_selected(self, page_id:str) -> None:
        '''
        Is called after a page has been selected.
        page_id -> id of the selected page
        if the root element is selected None will be returned.
        '''
    
class PropertiesControl(object):
    '''
    classdocs
    '''
    __root_id: str = 'properties'
    
    __observers: List[PropertiesControlObserver] = []
    
    __properties: Treeview = None
    
    __inserted: List[str] = []
    
    def __init__(self, master:tk.Frame):
        '''
        Constructor

        '''
        self.__properties = Treeview(master=master, selectmode='browse')
        self.__properties.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.__properties.bind('<Double-1>', self.__notifiy_observer)
        
        self.__properties.insert('', 0, self.__root_id, text='Properties')
        self.__properties.item(self.__root_id, open=True)
        
    def insert(self, _id:str, key:str, value:str):
        
        self.__inserted.append(key)
           
        self.__properties.insert(self.__root_id, 'end', key, text=value)
        
    def __remove(self, tag_id):
        self.__properties.delete(tag_id)
        
    def remove_all(self):
        
        for page_id in self.__inserted:
            self.__remove(page_id)
            
        self.__inserted.clear()
        
    def add_obeserver(self, observer:PropertiesControlObserver):
        
        self.__observers.append(observer)
        
    def remove_observer(self, observer:PropertiesControlObserver):
        
        self.__observers.remove(observer)
        
    def __notifiy_observer(self, event):  # @UnusedVariable
        
        key = event.widget.selection()[0]
        
        if '.' not in key:
            page_id = None
            
        for observer in self.__observers:
            observer.on_page_selected(key)