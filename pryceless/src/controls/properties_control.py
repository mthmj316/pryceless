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
    def on_property_selected(self, page_id:str) -> None:
        '''
        Is called after a page has been selected.
        page_id -> id of the selected page
        if the root element is selected None will be returned.
        '''
    
class PropertiesControl(object):
    '''
    classdocs
    '''
    __root_id: str = ''
    
    __observers: List[PropertiesControlObserver] = []
    
    __properties: Treeview = None
    
    __inserted: List[str] = []
    
    def __init__(self, master:tk.Frame):
        '''
        Constructor

        '''
        self.__properties = Treeview(master=master, columns=("#1"))
        self.__properties.column('#0', stretch=tk.NO)
        self.__properties.heading('#0',text='Key',anchor=tk.W)
        self.__properties.heading('#1',text='Value',anchor=tk.W)
        self.__properties.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.__properties.bind('<Double-1>', self.__notifiy_observer)
        
    def insert(self, _id:str, key:str, value:str):
        
        self.__inserted.append(_id)
        self.__properties.insert(self.__root_id, 'end', _id, text=key, values=[value])
        
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
        
    def __notifiy_observer(self, event):
        
        _id = event.widget.selection()[0]
        
        if '.' not in _id:
            _id = None
            
        for observer in self.__observers:
            observer.on_property_selected(_id)