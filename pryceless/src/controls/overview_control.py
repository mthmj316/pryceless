'''
Created on 23.08.2020

@author: mthoma
'''
from abc import ABC, abstractmethod
from typing import List

import tkinter as tk
from tkinter.ttk import Treeview
from utils.logger import log_enter_func, log_leave_func, log_set_var


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
        log_enter_func('OverviewControl', '__init__', {'master':master})
        
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
        
        log_leave_func('OverviewControl', '__init__')
        
    def select(self, page_id:str):
        
        log_enter_func('OverviewControl', 'select', {'page_id':page_id})
        
        if not page_id == None:
            self.__overview.focus(page_id)
            self.__overview.selection_set(page_id)
        
        log_leave_func('OverviewControl', 'select')
        
    def insert(self, page_id:str, page_name:str):
        
        log_enter_func('OverviewControl', 'insert', {'page_id':page_id, 'page_name':page_name})
        
        self.__inserted.append(page_id)
        
        parent_id = page_id.split(sep='.')[0]
           
        self.__overview.insert(parent_id, 'end', page_id, text=page_name)
        
        log_leave_func('OverviewControl', 'insert')
        
    def remove_page(self, page_id:str):
        
        log_enter_func('OverviewControl', 'remove_page', {'page_id':page_id})
        
        self.__remove(page_id)
        self.__inserted.remove(page_id)
        
        log_leave_func('OverviewControl', 'remove_page')
        
    def __remove(self, tag_id):
        
        log_enter_func('OverviewControl', '__remove', {'tag_id':tag_id})
        
        self.__overview.delete(tag_id)
        
        log_leave_func('OverviewControl', '__remove')
        
    def remove_all(self):
        
        log_enter_func('OverviewControl', 'remove_all')
        
        for page_id in self.__inserted:
            self.__remove(page_id)
            
        self.__inserted.clear()
        
        log_leave_func('OverviewControl', 'remove_all')
        
    def add_obeserver(self, observer:OverviewControlObserver):
        
        log_enter_func('OverviewControl', 'add_obeserver', {'observer':observer})
        
        self.__observers.append(observer)
        
        log_leave_func('OverviewControl', 'add_obeserver')
        
    def remove_observer(self, observer:OverviewControlObserver):
        
        log_enter_func('OverviewControl', 'remove_observer', {'observer':observer})
        
        self.__observers.remove(observer)
        
        log_leave_func('OverviewControl', 'remove_observer')
        
    def __notifiy_observer(self, event):  # @UnusedVariable
        
        log_enter_func('OverviewControl', '__notifiy_observer', {'event':event})
        
        page_id = event.widget.selection()[0]
        
        if '.' not in page_id:
            page_id = None
            
        log_set_var('OverviewControl', '__notifiy_observer', 'page_id', page_id)
            
        for observer in self.__observers:
            observer.on_page_selected(page_id)
        
        log_leave_func('OverviewControl', '__notifiy_observer')
        
    ###################################################################
    ###################################################################
    ###################################################################