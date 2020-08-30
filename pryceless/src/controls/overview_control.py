'''
Created on 23.08.2020

@author: mthoma
'''
import tkinter as tk
from tkinter.ttk import Treeview
from typing import List
from abc import ABC, abstractmethod

class OverviewControlObserver(ABC):

    @abstractmethod
    def on_page_selected(self, page_id:str) -> None:
        '''
        Is called after a page has been selected.
        page_id -> id of the selected page
        if the root element is selected None will be returned.
        '''
    
class OverviewControl(object):
    '''
    classdocs
    '''
    __root_id: str = 'pages'
    
    __observers: List[OverviewControlObserver] = []
    
    __overview: Treeview = None
    
    __inserted: List[str] = []
    
    def __init__(self, master:tk.Frame):
        '''
        Constructor

        '''
        self.__overview = Treeview(master=master, selectmode='browse')
        self.__overview.heading('#0',text='Overview',anchor=tk.W)
        self.__overview.pack(fill=tk.Y, side=tk.LEFT)
        self.__overview.bind('<<TreeviewSelect>>', self.__notifiy_observer)
        
        self.__overview.insert('', 0, self.__root_id, text='Pages')
        self.__overview.item(self.__root_id, open=True)
        
        self.__overview.insert('', 1, 'css_rules', text='CSS Rules')
        self.__overview.item('css_rules', open=True)
        
        self.__overview.insert('', 2, 'javascripts', text='JavaScripts')
        self.__overview.item('javascripts', open=True)
        
        self.__overview.insert('', 3, 'text', text='Text')
        self.__overview.item('text', open=True)
        
        self.__overview.insert('', 4, 'variables', text='Variables')
        self.__overview.item('variables', open=True)
        
    def select(self, page_id:str):
        
        if not page_id == None:
            self.__overview.focus(page_id)
            self.__overview.selection_set(page_id)
        
    def insert(self, page_id:str, page_name:str):
        
        self.__inserted.append(page_id)
        
        parent_id = page_id.split(sep='.')[0]
           
        self.__overview.insert(parent_id, 'end', page_id, text=page_name)
        
        
    def remove_page(self, page_id:str):
        
        self.__remove(page_id)
        self.__inserted.remove(page_id)
        
    def __remove(self, tag_id):
        self.__overview.delete(tag_id)
        
    def remove_all(self):
        
        for page_id in self.__inserted:
            self.__remove(page_id)
            
        self.__inserted.clear()
        
    def add_obeserver(self, observer:OverviewControlObserver):
        
        self.__observers.append(observer)
        
    def remove_observer(self, observer:OverviewControlObserver):
        
        self.__observers.remove(observer)
        
    def __notifiy_observer(self, event):  # @UnusedVariable
        
        page_id = event.widget.selection()[0]
        
        if '.' not in page_id:
            page_id = None
            
        for observer in self.__observers:
            observer.on_page_selected(page_id)