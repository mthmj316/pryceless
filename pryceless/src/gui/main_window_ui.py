'''
Created on 13.07.2020

@author: mthoma
'''
import tkinter as tk
from gui.abs_main_window_ui import ABSMainWindowUI
from overrides import overrides

'''
_____________________________________________________
|          |                              |         |
|          |                              |  Attr.  |
|   HTML   |                              |         |
|   Tag    |                              |         |
| Overview |     Page Config              |         |
|          |                              |---------|
|          |                              |         |
|          |                              |   CSS   |
|          |                              |         |
|----------|---------------|--------------|---------|
|          |               |              |         |
|          |               |              |         |
|    Text  |      Events   |    JS        |  Var    |
|          |               |              |         |
|__________|_______________|______________|_________|


--> 3 rows and 4 columns

'''
class MainWindowUI(tk.Frame, ABSMainWindowUI):
    
    __html_tag_frame: tk.Frame = None
    
    __page_config_frame: tk.Frame = None
    
    __attributes_frame: tk.Frame = None
    
    __css_frame: tk.Frame = None
    
    __text_frame: tk.Frame = None
    
    __events_frame: tk.Frame = None
    
    __java_scripts_frame: tk.Frame = None
    
    __variables_frame: tk.Frame = None
    
    '''
    classdoc
    '''
    def __init__(self, master):
        '''
        '''
        tk.Frame.__init__(self, master)
        
        self.__create_html_tag_frame()
        self.__create_page_config_frame()
        self.__create_attributes_fram()
        self.__create_css_frame()
        self.__create_text_frame()
        self.__create_events_frame()
        self.__create_java_scripts_frame()
        self.__create_variables_frame()

    @overrides
    def get_html_tag_frame(self) -> tk.Frame:
        '''
        '''
        return self.__html_tag_frame
        
    @overrides
    def get_page_config_frame(self) -> tk.Frame:
        '''
        '''
        return self.__page_config_frame

    @overrides
    def get_attributes_frame(self) -> tk.Frame:
        '''
        '''
        return self.__attributes_frame       

    @overrides
    def get_text_frame(self) -> tk.Frame:
        '''
        '''
        return self.__text_frame
        
    @overrides
    def get_css_frame(self) -> tk.Frame:
        '''
        '''
        return self.__css_frame

    @overrides
    def get_events_frame(self) -> tk.Frame:
        '''
        '''
        return self.__events_frame
        
    @overrides
    def get_java_script_frame(self) -> tk.Frame:
        '''
        '''
        return self.__java_scripts_frame

    @overrides
    def get_variable_frame(self) -> tk.Frame:
        '''
        '''
        return self.__variables_frame
      
    def __create_html_tag_frame(self):
        '''
        '''
        self.__html_tag_frame = tk.Frame(self, background='#111111')
        self.__html_tag_frame.grid(row=0, column=0, rowspan=2)
    
    def __create_page_config_frame(self):
        '''
        '''
        self.__page_config_frame = tk.Frame(self, background='#222222')
        self.__page_config_frame.grid(row=0, column=1, rowspan=2, columnspan=2)
    
    def __create_attributes_fram(self):
        '''
        '''
        
    def __create_css_frame(self):
        '''
        '''
        
    def __create_text_frame(self):
        '''
        '''
        
    def __create_events_frame(self):
        '''
        '''
    
    def __create_java_scripts_frame(self):
        '''
        '''
        
    def __create_variables_frame(self):
        '''
        '''