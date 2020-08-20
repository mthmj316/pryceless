'''
Created on 04.08.2020

@author: mthoma
'''
from overrides.overrides import overrides
from main_window.abs_main_window import ABSMainWindowMo
import os
from tkinter.filedialog import askopenfilename
import json

class MainWindowMo(ABSMainWindowMo):
    '''
    classdocs
    '''
    __last_project_folder: str = os.getenv('HOME')
    
    __loaded_project_dict: dict = None

    def __init__(self):
        '''
        Constructor
        '''
    
    @overrides
    def is_project_open(self) -> bool:
        '''
        Returns True if a project is open,
        otherwise False
        '''
        return self.__loaded_project_dict != None
    
    @overrides
    def open_project(self) -> bool:
        '''
        Opens askopenfilename dialog.
        The root of the dialog is the last used directory.
        If for the first time the is opened the user home
        directory will be the root. 
        '''
        # Open file selection dialog
        file_name = askopenfilename(initialdir = self.__last_project_folder,
                                    title = 'Select Project',
                                    filetypes =(('json files','*.json'),))
        
        # check if file has been select or the process cancelled
        if file_name:
            # file_name is set:
            # set new working dir
            self.__last_project_folder = os.path.dirname(file_name)
            # write the file content to the __loaded_project_json attribute
            with open(file_name, 'r') as file:
                self.__loaded_project_dict = json.load(file)
                
            return True
        
        return False