'''
Created on 04.08.2020

@author: mthoma
'''
from overrides.overrides import overrides
from main_window.abs_main_window import ABSMainWindowMo
import os
from tkinter.filedialog import askopenfilename, askdirectory
import json
from tkinter import messagebox, simpledialog

class MainWindowMo(ABSMainWindowMo):
    '''
    classdocs
    '''
    __last_project_folder: str = os.getenv('HOME')
    
    __loaded_project_dict: dict = None

    __has_changes: bool = False
    
    __full_project_path: str = None

    def __init__(self):
        '''
        Constructor
        '''
    
    @overrides
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
        selected_dir = askdirectory(initialdir = self.__last_project_folder,
                                    title = 'Select Project Folder')
        
        if len(selected_dir) > 0:
            self.__last_project_folder = selected_dir
            
            project_name = ''
            
            while project_name == '':
                # while loop is as long continued as
                # project_name is ''
                project_name = simpledialog.askstring('Project Name',
                                                      'Please enter an unique name for the new project.')
            
                if not project_name == None:
                    
                    new_
                    
                    if not self.__exists_project(project_name):
                        
                        self.__full_project_path = self.__create_full_project_path(project_name)
                        
                        print(self.__full_project_path)
                        
                        return
                    else:
                        messagebox.showerror('Project exsits', 
                                             'Project name "%s" is already used.' %(project_name))
                        project_name = ''
        
        messagebox.showinfo('Project Creation', 'Project creation has been cancelled.')
    
    def __create_full_project_path(self, project_name) -> str:
        '''
        Creates the full path for the given project_name
        '''
        full_path = '/'.join([self.__last_project_folder,
                              project_name])
        
        return '.'.join([full_path, 'json'])
    
    def __exists_project(self, project_name):
        '''
        Check if in the currently selected project folder
        a project exists with the given project name.
        If so True otherwise False is returned.
        '''
        return False
        
    @overrides
    def get_project_name(self)->str:
        '''
        Returns the name of the currently loaded project
        '''
        return self.__loaded_project_dict['project_name']
    
    @overrides
    def save(self)->None:
        '''
        '''
        with open(self.__full_project_path, 'w') as file:
            json.dump(self.__loaded_project_dict, file)
                
        self.__has_changes = False
    
    @overrides
    def has_changes(self)-> bool:
        '''
        '''
        return self.__has_changes
    
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
            
            #and save the file name
            self.__full_project_path = file_name
            
            return True
        
        return False