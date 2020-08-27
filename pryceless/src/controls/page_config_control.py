'''
Created on 27.08.2020

@author: mthoma
'''
from tkinter import Frame
from abc import ABC, abstractmethod
from typing import List
from tkinter.ttk import Treeview
from tkinter.constants import BOTH, BOTTOM

class PageConfigControlObserver(ABC):

    @abstractmethod
    def on_tag_selected(self, tag_id:str) -> None:
        '''
        Is called after a tag has been selected.
        tag_id -> id of the selected tag
        if the root element is selected None will be returned.
        '''

class PageConfigControl(object):
    '''
    classdocs
    '''
    __root_id: str = 'tags'
    
    __observers: List[PageConfigControlObserver] = []
    
    __overview: Treeview = None
    
    __inserted: List[str] = []


    def __init__(self, master:Frame):
        '''
        Constructor
        '''
        self.__overview = Treeview(master=master)
        self.__overview.pack(fill=BOTH, side=BOTTOM)
        self.__overview.insert('', 0, self.__root_id, text='Configuration')
        self.__overview.item(self.__root_id, open=True)
        self.__overview.bind('<<TreeviewSelect>>', self.__notifiy_observer)
    
    
    def insert_tag(self, tag_id:str, tag_name:str, parent:str='tags', pos:str='end'):
        
        self.__inserted.append(tag_id)
        self.__overview.insert(parent, pos, tag_id, text=tag_name)
    
    def append_tag(self, tag_id:str, tag_name:str):
        
        self.insert_tag(tag_id, tag_name)
        
        
    def remove_tag(self, tag_id:str):
        
        self.__remove(tag_id)
        self.__inserted.remove(tag_id)
        
    def __remove(self, tag_id):
        self.__overview.delete(tag_id)
        
    def remove_all(self):
        
        for tag_id in self.__inserted:
            self.__remove(tag_id)
            
        self.__inserted.clear()
    
        
    def add_obeserver(self, observer:PageConfigControlObserver):
        
        self.__observers.append(observer)
        
    def remove_observer(self, observer:PageConfigControlObserver):
        
        self.__observers.remove(observer)
        
    def __notifiy_observer(self, event):  # @UnusedVariable
        
        tag_id = self.__overview.focus()
        
        if tag_id == self.__root_id or tag_id == '':
            tag_id = None
            
        for observer in self.__observers:
            observer.on_page_selected(tag_id)
        