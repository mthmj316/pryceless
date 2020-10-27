'''
Created on 27.08.2020

@author: mthoma
'''
from abc import ABC, abstractmethod
from typing import List

from tkinter import Frame
import tkinter
from tkinter.constants import BOTH
from tkinter.ttk import Treeview
from utils.logger import log_enter_func, log_leave_func, log_set_var


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
        
        log_enter_func('ConfigurationControl', '__init__', {'master':master})
        
        self.__configuration = Treeview(master=master)
        self.__configuration.heading('#0',text='Configuration',anchor=tkinter.W)
        self.__configuration.pack(fill=BOTH, side=tkinter.LEFT, expand=True)
        self.__configuration.bind('<<TreeviewSelect>>', self.__notifiy_observer)
    
        log_leave_func('ConfigurationControl', '__init__')
    
    def select(self, _id:str):
        
        log_enter_func('ConfigurationControl', 'select', {'_id':_id})
        
        if not _id == None:
            self.__configuration.focus(_id)
            self.__configuration.selection_set(_id)
            
        log_leave_func('ConfigurationControl', 'select')
            
    def insert_conf(self, conf_id:str, conf_name:str, parent:str='confs', pos:str='end'):
        
        log_enter_func('ConfigurationControl', 'insert_conf', 
                       {'conf_id':conf_id, 'conf_name':conf_name, 'parent':parent, 'pos':pos})
        
        if parent == None:
            parent = self.__root_id
            
        log_set_var('ConfigurationControl', 'insert_conf', 'parent', parent)
        
        self.__inserted.append(conf_id)
        self.__configuration.insert(parent, pos, conf_id, text=conf_name)
        self.__configuration.item(conf_id, open=True)
        
        log_leave_func('ConfigurationControl', 'insert_conf')
        
    def __remove(self, conf_id):
        
        log_enter_func('ConfigurationControl', '__remove', {'conf_id':conf_id})
        
        self.__configuration.delete(conf_id)
        
        log_leave_func('ConfigurationControl', '__remove')
        
    def remove_all(self):
        
        log_enter_func('ConfigurationControl', 'remove_all')
        
        for conf_id in self.__inserted:
            if self.__configuration.exists(conf_id):
                self.__remove(conf_id)
            
        self.__inserted.clear()
        
        log_leave_func('ConfigurationControl', 'remove_all')
    
        
    def add_obeserver(self, observer:ConfigurationControlObserver):
        
        log_enter_func('ConfigurationControl', 'add_obeserver', {'observer':observer})
        
        self.__observers.append(observer)
        
        log_leave_func('ConfigurationControl', 'add_obeserver')
        
    def remove_observer(self, observer:ConfigurationControlObserver):
        
        log_enter_func('ConfigurationControl', 'remove_observer', {'observer':observer})
        
        self.__observers.remove(observer)
        
        log_leave_func('ConfigurationControl', 'remove_observer')
        
    def __notifiy_observer(self, event):  # @UnusedVariable
        
        log_enter_func('ConfigurationControl', '__notifiy_observer', {'event':event})
        
        conf_id = self.__configuration.focus()
        
        if conf_id == self.__root_id or conf_id == '':
            conf_id = None
        
        log_set_var('ConfigurationControl', '__notifiy_observer', 'conf_id', conf_id)
            
        for observer in self.__observers:
            observer.on_conf_selected(conf_id)
            
        log_leave_func('ConfigurationControl', '__notifiy_observer')
        
    ###################################################################
    ###################################################################
    ###################################################################