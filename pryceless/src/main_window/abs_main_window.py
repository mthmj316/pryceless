'''
Created on 04.08.2020

@author: mthoma
'''
import abc as abc
import tkinter as tk

class ABSMainWindowUI(abc.ABC):
    '''
    classdocs
    '''    
    @abc.abstractmethod
    def get_html_tag_frame(self) -> tk.Frame:
        '''
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
        
    @abc.abstractmethod
    def get_java_script_frame(self) -> tk.Frame:
        '''
        '''

    @abc.abstractmethod
    def get_variable_frame(self) -> tk.Frame:
        '''
        '''