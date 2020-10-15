'''
Created on 25.09.2020

@author: mthoma
'''
from abc import ABC, abstractmethod
from enum import Enum

from utils.logger import log_getter, log_setter, log_delete,\
    create_key_value_str, log_enter_func, log_leave_func, log_set_var
import uuid

import tkinter as tk
from tkinter.ttk import Treeview


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
        
        log_leave_func('TreeViewItem', '__init__')
        
    @property
    def parent_id(self):
        '''
        returns the __parent_id
        '''
        log_getter('TreeViewItem', '__parent_id', self.__parent_id)
        return self.__parent_id
    
    @parent_id.setter
    def parent_id(self, value):
        '''
        sets the __parent_id
        '''
        self.__parent_id = value
        log_setter('TreeViewItem', '__parent_id', self.__parent_id)
        
    @parent_id.deleter
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
        return self.__value
    
    @value.setter
    def value(self, value):
        '''
        sets the __value
        '''
        self.__value = value
        log_setter('TreeViewItem', '__value', self.__value)
        
    @value.deleter
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
        self.__key = value
        log_setter('TreeViewItem', '__key', self.__key)
        
    @key.deleter
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
        self.__is_selectable = value
        log_setter('TreeViewItem', '__is_selectable', self.__is_selectable)
        
    @is_selectable.deleter
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
        self.__is_double_clickable = value
        log_setter('TreeViewItem', '__is_double_clickable', self.__is_double_clickable)
        
    @is_double_clickable.deleter
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
        self.__id = value
        log_setter('TreeViewItem', '__id', self.__id)
        
    @id.deleter
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
    
    @column_names.deleter
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
        self.__column_count = value
        log_setter('TreeViewConfiguration', '__column_count', self.__column_count)
        
    @column_count.deleter
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
    PARENTLESS_ROOT_ID:str = 'parentless_root_id'
    PARENTLESS_ROOT_KEY:str = 'Parentless'
    
    def __init__(self, master:tk.Frame, treeview_config:TreeViewConfiguration=None):
        '''
        
        :param tree_config: TreeViewConfiguration
        '''
        log_enter_func('TreeViewControl', '__init__', {'master':master, 'tree_config':treeview_config})
        
        #Contains all TreeViewItems added to the TreeView
        self.__added_treeview_items = []
        #Is the item which is currently about to be added to the tree. 
        self.__current_treeview_item = None
        #Contains the error message if the state is set to ERROR.
        #This is optional! It is not said that there is an message if an error occurs.
        self.__error_message = None
        #State of the TreeViewControl
        self.__treeview_state = TreeViewState.OK
        #Contains all registered observers.
        self.__observers = []
        #This array contains all TreeViewItem for which the parent element was not added
        #at the time as they were added.
        self.__parentless_items = []
        #UI Treeview element.
        self.__treeview = None
        #Contains the mapping of the treeview_id and the corresponding TreeViewItem.
        self.__treeview_id_dict = {}
        #build the treeview
        self.__build_tree(master, treeview_config) 
        
        log_leave_func('TreeViewControl', '__init__')

    ### public methods ###################################################################
    def insert(self, treeview_item:TreeViewItem) -> None:
        '''
        Add the given treeview_item to the TreeViewcontrol.
        If the parent_id of the treeview_item is set, the given treeview_item will inserted
        under TreeViewItem with the corresponding ID.
        If the parent_id of the treeview_item is set, but there is no item with that ID
        in the TreeViewControl, the given treeview_item will be inserted under the "Parentless"
        top level element.
        As soon as the parent is added the parentless TreeViewItem will be moved from the 
        "Parentless" element to its actual parent.
        :param treeview_item:TreeViewItem the item to be added to the TreeViewcontrol
        '''
        log_enter_func('TreeViewControl', 'insert', {'treeview_item':treeview_item})
        
        self.__current_treeview_item = treeview_item
        
        new_treeview_id = self.__create_treeview_id()

        self.__treeview_id_dict[new_treeview_id] = treeview_item
        self.__added_treeview_items.append(treeview_item)
        
        self.__validate_input()
        
        parent_id = '' #This would insert the item as root element
        
        if self.__treeview_state == TreeViewState.OK:
            parent_id = self.__get_treeview_id(treeview_item.parent_id)
        elif self.__treeview_state == TreeViewState.PARENT_NOT_EXISTS:
            #Add current_treeview_item to parentless items
            self.__parentless_items.append(treeview_item)
            parent_id = TreeViewControl.PARENTLESS_ROOT_ID
            
            #Check if parentless node exists
            if not self.__treeview.exists(parent_id):
                #If not add it.
                self.__treeview.insert('', 'end', parent_id, text=TreeViewControl.PARENTLESS_ROOT_KEY)
        
        values = ['']
        
        if not treeview_item.value == None:
            values = [treeview_item.value]
        
        self.__treeview.insert(parent_id, 'end', new_treeview_id, text=treeview_item.key, values=values)
        
        self.__revise_parentlesses()
        
        log_leave_func('TreeViewControl', 'insert')
    
    def remove(self, treeview_item:TreeViewItem=None):
        '''
        Removes the given treeview_item and all its children from the TreeViewControl.
        If treeview_item == None, then the whole TreeViewControl will be cleared.
        :param treeview_item: TreeViewItem to be deleted form tree.
        '''
        log_enter_func('TreeViewControl', 'remove', {'treeview_item':treeview_item})
        
        if treeview_item == None:
            # Clear the whole tree
            self.__treeview.delete(*self.__treeview_id_dict.keys())
            self.__added_treeview_items.clear()
            self.__treeview_id_dict.clear()
            self.__parentless_items.clear()
            
        else:
            #Remove the given item and its children from the tree.
            for child in self.__find_children(treeview_item.parent_id):
                self.remove(child)
                
            treeview_id = self.__get_treeview_id(treeview_item.id)
            
            self.__treeview.delete(treeview_id)
            self.__added_treeview_items.remove(treeview_item)
            del self.__treeview_id_dict[treeview_id]
            self.__parentless_items.remove(treeview_item)
        
        log_leave_func('TreeViewControl', 'remove')
        
    def select(self, treeview_item:TreeViewItem) -> None:
        '''
        Removes the focus and the selection form the currently selected treeview item.
        If treeview_item and the id in the treeview_itme is NOT None
        then the corresponding item in the tree will be selected and focused.
        If treeview_item or its attribute is None, then after removing the focus
        and the selection the method will be left.
        :param treeview_item: The treeview item to be selected.
        '''
        log_enter_func('TreeViewControl', 'select', {'treeview_item':treeview_item})
        
        if len(self.__treeview) > 0:
            self.__treeview.selection_remove(self.__treeview.selection()[0])
        
        self.__treeview.focus('')
        
        if not treeview_item == None and not treeview_item.id == None:
            self.__treeview.focus(treeview_item.id)
            self.__treeview.selection_set(treeview_item.id)
        
        log_leave_func('TreeViewControl', 'select')
        
    
    ### Public Observer methods ##########################################################
    
    def remove_observer(self, observer:TreeViewObserver) -> None:
        '''
        Removes the given TreeViewObserver from the TreeViewControl.
        :param observer: TreeViewObserver to be removed.
        '''
        log_enter_func('TreeViewControl', 'remove_observer', {'observer':observer})
        
        self.__observers.remove(observer)
        
        log_leave_func('TreeViewControl', 'remove_observer')
        
    def clear_observers(self) -> None:
        '''
        Removes all registered observers.
        '''
        log_enter_func('TreeViewControl', 'clear_observers')
        
        self.__observers.clear()
        
        log_leave_func('TreeViewControl', 'clear_observers')
        
    
    def add_observer(self, observer:TreeViewObserver) -> None:
        '''
        Adds the given observer to the TreeViewcontrol.
        :param observer: TreeViewObserver to be added.
        '''
        log_enter_func('TreeViewControl', 'add_observer', {'observer':observer})
        
        self.__observers.append(observer)
        
        log_leave_func('TreeViewControl', 'add_observer')
        
    ######################################################################################
        
    ### private methods ##################################################################
    def __find_children(self, parent_id):
        '''
        Searches the __added_treeview_items array for items with item.parent_id == parent_id
        :param parent_id: Id (not treeview_id) of the parent.
        '''
        log_enter_func('TreeViewControl', '__find_children', {'parent_id':parent_id})
        
        children = []
        
        for treeview_item in self.__added_treeview_items:
            if treeview_item.parent_id == parent_id:
                children.append(treeview_item)
        
        log_leave_func('TreeViewControl', '__find_children', children)
        
    
    def __build_tree(self,master, treeview_config):
        '''
        Build the basic setup of the treeview by considering treeview_config.
        :param treeview_config:
        '''
        log_enter_func('TreeViewControl', '__build_tree', {'master':master, 'tree_config':treeview_config})
        
        self.__treeview = Treeview(master=master, columns=('#%s' %(treeview_config.column_count)))
        self.__treeview.column('#0', stretch=tk.NO)
        
        for idx,col_name in enumerate(treeview_config.column_names):
            self.__treeview.heading('#%s' %(idx),text=col_name,anchor=tk.W)
            
        self.__treeview.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        
        self.__treeview.bind('<<TreeviewSelect>>', self.__notify_on_select)
        self.__treeview.bind('<Double-1>', self.__notify_on_double_click)
        
        log_leave_func('TreeViewControl', '__build_tree')
        
    
    def __create_treeview_id(self):
        '''
        Creates the temporary id and sets it in the current TreeViewItem.
        '''
        log_enter_func('TreeViewControl', '__create_treeview_id')
        
        treeview_id = uuid.uuid1()
        
        log_leave_func('TreeViewControl', '__create_treeview_id', treeview_id)
        
        return str(treeview_id)
    
    
    def __get_treeview_id(self, _id):
        '''
        Searches the __treeview_id_dict mapping for the TreeViewItem (value) for 
        item with TreeViewItem.id == __id, and, if found, returns the key of the
        mapping entry.
        :param _id: The id of the TreeViewItem 
        '''
        log_enter_func('TreeViewControl', '__get_treeview_id', {'_id':_id})
        
        searched_treeview_id = None
        
        for treeview_id, treeview_item in self.__treeview_id_dict.items():
            if treeview_item.id == _id:
                searched_treeview_id = treeview_id
                break
        
        log_leave_func('TreeViewControl', '__get_treeview_id', searched_treeview_id)
        
        return searched_treeview_id
        
    def __notify_on_double_click(self, event):
        '''
        Event handler for the double click event.
        Calls the just the __notify_on_selection_event with is_double_click == True.
        :param event: Double click event, contains the treeview_id of the double clicked TreeViewItem
        '''
        log_enter_func('TreeViewControl', '__notify_on_double_click', {'event':event})
        
        self.__notify_on_selection_event(event, True)
        
        log_leave_func('TreeViewControl', '__notify_on_double_click')
        
    def __notify_on_error(self):
        '''
        Notifies all registered observers that an error has occurred.
        '''
        log_enter_func('TreeViewControl', '__notify_on_error')
        
        for observer in self.__observers:
            observer.on_error(self.__error_message)
        
        log_leave_func('TreeViewControl', '__notify_on_error')
    
    def __notify_on_select(self, event):
        '''
        Event handler for the select event.
        Calls the just the __notify_on_selection_event with is_double_click == False.
        :param event: Select event, contains the treeview_id of the selected TreeViewItem
        '''
        log_enter_func('TreeViewControl', '__notify_on_select', {'event':event})
        
        self.__notify_on_selection_event(event, False)
        
        log_leave_func('TreeViewControl', '__notify_on_select')
        
    def __notify_on_selection_event(self, event, is_double_click):
        '''
        Calls for the given event the corresponding observer method.
        is_double_click == True -> on_double_click
        is_double_click == False -> on_select
        :param event: Select or the double click event
        :param is_double_click: is True if the event was a double click event, otherwise False.
        '''
        log_enter_func('TreeViewControl', '__notify_on_selection_event', {'event':event, 'is_double_click':is_double_click})
        
        selected_treeview_item = self.__treeview_id_dict[event.widget.selection()[0]]
        
        for observer in self.__observers:
            if is_double_click:
                observer.on_double_click(selected_treeview_item)
            else:
                observer.on_select(selected_treeview_item)
        
        log_leave_func('TreeViewControl', '__notify_on_selection_event')
        
    def __revise_parentlesses(self):
        '''
        Checks for each parentless TreeViewItem if now the parent is in the tree.
        If the parentless TreeViewItem will be move under the proper superior element
        it will be removed from __parentless_items array. 
        '''
        log_enter_func('TreeViewControl', '__revise_parentlesses')
        
        for parentless_item in self.__parentless_items:
            self.__current_treeview_item = parentless_item
            self.__validate_input()
            if self.__treeview_state == TreeViewState.OK:
                treeview_id = self.__get_treeview_id(parentless_item.id)
                parent_id = self.__get_treeview_id(parentless_item.parent_id)
                
                self.__properties.move(treeview_id, parent_id, 'end')
                self.__parentless_items.remove(parentless_item)
                
        if len(self.__parentless_items) == 0 and self.__treeview.exists(TreeViewControl.PARENTLESS_ROOT_ID):
            self.__treeview.delete(TreeViewControl.PARENTLESS_ROOT_ID)
        
        log_leave_func('TreeViewControl', '__revise_parentlesses')
        
    def __search_parent(self):
        '''
        Searches in the __added_treeview_items for the parent of the element
        which is currently assigned to the __current_treeview_item. 
        If found it'll return the parent TreeViewItem otherwise None.
        '''
        log_enter_func('TreeViewControl', '__search_parent')
        
        parent = None
        
        for treeview_item in self.__added_treeview_items:
            if treeview_item.id == self.__current_treeview_item.parent_id:
                parent = treeview_item
                break
        
        log_leave_func('TreeViewControl', '__search_parent', parent)
        
        return parent
        
    def __set_error_state(self, error_message):
        '''
        Sets the state and the error message of the TreeViewControl and triggers the error notification of observers.
        :param error_message: The error message
        '''
        log_enter_func('TreeViewControl', '__set_error_state', {'error_message':error_message})
        
        self.__error_message = error_message
        self.__treeview_state = TreeViewState.ERROR
        self.__notify_on_error()
        
        log_leave_func('TreeViewControl', '__set_error_state')
        
    def __validate_input(self):
        '''
        Set the treview_state to TreeViewState.OK.
        Checks if the parent id of the __current_treeview_item is set and if so it searches
        for the parent in the __added_treeview_items array. If it finds the item the treeview_state remains unchanged.
        If the parent couldn't be found the treeview_state will be changed to TreeViewState.PARENT_NOT_EXISTS.
        If the parent id of the __current_treeview_item is not set the __treeview_state is set to TreeViewState.NO_PARENT.
        '''
        log_enter_func('TreeViewControl', '__validate_input')
        
        self.__treeview_state = TreeViewState.OK
        
        if not self.__current_treeview_item.parent_id == None:
            
            parent_item = self.__search_parent()
            
            if parent_item == None:
                self.__treeview_state = TreeViewState.PARENT_NOT_EXISTS
            
        else:
            self.__treeview_state = TreeViewState.NO_PARENT
            
        
        log_set_var('TreeViewControl', '__validate_input', '__treeview_state', self.__treeview_state)
        
        
        log_leave_func('TreeViewControl', '__validate_input')
    
    ######################################################################################
    ######################################################################################
    ######################################################################################        
        
