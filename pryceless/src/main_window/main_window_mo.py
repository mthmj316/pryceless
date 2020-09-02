'''
Created on 04.08.2020

@author: mthoma
'''
from overrides.overrides import overrides
from main_window.abs_main_window import ABSMainWindowMo,\
    ABSMainWindowModelObserver
import os
from tkinter.filedialog import askopenfilename, askdirectory
import json
from tkinter import messagebox, simpledialog
from dialogs.html_dialogs import CreateTagDialog, ABSHTMLDialogObserver
import time
from typing import List
from scripts.configuration_loader import load_html_tag

class MainWindowMo(ABSMainWindowMo, ABSHTMLDialogObserver):
    '''
    classdocs
    '''
    __NONE_DISPLAY_PROPERTIES = ['internal_id', 'parent_id']
    
    __observers: List[ABSMainWindowModelObserver] = []
    
    __last_project_folder: str =  '/'.join([os.getenv('HOME'), '/Dokumente/prycless-workspace'])
    
    __loaded_project_dict: dict = None

    __has_changes: bool = False
    
    __full_project_path: str = None
    
    __selected_id: str = None
    
    __selected_sub: str = None
    
    __iterate_this: dict = {}
    
    __iteration_current: int = 0

    def __init__(self):
        '''
        Constructor
        ''' 
    @overrides
    def is_sub_selected(self) -> bool:
        '''
        Returns True if a sub element is selcted. 
        '''
        return not self.__selected_sub == None
        
    @overrides
    def delete_property(self, property_id:str):
        '''
        '''
        print(property_id)
        
    @overrides
    def on_create_tag_closed(self, result=None):
        '''
        '''
        if not result == None:
            
            split_selected_id = self.__selected_id.split('.')
            selected_page_conf = self.__loaded_project_dict['pages'][split_selected_id[-1]]

            parent_iid = ''

            if not self.__selected_sub == None:
                parent_iid = self.__selected_sub.split('.')[-1]
            else:
                if 'root' in selected_page_conf['struct']:
                    # Check if root is already set
                    messagebox.showerror('Input Error', 'Root element already exists!')
                    return
                
            self.__insert_tag(result, split_selected_id[-1], parent_iid)
            self.__notify_observer(ABSMainWindowModelObserver.CONFIGURATION_CHANGE_TYPE)
                    
                    
    def __insert_tag(self, tag_basic_data, page_id, parent_iid):
        
        internal_id = str(time.time()).replace('.', '_')
        
        tag = {
            'id': tag_basic_data[0],
            'name': tag_basic_data[1],
            'internal_id': internal_id,
            'parent_id': parent_iid
        }
        
        page = self.__loaded_project_dict['pages'][page_id]
        
        page['content'][internal_id] = tag
        
        self.__update_page_struct(tag_basic_data[2], internal_id, page['struct'], parent_iid)
    
    def __update_page_struct(self, position, internal_id, struct, parent_iid):
        
        if self.__selected_sub == None:
            #New tag must be root
            struct['root'] = internal_id
            struct[internal_id] = ''
        else:
            
            # internal_id to the parent at the given position
            if not struct[parent_iid] == '':
                children_for_parent_iid = struct[parent_iid].split(',')
            else :
                children_for_parent_iid = []
                
            # position must be converted to str
            # and decremented by 1
            
            idx = int(position) - 1
            
            children_for_parent_iid.insert(idx, internal_id)
            struct[parent_iid] = ','.join(children_for_parent_iid)
                    
            # add internal_id to to struct with empty child info
            struct[internal_id] = ''    
    
    @overrides
    def create_tag(self)-> bool:
        '''
        '''
        CreateTagDialog(self)
    
    @overrides
    def rename(self)->None:
        '''
        '''
        
        split_selected_id = self.__selected_id.split('.')
        existing_names = self.__loaded_project_dict[split_selected_id[0]].keys()
        
        initial_value = split_selected_id[1]
        
        new_name = ''
        while new_name == '':
            
            new_name = simpledialog.askstring('Rename ...', 
                                              'Enter the new name:',
                                              initialvalue=initial_value)
            
            if new_name in existing_names:
                messagebox.showerror('Name exists',
                                     'Item "%s" already exists.' %(new_name))
                initial_value = new_name
                new_name = ''
        
        if not new_name == None:
            
            conf = self.__loaded_project_dict[split_selected_id[0]][split_selected_id[1]]
            conf['name'] = new_name
        
            del self.__loaded_project_dict[split_selected_id[0]][split_selected_id[1]]
            
            self.__loaded_project_dict[split_selected_id[0]][new_name] = conf
            
            self.save()
            
            self.__load_project(self.__full_project_path)
            
            self.__selected_id = '.'.join([split_selected_id[0], new_name])
        
    @overrides
    def is_selected(self)->bool:
        '''
        '''
        return (not self.__selected_id == None)
        
    @overrides
    def create_variable(self) -> None:
        '''
        '''
        variable_name = ''
        
        existing_variables = self.__loaded_project_dict['variables'].keys()
        while variable_name == '':
            
            variable_name = simpledialog.askstring("Create Variable", 
                                                  'Enter the name of the variable:')
            
            if variable_name in existing_variables:
                messagebox.showerror('Variable exists',
                                     'Variable "%s" already exists.' %(variable_name))
                
                variable_name = ''
            
        if not variable_name == None:
            
            new_variable = {
                'content': {},
                'name': variable_name
            }
            
            self.__loaded_project_dict['variables'][variable_name] = new_variable
            self.save()
            
    @overrides
    def create_text(self) -> None:
        '''
        '''
        text_name = ''
        
        existing_texts = self.__loaded_project_dict['text'].keys()
        while text_name == '':
            
            text_name = simpledialog.askstring("Create Text", 
                                                  'Enter the name of the Text')
            
            if text_name in existing_texts:
                messagebox.showerror('Text exists',
                                     'Text "%s" already exists.' %(text_name))
                
                text_name = ''
            
        if not text_name == None:
            
            new_text = {
                'content': {},
                'name': text_name
            }
            
            self.__loaded_project_dict['text'][text_name] = new_text
            self.save()
   
    @overrides
    def create_javascript(self) -> None:
        '''
        '''
        script_name = ''
        
        existing_scripts = self.__loaded_project_dict['javascripts'].keys()
        while script_name == '':
            
            script_name = simpledialog.askstring("Create JavaScript", 
                                                  'Enter the name of the JS')
            
            if script_name in existing_scripts:
                messagebox.showerror('JavaScript exists',
                                     'JavaScript "%s" already exists.' %(script_name))
                
                script_name = ''
            
        if not script_name == None:
            
            new_script = {
                'content': {},
                'name': script_name
            }
            
            self.__loaded_project_dict['javascripts'][script_name] = new_script
            self.save()   
    
    @overrides
    def create_css_rule(self) -> None:
        '''
        '''
        new_css_rule = ''
        
        existing_rules = self.__loaded_project_dict['css_rules'].keys()
        while new_css_rule == '':
            
            new_css_rule = simpledialog.askstring("Create CSS Rule", 
                                                  'Enter the name of the rule')
            
            if new_css_rule in existing_rules:
                messagebox.showerror('CSS Rule exists',
                                     'CSS Rule "%s" already exists.' %(new_css_rule))
                
                new_css_rule = ''
            
        if not new_css_rule == None:
            
            new_rule = {
                'content': {},
                'name': new_css_rule
            }
            
            self.__loaded_project_dict['css_rules'][new_css_rule] = new_rule
            self.save()    
            
    @overrides
    def set_property(self, property_id:str) -> None:
        '''
        '''
        split_property_id = property_id.split('.')
        answer = simpledialog.askstring("Input", ''.join(['Set: ', split_property_id[-1]]),
                                        initialvalue=self.get_property_value(property_id))
            
        if answer == None:
            return
        
        print(answer)
            
        #At the end this variable contains 
        #the reference to configuration item for which
        # the proerty must be set. 
        conf = self.__loaded_project_dict
        
        #The index when the loop has to be left
        #The loop must be left after the second to last item
        break_idx = len(split_property_id) - 1
        current_idx = 0
        
        while current_idx < break_idx:
            conf = conf[split_property_id[current_idx]]
            
            current_idx += 1
            
        conf[split_property_id[-1]] = answer
        
        self.__notify_observer(ABSMainWindowModelObserver.PROPERTY_CHANGE_TYPE)
            
        
    @overrides
    def get_property_value(self, property_id:str) -> str:
        '''
        '''
        split_property_id = property_id.split('.')
        
        value = self.__loaded_project_dict
        
        for _id in split_property_id:
            if _id in value:
                value = value[_id]
            else:
                value = ''
                break
            
        return value
            
        
    @overrides
    def get_sub_data(self) -> dict:
        '''
        '''
        split_sub_id = self.__selected_sub.split('.')
        
        sub_data = self.__loaded_project_dict
        
        for _id in split_sub_id:
            sub_data = sub_data[_id]
        
        properties = []
        
        defined_property = []
        
        for key,value in sub_data.items():
            if key in self.__NONE_DISPLAY_PROPERTIES:
                continue
            properties.append(('.'.join([self.__selected_sub, key]),key,value,None))
            defined_property.append(key)
            
        #Add other possible attributes
        
        
        if split_sub_id[0] == 'pages':
            html_tag_data = load_html_tag(sub_data['name'])
            for attribute in html_tag_data['attributes']:
                
                if attribute in defined_property:
                    continue
                                
                properties.append(('.'.join([self.__selected_sub, attribute]),attribute,'','Attributes'))
                  
            for event in html_tag_data['events']:
                
                if event in defined_property:
                    continue
                                
                properties.append(('.'.join([self.__selected_sub, event]),event,'','Events'))
                      
        return properties
    
    @overrides
    def selected_sub(self) -> str:
        '''
        '''
        return self.__selected_sub
    
    @overrides
    def select_sub(self, sub_id:str) -> None:
        '''
        Sets the selected configuration item in the model.
        '''
        self.__selected_sub = sub_id
    
    @overrides
    def __iter__(self):
        
        if not self.is_project_open():
            raise ValueError('No Project opened!')
        elif self.__selected_id == None:
            raise ValueError('No page selected!')
        
        self.__iteration_current = 0
        
        selected_split = self.__selected_id.split(sep='.')
        content = self.__loaded_project_dict[selected_split[0]][selected_split[1]]['content']
        
        #Check if the dict to be iterated has a sub-dict: struct
        if 'struct' in self.__loaded_project_dict[selected_split[0]][selected_split[1]]:
            #Sub-struct -> the structure must be built before iteration can be start.
            for _id in self.__build_struct(selected_split):
                self.__iterate_this[_id] = content[_id]
        else:
            #No sub-dict -> there is no structure to be built up
            self.__iterate_this = content
        
        return self
    
    def __build_struct(self, selected_split):
        '''
        Builds the structure for the iterator
        '''
        struct_info = self.__loaded_project_dict[selected_split[0]][selected_split[1]]['struct']
        
        if not 'root' in struct_info:
            return []
        
        root_id = struct_info['root']
        
        root_children = struct_info[root_id]
        
        if root_children == '':
            return [root_id]
        
        children = root_children.split(',')
        
        struct = [root_id]
        
        struct += children
        
        while len(children) > 0:
            
            tmp = []
            
            for child in children:
                for s in struct_info[child].split(','):
                    if not s == '':
                        
                        struct.append(s)
                        tmp.append(s)
                        
            children = tmp
            tmp = []
            
        return struct
    
    @overrides
    def __next__(self):
        
        if self.__iteration_current < len(self.__iterate_this):
            
            _data = list(self.__iterate_this.values())[self.__iteration_current]
            self.__iteration_current += 1
            
            #ret_val = (id, parent_id, display_name)
            # parent_id is the id of the element within the conf
            # not within the json file -> eg. css_rule has no parent_id
            
            internal_id =  '.'.join([self.__selected_id, 'content', _data['internal_id']])
            parent_id = None
            
            if 'parent_id' in _data and not _data['parent_id'] == '':
                parent_id = '.'.join([self.__selected_id, 'content', _data['parent_id']])
            
            display_name = ''
                
            if 'tag' in _data:
                display_name = ''.join([_data['tag'],' (', _data['id'] ,')'])
            elif 'type' in _data:
                display_name = ''.join([_data['id'],' (', _data['type'] ,')'])
            else:
                display_name = _data['id']        
            
            return (internal_id, parent_id, display_name)
        
        self.__iterate_this = {}
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
        self.__selected_sub = None
        
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
            overview_data.update(self.__get_for_overview('javascripts'))
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
                'content': {},
                'struct': {}
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
                    'javascripts': {},
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
            self.__load_project(file_name)
            
            #and save the file name
            self.__full_project_path = file_name
            
            self.__selected_id = None
            self.__has_changes = None
            
            return True
        
        return False
    
    def __load_project(self, file_name):
        '''
        '''
        with open(file_name, 'r') as file:
            self.__loaded_project_dict = json.load(file)
            
    def __notify_observer(self,change_typ):
        '''
        '''
        for observer in self.__observers:
            observer.on_model_changed(change_typ)
    
    @overrides
    def add_observer(self, observer:ABSMainWindowModelObserver) -> None:
        '''
        '''
        self.__observers.append(observer)
    
    @overrides
    def remove_observer(self, observer:ABSMainWindowModelObserver) -> None:
        '''
        '''
        self.__observers.remove(observer)
        
    @overrides
    def clear_observer(self) -> None:
        '''
        '''
        self.__observers.clear()