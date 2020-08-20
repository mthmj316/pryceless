'''
Created on 04.08.2020

@author: mthoma
'''
import abc as abc
import tkinter as tk
from abc import abstractmethod
from utils.utils import Event


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
    def on_select_page(self, event:Event) -> None:
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
    def notify_select_page(self) -> None:
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
    @abc.abstractmethod
    def get_page_config_frame(self) -> tk.Frame:
        '''
        '''

    @abc.abstractmethod
    def get_attributes_frame(self) -> tk.Frame:
        '''
        '''        

    @abc.abstractmethod
    def get_text_frame(self) -> tk.Frame:
        '''
        '''
        
    @abc.abstractmethod
    def get_css_frame(self) -> tk.Frame:
        '''
        '''
        
    @abc.abstractmethod
    def get_events_frame(self) -> tk.Frame:
        '''
        '''

class ABSMainWindowMo(abc.ABC):
    '''
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

    KEY_RENAME_PAGE = 'Rename Page'

    KEY_RENAME_PROJECT = 'Rename Project'

    KEY_SAVE = 'Save'

    KEY_SAVE_AS = 'Save as ...'

    KEY_SELECT_PAGE = 'Select Page'

    KEY_SELENIUM_TEST_CASES = 'Selenium Test Cases'

    KEY_TEXT = 'Text'

    KEY_UNDO = 'Undo'

    KEY_VARIABLE = 'Variable'