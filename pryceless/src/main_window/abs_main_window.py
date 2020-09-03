'''
Created on 04.08.2020

@author: mthoma
'''
import abc as abc
import tkinter as tk
from abc import abstractmethod
from utils.utils import Event


class ABSMainWindowModelObserver(abc.ABC):
    '''
    '''
    
    PROPERTY_CHANGE_TYPE = 0
    
    CONFIGURATION_CHANGE_TYPE = 1
    
    @abstractmethod
    def on_model_changed(self, change_typ:int) -> None:
        '''
        '''

class ABSMainWindowObserver(abc.ABC):
    '''
    '''
    @abstractmethod
    def on_save_as(self, event:Event) -> None:
        '''
        '''
        
    @abstractmethod
    def on_save(self, event:Event) -> None:
        '''
        '''
        
    @abstractmethod
    def on_open(self, event:Event) -> None:
        '''
        '''
        
    @abstractmethod
    def on_new(self, event:Event) -> None:
        '''
        '''
        
    @abstractmethod
    def on_exit(self, event:Event) -> None:
        '''
        '''
        
    @abstractmethod
    def on_undo(self, event:Event) -> None:
        '''
        '''
    
    @abstractmethod
    def on_rename(self, event:Event) -> None:
        '''
        '''
        
    @abstractmethod
    def on_edit(self, event:Event) -> None:
        '''
        '''
    
    @abstractmethod
    def on_add(self, event:Event) -> None:
        '''
        '''
        
    @abstractmethod
    def on_delete(self, event:Event) -> None:
        '''
        '''
        
    @abstractmethod
    def on_generate(self, event:Event) -> None:
        '''
        '''
        
    @abstractmethod
    def on_move(self, event:Event) -> None:
        '''
        '''
        
class ABSMainwindowObservable(abc.ABC):
    '''
    '''
    @abstractmethod
    def register_observer(self, observer:ABSMainWindowObserver) -> None:
        '''
        '''
        
    @abstractmethod
    def unregister_observer(self, observer:ABSMainWindowObserver) -> None:
        '''
        '''
        
    @abstractmethod
    def notify_save_as(self) -> None:
        '''
        '''
        
    @abstractmethod
    def notify_save(self) -> None:
        '''
        '''
        
    @abstractmethod
    def notify_open(self) -> None:
        '''
        '''
        
    @abstractmethod
    def notify_new(self) -> None:
        '''
        '''
        
    @abstractmethod
    def notify_exit(self) -> None:
        '''
        '''
        
    @abstractmethod
    def notify_undo(self) -> None:
        '''
        '''
    
    @abstractmethod
    def notify_rename(self) -> None:
        '''
        '''
        
    @abstractmethod
    def notify_edit(self) -> None:
        '''
        '''
    @abstractmethod
    def notify_add(self) -> None:
        '''
        '''
        
    @abstractmethod
    def notify_delete(self) -> None:
        '''
        '''
        
    @abstractmethod
    def notify_generate(self) -> None:
        '''
        '''
        
    @abstractmethod
    def notify_move(self) -> None:
        '''
        '''
          
class ABSMainWindowUI(ABSMainwindowObservable):
    '''
    classdocs
    '''
    @abstractmethod
    def enable_menu_conf_depending(self, enable:bool) -> None:
        '''
        Enables/disables al menu items which depend on
        that a config item is selected:
            HTML-Page/Add Attribute
        '''
        
    @abstractmethod
    def enable_menu_overview_depending(self, enable:bool) -> None:
        '''
        Enables/disables all menu items which depend on that a
        overview item is selected:
            Rename Page
        '''
    
    @abstractmethod
    def enable_menu_project_depending(self, enable:bool) -> None:
        '''
        Enables/disbales all menu items which only depend on
        that a project is opened:
            HTML Page, 
            CSS Rule, 
            JavaScript, 
            Text, 
            Variable, 
            Rename Project 
            and Generate
        '''
        
    @abc.abstractmethod
    def get_page_config_frame(self) -> tk.Frame:
        '''
        '''

    @abc.abstractmethod
    def get_attributes_frame(self) -> tk.Frame:
        '''
        '''        
        
    @abc.abstractmethod
    def get_page_overview_frame(self) -> tk.Frame:
        '''
        '''
        
class ABSMainWindowMo(abc.ABC):
    '''
    
    '''
    @abstractmethod
    def set_text(self):
        '''
        '''
        
    @abstractmethod
    def set_property(self, property_id:str):
        '''
        '''
        
    @abstractmethod
    def is_sub_selected(self) -> bool:
        '''
        Returns True if a sub element is selcted. 
        '''
    
    @abstractmethod
    def delete_property(self, property_id:str):
        '''
        '''
        
    @abstractmethod
    def create_child(self) -> bool:
        '''
        '''
    
    @abstractmethod
    def rename(self) -> None:
        '''
        '''
        
    @abstractmethod
    def is_selected(self) -> bool:
        '''
        '''
    
    @abstractmethod
    def create_variable(self) -> None:
        '''
        '''
        
    @abstractmethod
    def create_text(self) -> None:
        '''
        '''
    
    @abstractmethod
    def create_javascript(self) -> None:
        '''
        '''
        
    @abstractmethod
    def create_css_rule(self) -> None:
        '''
        '''
        
    @abstractmethod
    def get_property_value(self, property_id:str) -> str:
        '''
        '''
    
    @abstractmethod
    def __iter__(self):
        '''
        '''
    
    @abstractmethod
    def __next__(self):
        '''
        '''
    @abstractmethod
    def get_sub_data(self) -> dict:
        '''
        '''
    
    @abstractmethod
    def selected_sub(self) -> str:
        '''
        '''
      
    @abstractmethod
    def selected(self) -> str:
        '''
        Returns the id of the selected configuration item.
        If none is selected None will be returned.
        '''
    
    @abstractmethod
    def select_sub(self, sub_id:str) -> None:
        '''
        Sets the selected configuration item in the model.
        '''
       
    @abstractmethod
    def select(self, conf_id:str) -> None:
        '''
        Sets the selected configuration item in the model.
        '''
    
    @abstractmethod
    def get_overview_data(self) -> dict:
        '''
        Returns a dictionary containing:
        key -> id of the page
        value -> name of the page
        '''
        
    @abstractmethod
    def create_page(self) -> None:
        '''
        Creates a new HTML page within the selected project.
        Duplicated pages are prevented.
        '''
    
    @abstractmethod
    def rename_project(self) -> None:
        '''
        Renames the currently loaded project
        '''
    @abstractmethod
    def create_new_project(self) -> None:
        '''
        Creates a new project.
        Firstly the user must select the directory where the
        project shall be created.
        After that the user is ask to define a project name.
        If the user input is cancelled or the input is empty
        the project won't be created.
        If the name has been entered it is check if there is already 
        a project in the selected directory with the same name.
        If so the user is asked to change the name.
        After that the project file is created.
        '''
    
    @abstractmethod
    def get_project_name(self) -> str:
        '''
        Returns the name of the currently loaded project
        '''
    
    @abstractmethod
    def is_project_open(self) -> bool:
        '''
        Returns True if a project is open,
        otherwise False
        '''
        
    @abstractmethod
    def open_project(self) -> bool:
        '''
        Opens askopenfilename dialog.
        The root of the dialog is the last used directory.
        If for the first time the is opened the user home
        directory will be the root. 
        If a project has been actually open
        True will be returned, otherwise False.
        '''
    
    @abstractmethod
    def has_changes(self) -> bool:
        '''
        Returns True if there are unsaved changes,
        Otherwise False.
        '''
    
    @abstractmethod
    def save(self) -> None:
        '''
        Save the current project setup to the file system.
        '''
    
    @abstractmethod
    def add_observer(self, observer:ABSMainWindowModelObserver) -> None:
        '''
        '''
    
    @abstractmethod
    def remove_observer(self, observer:ABSMainWindowModelObserver) -> None:
        '''
        '''
        
    @abstractmethod
    def clear_observer(self) -> None:
        '''
        '''
           

class MainWindowMenuKeys(object):
    '''
    '''
    KEY_ADD_ATTRIBUTE = 'Add Attribute'

    KEY_ADD_CHILD = 'Add Child'

    KEY_ADD_EVENT = 'Add Event'

    KEY_ADD_TEXT = 'Add Text'

    KEY_ALL = 'All'

    KEY_CHANGE_PARENT = 'Change Parent'

    KEY_CSS = 'CSS'

    KEY_CSS_RULE = 'CSS Rule'

    KEY_DELETE_ATTRIBUTE = 'Delete Attribute'

    KEY_DELETE_EVENT = 'Delete Event'

    KEY_DELETE_TAG = 'Delete Tag'

    KEY_DELETE_TEXT = 'Deletet Text'

    KEY_EDIT = 'Edit'

    KEY_EXIT = 'Exit'

    KEY_FILE = 'File'

    KEY_GENERATE = 'Generate'

    KEY_HTML_HYPHEN_PAGE = 'HTML-Page'

    KEY_HTML_PAGE = 'HTML Page'

    KEY_JAVASCRIPT = 'JavaScript'

    KEY_MOVE_DOWN = 'Move Down'

    KEY_MOVE_UP = 'Move Up'

    KEY_NEW = 'New'

    KEY_OPEN = 'Open ...'

    KEY_PROJECT = 'Project'

    KEY_REDO = 'Redo'

    KEY_RENAME = 'Rename ...'

    KEY_RENAME_PROJECT = 'Rename Project'

    KEY_SAVE = 'Save'

    KEY_SAVE_AS = 'Save as ...'

    KEY_SELENIUM_TEST_CASES = 'Selenium Test Cases'

    KEY_TEXT = 'Text'

    KEY_UNDO = 'Undo'

    KEY_VARIABLE = 'Variable'