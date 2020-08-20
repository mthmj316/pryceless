'''
Created on 18.08.2020

@author: mthoma
'''
from abc import ABC, abstractmethod
from typing import List


class ABSMementoOrigin(ABC):
    
    @abstractmethod
    def restore(self, memento:ABSMemento):
        '''
        '''
        
class ABSMemento(ABC):
    '''
    
    '''
    @abstractmethod
    def push(self, change:dict) -> None:
        '''
        Put the given change at the top of the change stack.
        If by adding this change the max. stack size is
        exceeded, the the change which is at the bottom of
        the stack will be removed.
        '''
    
    @abstractmethod
    def pull(self) -> dict:
        '''
        Returns the change which is at the top of the change stack.
        The returned change will be removed from the stack.
        '''

class Memento(ABSMemento):
    '''
    classdocs
    '''
    #Model to which this memento belongs
    __memento_origin: ABSMementoOrigin = None
    
    #possible values: add, delete and modify
    __change_type: str = None
    
    def __init__(self):
        '''
        Constructor
        ''' 

class ChangeStack(object):
    
    __stack_size = 0
    
    __undo_stack: List[ABSMemento] = []
    
    __redo_stack: List[ABSMemento] = []
    
    def __init__(self, stack_size=50):
        '''
        '''
        self.__stack_size = stack_size
        
    def push(self, memento:ABSMemento) -> bool:
        '''
        Put the given memento at the top of the change stack.
        If by adding this memento the max. stack size is
        exceeded, the the memento which is at the bottom of
        the stack will be removed.
        Returns True after the max stack size has been exceeded once.
        '''
        
    def undo(self) -> ABSMemento:
        '''
        '''
    
    def redo(self) -> ABSMemento:
        '''
        '''   