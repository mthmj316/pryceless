'''
Created on 18.08.2020

@author: mthoma
'''
from abc import ABC, abstractmethod
from typing import List
        
class ABSMemento(ABC):
    '''
    Empty interface
    '''

class ABSMementoOrigin(ABC):
    
    @abstractmethod
    def restore(self, memento:ABSMemento):
        '''
        '''

class Memento(ABSMemento):
    '''
    classdocs
    '''
    MODIFY_CHANGE_TYPE = 'modify'
    
    ADD_CHANGE_TYPE = 'add'
    
    DELETE_CHANGE_TYPE = 'delete'
    
    #Model to which this memento belongs
    __memento_origin: ABSMementoOrigin = None
    
    #possible values: add, delete and modify
    __change_type: str = None
    
    #Contains the changed date.
    #How the data is prepared depends on the originator
    __change: dict = {}
    
    def __init__(self, change_type:str = MODIFY_CHANGE_TYPE,
                 origin:ABSMementoOrigin):
        '''
        Constructor
        '''
        self.__change_type = change_type
        self.__memento_origin = origin

    @property
    def change(self):
        '''
            change getter
        '''
        return self.__change
    
    @change.setter
    def change(self, value:dict):
        '''
            change setter
        '''
        self.__change = value
    
    @change.deleter
    def change(self):
        '''
            change deleter
        '''
        del self.__change

    @property
    def change_type(self):
        '''
            change_type getter
        '''
        return self.__change_type
    
    @change_type.setter
    def change_type(self, value:str):
        '''
            change_type setter
        '''
        self.__change_type = value
    
    @change_type.deleter
    def change_type(self):
        '''
            change_type deleter
        '''
        del self.__change_type
        
    @property
    def memento_origin(self):
        '''
            memento_origin getter
        '''
        return self.__memento_origin
    
    @memento_origin.setter
    def memento_origin(self, value:ABSMementoOrigin):
        '''
            memento_origin setter
        '''
        self.__memento_origin = value
    
    @memento_origin.deleter
    def memento_origin(self):
        '''
            memento_origin deleter
        '''
        del self.__memento_origin


class ChangeStack(object):
    
    __stack_size = 0
    
    __stack: List[ABSMemento] = []
    
    __stack_size_exceeded = False
    
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
        self.__stack.insert(0, memento)
        
        while len(self.__stack) > self.__stack_size:
            #should be actually just one loop 
            self.__stack.pop()
            self.__stack_size_exceeded = True
            
        return self.__stack_size_exceeded
        
    def pop(self) -> ABSMemento:
        '''
        Returns and removes the memento which is
        at the top of the stack.
        '''
        return self.__stack.pop(0)
    
    @property
    def stack_size_exceeded(self):
        '''
        getter stack_size_exceeded
        '''
        return self.__stack_size_exceeded