'''
Created on 27.08.2020

@author: mthoma
'''
from tkinter import Frame
from abc import ABC, abstractmethod
from typing import List
from tkinter.ttk import Treeview
from tkinter.constants import BOTH
import tkinter

class ConfigurationControlObserver(ABC):

    @abstractmethod
    def on_conf_selected(self, conf_id:str) -> None:
        '''
        Is called after a conf has been selected.
        conf_id -> id of the selected conf
        if the root element is selected None will be returned.
        '''

class ConfigurationControl(object):
    '''
    classdocs
    '''
    __root_id: str = ''
    
    __observers: List[ConfigurationControlObserver] = []
    
    __configuration: Treeview = None
    
    __inserted: List[str] = []


    def __init__(self, master:Frame):
        '''
        Constructor
        '''
        self.__configuration = Treeview(master=master)
        self.__configuration.heading('#0',text='Configuration',anchor=tkinter.W)
        self.__configuration.pack(fill=BOTH, side=tkinter.LEFT, expand=True)
        #self.__configuration.insert('', 0, self.__root_id, text='Configuration')
        #self.__configuration.item(self.__root_id, open=True)
        self.__configuration.bind('<<TreeviewSelect>>', self.__notifiy_observer)
    
    
    def insert_conf(self, conf_id:str, conf_name:str, parent:str='confs', pos:str='end'):
        
        if parent == None:
            parent = self.__root_id
        
        self.__inserted.append(conf_id)
        self.__configuration.insert(parent, pos, conf_id, text=conf_name)
        
    def __remove(self, conf_id):
        self.__configuration.delete(conf_id)
        
    def remove_all(self):
        
        for conf_id in self.__inserted:
            if self.__configuration.exists(conf_id):
                self.__remove(conf_id)
            
        self.__inserted.clear()
    
        
    def add_obeserver(self, observer:ConfigurationControlObserver):
        
        self.__observers.append(observer)
        
    def remove_observer(self, observer:ConfigurationControlObserver):
        
        self.__observers.remove(observer)
        
    def __notifiy_observer(self, event):  # @UnusedVariable
        
        conf_id = self.__configuration.focus()
        
        if conf_id == self.__root_id or conf_id == '':
            conf_id = None
            
        for observer in self.__observers:
            observer.on_conf_selected(conf_id)
        