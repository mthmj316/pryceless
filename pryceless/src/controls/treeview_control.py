'''
Created on 25.09.2020

@author: mthoma
'''
from abc import ABC, abstractmethod
from enum import Enum

class TreeViewItem():
    '''
    Represents a item which can be added to the TreeViewControl
    '''
    def __init__(self):
        '''
        '''
        self.__id = None
        self.__is_double_clickable = True
        self.__is_selectable = True
        self.__key = None
        self.__value = None
        self.__parent_id = None
        
    @property
    def id(self):
        '''
        returns the id
        '''
        return self.__id
    
    @id.setter
    def id(self, value):
        '''
        sets the id
        '''
        print('TreeViewItem')
        
    

class TreeViewState(Enum):
    '''
    Represents the state of the TreeViewcontrol.
    OK = Everything is just fine.
    RECURSIV = The currently added TreeViewItem already exists but under another parent. 
    NO_PARENT = The currently added TreeViewItem has no parent.
    PARENT_NOT_EXISTS = The parent of the currently added TreeViewItem hasen't been added, yet.
    ERROR = An error occurred with the effect that the tree cannot be build correctly.   
    '''
    OK = 0
    RECURSIV = 10
    NO_PARENT = 20
    PARENT_NOT_EXISTS = 30
    ERROR = 99    
    

class TreeViewObserver(ABC):
    '''
    classdocs
    '''
    
    @abstractmethod
    def on_double_click(self, item:TreeViewItem) -> None:
        '''
        Is called after a treeview item has been doubled clicked.
        :param item: The item which has been double clicked.
        '''
        
    @abstractmethod
    def on_select(self, item:TreeViewItem) -> None:
        '''
        Is called after a treeview item has been selected
        :param item: selected item
        '''

    @abstractmethod
    def on_error(self, error_msg:str) -> None:
        '''
        Is called after the state of the treeview has been set to ERROR. 
        :param error_msg: The error message.
        '''