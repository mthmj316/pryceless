'''
Created on 25.09.2020

@author: mthoma
'''
from abc import ABC, abstractmethod
from enum import Enum

from utils.logger import log_getter, log_setter, log_delete,\
    create_key_value_str


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
    def parent_id(self):
        '''
        returns the __parent_id
        '''
        log_getter('TreeViewItem', '__parent_id', self.__parent_id)
        return self.__key
    
    @parent_id.setter
    def parent_id(self, value):
        '''
        sets the __parent_id
        '''
        log_setter('TreeViewItem', '__parent_id', self.__parent_id)
        self.__parent_id = value
        
    @parent_id.delete
    def parent_id(self):
        '''
        Deletes the __parent_id attribute
        '''
        log_delete('TreeViewItem', '__parent_id')
        del self.__parent_id
        
    @property
    def value(self):
        '''
        returns the __value
        '''
        log_getter('TreeViewItem', '__value', self.__value)
        return self.__key
    
    @value.setter
    def value(self, value):
        '''
        sets the __value
        '''
        log_setter('TreeViewItem', '__value', self.__value)
        self.__value = value
        
    @value.delete
    def value(self):
        '''
        Deletes the __value attribute
        '''
        log_delete('TreeViewItem', '__value')
        del self.__value

    @property
    def key(self):
        '''
        returns the __key
        '''
        log_getter('TreeViewItem', '__key', self.__key)
        return self.__key
    
    @key.setter
    def key(self, value):
        '''
        sets the __key
        '''
        log_setter('TreeViewItem', '__key', self.__key)
        self.__key = value
        
    @key.delete
    def key(self):
        '''
        Deletes the __key attribute
        '''
        log_delete('TreeViewItem', '__key')
        del self.__key
        
    @property
    def is_selectable(self):
        '''
        returns the __is_selectable
        '''
        log_getter('TreeViewItem', '__is_selectable', self.__is_selectable)
        return self.__is_selectable
    
    @is_selectable.setter
    def is_selectable(self, value):
        '''
        sets the __is_selectable
        '''
        log_setter('TreeViewItem', '__is_selectable', self.__is_selectable)
        self.__is_selectable = value
        
    @is_selectable.delete
    def is_selectable(self):
        '''
        Deletes the __is_selectable attribute
        '''
        log_delete('TreeViewItem', '__is_selectable')
        del self.__is_selectable
      
    @property
    def is_double_clickable(self):
        '''
        returns the __is_double_clickable
        '''
        log_getter('TreeViewItem', '__is_double_clickable', self.__is_double_clickable)
        return self.__is_double_clickable
    
    @is_double_clickable.setter
    def is_double_clickable(self, value):
        '''
        sets the __is_double_clickable
        '''
        log_setter('TreeViewItem', '__is_double_clickable', self.__is_double_clickable)
        self.__is_double_clickable = value
        
    @is_double_clickable.delete
    def is_double_clickable(self):
        '''
        Deletes the __is_double_clickable attribute
        '''
        log_delete('TreeViewItem', '__is_double_clickable')
        del self.__is_double_clickable
        
    @property
    def id(self):  # @DontTrace
        '''
        returns the __id
        '''
        log_getter('TreeViewItem', '__id', self.__id)
        return self.__id
    
    @id.setter
    def id(self, value):  # @DontTrace
        '''
        sets the id
        '''
        log_setter('TreeViewItem', '__id', self.__id)
        self.__id = value
        
    @id.delete
    def id(self):  # @DontTrace
        '''
        Deletes the id attribute
        '''
        log_delete('TreeViewItem', '__id')
        del self.__id
        
    def __str__(self):
        return ' '.join([create_key_value_str('__id', self.__id),
                         create_key_value_str('__is_double_clickable', self.__is_double_clickable),
                         create_key_value_str('__is_selectable', self.__is_selectable),
                         create_key_value_str('key', self.__key),
                         create_key_value_str('value', self.__value),
                         create_key_value_str('__parent_id', self.__parent_id)])
        

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