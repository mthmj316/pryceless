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
    __last_project_folder: str =  '/home/mthoma/Dokumente/prycless-workspace'  #os.getenv('HOME')
    
    __loaded_project_dict: dict = None

    __has_changes: bool = False
    
    __full_project_path: str = None
    
    __selected_id: str = None
    
    __selected_sub: str = None
    
    __iterate_this: dict = None
    
    __iteration_current: int = 0

    def __init__(self):
        '''
        Constructor
        ''' 
    
    @overrides
    def get_sub_data(self) -> dict:
        '''
        '''
    
    @overrides
    def select_sub(self, sub_id:str) -> None:
        '''
        Sets the selected configuration item in the model.
        '''
        self.__selected_sub = sub_id
        print(self.__selected_sub)
    
    @overrides
    def __iter__(self):
        
        if not self.is_project_open():
            raise ValueError('No Project opened!')
        elif self.__selected_id == None:
            raise ValueError('No page selected!')
        
        self.__iteration_current = 0
        
        selected_split = self.__selected_id.split(sep='.')
        self.__iterate_this = self.__loaded_project_dict[selected_split[0]][selected_split[1]]['content']
        
        return self
    
    @overrides
    def __next__(self):
        
        print(len(self.__iterate_this))
        
        if self.__iteration_current < len(self.__iterate_this):
            
            _data = list(self.__iterate_this.values())[self.__iteration_current]
            self.__iteration_current += 1
            
            #ret_val = (id, parent_id, display_name)
            # parent_id is the id of the element within the conf
            # not within the json file -> eg. css_rule has no parent_id
            
            _id =  '.'.join([self.__selected_id, 'content', _data['id']])
            parent_id = None
            
            if 'parent_id' in _data and not _data['parent_id'] == '':
                parent_id = '.'.join([self.__selected_id, 'content', _data['parent_id']])
            
            display_name = ''
                
            if 'name' in _data:
                display_name = ''.join([_data['name'],' (', _data['id'] ,')'])
            elif 'type' in _data:
                display_name = ''.join([_data['id'],' (', _data['type'] ,')'])
            else:
                display_name = _data['id']        
            
            return (_id, parent_id, display_name)
        
        raise StopIteration
    
    @overrides
    def selected(self) -> str:
        '''
        Returns the id of the selected configuration item.
        If none is selected None will be returned.
        '''
        return self.__selected_id
           
    @overrides
    def select(self, conf_id:str) -> None:
        '''
        Sets the selected configuration item in the model.
        '''
        self.__selected_id = conf_id
        
    @overrides
    def get_overview_data(self) -> dict:
        '''
        Returns a dictionary containing:
        key -> id of the page
        value -> name of the page
        '''
        overview_data = {}
        

        if self.is_project_open():
            overview_data.update(self.__get_for_overview('pages'))
            overview_data.update(self.__get_for_overview('css_rules'))
            overview_data.update(self.__get_for_overview('javascript'))
            overview_data.update(self.__get_for_overview('text'))
            overview_data.update(self.__get_for_overview('variables'))
            
            '''
            items = self.__loaded_project_dict['pages']
            for page_id in items.keys():
                overview_data['.'.join(['pages', page_id])] = page_id
            '''
            
        return overview_data
        
    def __get_for_overview(self, base):
        
        _data = {}
        
        if base in self.__loaded_project_dict:
            items = self.__loaded_project_dict[base]
        
            for _id in items.keys():
                _data['.'.join([base, _id])] = _id
            
        return _data
                
    @overrides
    def create_page(self) -> None:
        '''
        Creates a new HTML page within the selected project.
        Duplicated pages are prevented.
        '''
        page_name = self.__name_page('New Page', 'Please enter page name.')
        
        if not page_name == None:
            
            self.__loaded_project_dict['pages'][page_name] = {
                'page_name': page_name,
                'content': {}
                } 
            
            self.save()
            
            self.select(page_name)
    
    def __name_page(self, title, msg) -> str:
        
        page_name = ''
            
        while page_name == '':
            # while loop is as long continued as
            # page_name is ''
            page_name = simpledialog.askstring(title, msg)
        
            if not page_name == None:
                # Check if the name already exists
                
                pages = self.__loaded_project_dict['pages']
                
                if not page_name in pages:
                    
                    return page_name
                    
                else:
                    messagebox.showerror('Page exists', 
                                         'Page name "%s" is already used.' %(page_name))
                    page_name = ''
        
        return None
    
    @overrides
    def rename_project(self) -> None:
        '''
        Renames the currently loaded project
        '''
        new_project = self.__name_project('Rename Project', 
                                               'Please enter the new project name.')
        
        if not new_project == None:
            
            old_fully_qualified_path = self.__full_project_path
            self.__full_project_path = new_project[1]
            
            self.__loaded_project_dict['project_name'] = new_project[0]
            
            self.save()
            
            os.unlink(old_fully_qualified_path)
    
        
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
            
            project_names = self.__name_project('Project Name', 
                                                'Please enter an unique name for the new project.')
            
            if not project_names == None:
                
                self.__full_project_path = project_names[1]
                self.__loaded_project_dict = {
                    'project_name': project_names[0],
                    'pages': {},
                    'css_rules': {},
                    'javascript': {},
                    'text': {},
                    'variables': {}                         
                    }
                        
                self.save()
                
                self.__selected_id = None
                self.__has_changes = False
                
                return
        
        messagebox.showinfo('Project Creation', 'Project creation has been cancelled.')
    
    def __name_project(self, title, msg):
        
        project_name = ''
            
        while project_name == '':
            # while loop is as long continued as
            # project_name is ''
            project_name = simpledialog.askstring(title, msg)
        
            if not project_name == None:
                
                new_full_project_path = self.__create_full_project_path(project_name)
                
                if not self.__exists_project(new_full_project_path):
                    
                    return (project_name, new_full_project_path)

                else:
                    messagebox.showerror('Project exists', 
                                         'Project name "%s" is already used.' %(project_name))
                    project_name = ''
        
        return None
    
    def __create_full_project_path(self, project_name) -> str:
        '''
        Creates the full path for the given project_name
        '''
        full_path = '/'.join([self.__last_project_folder,
                              project_name])
        
        return '.'.join([full_path, 'json'])
    
    def __exists_project(self, full_project_path):
        '''
        Check if full_project_path already exists.
        Return True if so otheriwse False
        '''
        return os.path.isfile(full_project_path)
        
    @overrides
    def get_project_name(self)->str:
        '''
        Returns the name of the currently loaded project
        '''
        
        if self.is_project_open():
            return self.__loaded_project_dict['project_name']
        else:
            return ''
    
    @overrides
    def save(self)->None:
        '''
        '''
        with open(self.__full_project_path, 'w') as file:
            json.dump(self.__loaded_project_dict, file, indent=4, sort_keys=True)
                
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
            
            self.__selected_id = None
            self.__has_changes = None
            
            return True
        
        return False