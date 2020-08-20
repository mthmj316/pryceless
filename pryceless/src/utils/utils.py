'''
Created on 11.08.2020

@author: mthoma
'''

class Event(object):
    '''
    classdocs
    '''
    
    __event_source: str = None

    def __init__(self):
        '''
        Constructor
        '''   

    @property
    def event_source(self):
        '''
            event_source getter
        '''
        return self.__event_source

    @event_source.setter
    def event_source(self, value):
        '''
            event_source setter
        '''
        self.__event_source = value

    @event_source.deleter
    def event_source(self):
        '''
            event_source deleter
        '''
        del self.__event_source