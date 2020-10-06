'''
Created on 25.09.2020

@author: mthoma
'''
from abc import ABC, abstractmethod
from enum import Enum

from utils.logger import log_getter, log_setter, log_delete,\
    create_key_value_str, log_enter_func, log_leave_func


class TreeViewItem():
    '''
    Represents a item which can be added to the TreeViewControl
    '''
    def __init__(self):
        '''
        '''
        log_enter_func('TreeViewItem', '__init__')
        
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


class TreeViewConfiguration():
    '''
    Defines the configuration of the TreeView UI.
    Currently only the number of columns and their headers can be defined.
    '''
    
    def __init__(self):
        '''
        '''
        log_enter_func('TreeViewConfiguration', '__init__')
        
        self.__column_count:int = 0
        self.__column_names:str = []
    
    @property
    def column_names(self):  # @DontTrace
        '''
        returns the __column_names
        '''
        log_getter('TreeViewConfiguration', '__column_names', self.__column_names)
        return self.__column_names
    
    @column_names.delete
    def column_names(self):  # @DontTrace
        '''
        Deletes the __column_names attribute
        '''
        log_delete('TreeViewConfiguration', '__column_names')
        self.__column_names = []
        
    def add_column_name(self, name:str, idx:int):
        '''
        Adds the given name to the column name array
        :param name: Column name to be added
        :param idx: The index of the column. If idx < 0 the name will be appended.
        '''
        log_enter_func('TreeViewConfiguration', 'add_column_name', {'name':name,'idx':idx})
        if idx < 0:
            self.__column_names.append(name)
        else:
            self.__column_names.insert(idx, name)
        
        
    @property
    def column_count(self):  # @DontTrace
        '''
        returns the __column_count
        '''
        log_getter('TreeViewConfiguration', '__column_count', self.__column_count)
        return self.__column_count
    
    @column_count.setter
    def column_count(self, value):  # @DontTrace
        '''
        sets the __column_count
        '''
        log_setter('TreeViewConfiguration', '__column_count', self.__column_count)
        self.__column_count = value
        
    @column_count.delete
    def column_count(self):  # @DontTrace
        '''
        Deletes the __column_count attribute
        '''
        log_delete('TreeViewConfiguration', '__column_count')
        del self.__column_count
        
    def __str__(self):
        return ' '.join([create_key_value_str('__column_count', self.__column_count),
                         create_key_value_str('__column_names', self.__column_names)])


class TreeViewControl():
    '''
    
    '''
    def __init__(self, treeview_config:TreeViewConfiguration=None):
        '''
        
        :param tree_config: TreeViewConfiguration
        '''
        log_enter_func('TreeViewControl', '__init__', {'tree_config':treeview_config})
        
        #Contains all TreeViewItems added to the TreeView
        self.__added_treeview_items = []
        #Is the item which is currently about to be added to the tree. 
        self.__current_treeview_item = None
        #Contains the error message if the state is set to ERROR.
        #This is optional! It is not said that there is an message if an error occurs.
        self.__error_message = None
        #State of the TreeViewControl
        self.__treeview_state
        #Contains all registered observers.
        self.__observers = []
        #This array contains all TreeViewItem for which the parent element was not added
        #at the time as they were added.
        self.__parentless_items = []
        #UI Treeview element.
        self.__treeview = None
        #Contains the mapping of the treeview_id and the corresponding TreeViewItem.
        self.__treeview_id_dict = {}

    ### public methods ###################################################################
        
    ######################################################################################
        
    ### private methods ##################################################################
    def __build_tree(self, treeview_config):
        '''
        Build the basic setup of the treeview by considering treeview_config.
        :param treeview_config:
        '''
        log_enter_func('TreeViewControl', '__build_tree', {'tree_config':treeview_config})
        
        log_leave_func('TreeViewControl', '__build_tree')
        
    
    def __create_treeview_id(self):
        '''
        Creates the temporary id and sets it in the current TreeViewItem.
        '''
        log_enter_func('TreeViewControl', '__create_treeview_id')
        
        log_leave_func('TreeViewControl', '__create_treeview_id')
    
    
    def __get_treeview_id(self, _id) -> str:
        '''
        Searches the __treeview_id_dict mapping for the TreeViewItem (value) for 
        item with TreeViewItem.id == __id, and, if found, returns the key of the
        mapping entry.
        :param _id: The id of the TreeViewItem 
        '''
        log_enter_func('TreeViewControl', '__get_treeview_id', {'_id':_id})
        
        treeview_id = None
        
        log_leave_func('TreeViewControl', '__get_treeview_id', treeview_id)
        
    def __notify_on_double_click(self, event):
        '''
        Event handler for the double click event.
        Calls the just the __notify_on_selection_event with is_double_click == True.
        :param event: Double click event, contains the treeview_id of the double clicked TreeViewItem
        '''
        log_enter_func('TreeViewControl', '__notify_on_double_click', {'event':event})
        
        
        log_leave_func('TreeViewControl', '__notify_on_double_click')
    
    ######################################################################################
        
        
