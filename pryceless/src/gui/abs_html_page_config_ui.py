'''
Created on 04.08.2020

@author: mthoma
'''
import abc as abc
from scripts.html_element import HTMLElement
from utils.observable import Observable

class ABSHTMLPageConfigUI(abc.ABC, Observable):
    '''
    Interface for HTML
    '''
        
    @abc.abstractmethod
    def insert(self, tag: HTMLElement) -> None:
        '''
        '''
        
    @abc.abstractmethod
    def remove(self, tag: HTMLElement) -> None:
        '''
        '''
    
    @abc.abstractmethod
    def update(self, tag: HTMLElement) -> None:
        '''
        '''
        
    @abc.abstractmethod
    def clear(self) -> None:
        '''
        '''
        
    @abc.abstractmethod
    def move(self, tag: HTMLElement) -> None:
        '''
        '''

    @abc.abstractmethod
    def get_selected(self) -> str:
        '''
        Returns the id of the selected html tag
        ''' 