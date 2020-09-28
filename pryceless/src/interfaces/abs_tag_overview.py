'''
Created on 10.08.2020

@author: mthoma
'''
from abc import ABC, abstractmethod

from utils.utils import Event


class TagOverviewObserver(ABC):
    '''
    '''
    @abstractmethod
    def on_click(self, event:Event):
        '''
        '''
    
    @abstractmethod
    def on_double_click(self, event:Event):
        '''
        '''

class TagOverviewObservable(ABC):
    
    '''
    classdocs
    '''
    @abstractmethod
    def notify_double_click(self) -> None:
        '''
        Notifies all registered observers that a double click event
        has happened.
        '''
        
    @abstractmethod
    def register_double_click(self, observer: TagOverviewObserver) -> None:
        """
        Attach an observer to the double click event.
        """

    @abstractmethod
    def unregister_double_click(self, observer: TagOverviewObserver) -> None:
        """
        Detach an observer form the double click event.
        """
    
    @abstractmethod
    def notify_click(self) -> None:
        '''
        Notifies all registered observers that a click event
        has happened.
        '''
        
    @abstractmethod
    def register_click(self, observer: TagOverviewObserver) -> None:
        """
        Attach an observer to the click event.
        """

    @abstractmethod
    def unregister_click(self, observer: TagOverviewObserver) -> None:
        """
        Detach an observer form the click event.
        """

class ABSTagOverviewUI(ABC):
    
    @abstractmethod
    def add_list_item(self, item:str) -> None:
        '''
        Adds the given string at the end of the list
        '''
    
    @abstractmethod
    def set_description(self, description:str) -> None:
        '''
        Set the content of the text widget which beneath the list.
        '''
        
    @abstractmethod
    def enable(self, enable) -> None:
        '''
        '''