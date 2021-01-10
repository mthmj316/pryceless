'''
Created on 04.08.2020

@author: mthoma
'''
import json
import os
from pathlib import Path
import time
from typing import List

from dialogs.css_dialogs import CreateCssRuleSet, ABSCreateCssRuleSetObserver
from dialogs.html_dialogs import CreateTagDialog, ABSHTMLDialogObserver
from dialogs.text_dialogs import ABSTextDialogObserver, SelectText
from main_window.abs_main_window import ABSMainWindowMo, \
    ABSMainWindowModelObserver
from overrides.overrides import overrides
import scripts.configuration_loader as conf_loader
from tkinter import messagebox, simpledialog
from tkinter.filedialog import askopenfilename, askdirectory
from utils.logger import log_enter_func, log_leave_func, log_set_var, log_msg,\
    log_getter, log_setter
from controls.treeview_control import TreeViewItem


TEXT = 'text'
INTERNAL_ID = 'internal_id'
INNER_TEXT = 'inner_text'
PAGES = 'pages'

class MainWindowMo(ABSMainWindowMo, ABSHTMLDialogObserver, ABSTextDialogObserver, ABSCreateCssRuleSetObserver):
    '''
    classdocs
    '''
    __NONE_DISPLAY_PROPERTIES = [INTERNAL_ID, 'parent_id', INNER_TEXT, 'is_compound', 
                                 'selector_type', 'selector_element', 'selector_specifier', 
                                 'selector_sep']
        
    __observers: List[ABSMainWindowModelObserver] = []
    
    __last_project_folder: str =  os.path.join(str(Path.home()),'Dokumente','pryceless-workspace')
    
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
        log_enter_func('MainWindowMo', '__init__')
        
        log_leave_func('MainWindowMo', '__init__')
    
    
    @overrides
    def on_text_selected(self, result=None):
        '''
        '''
        log_enter_func('MainWindowMo', 'on_text_selected', {'result':result})
        
        if not result == None:
            
            #contains all defined text collections
            text_collections = self.__loaded_project_dict[TEXT]
            
            #Search for the text collection which has bee 
            #selected to get the internal_id 
            internal_id_text_collection = None
            for txtcol_id,txtcol_content in text_collections.items():
                if txtcol_content['name'] == result[0]:
                    for txt_id, txt_conf in txtcol_content['content'].items():
                        if txt_conf['id'] == result[1]:
                            internal_id_text_collection = '.'.join([TEXT, txtcol_id, 'content', txt_id])
                    break
                         
            log_set_var('MainWindowMo', 'on_text_selected', 'internal_id_text_collection', internal_id_text_collection)

            #the configuration of the selected sub element (__selected_sub)
            sub_conf = self.__conf_of(self.__selected_sub)             
            log_set_var('MainWindowMo', 'on_text_selected', 'sub_conf', sub_conf)
            
            sub_conf[INNER_TEXT] = internal_id_text_collection            
            log_set_var('MainWindowMo', 'on_text_selected', 'sub_conf', sub_conf)
            
            self.__notify_observer(ABSMainWindowModelObserver.CONFIGURATION_CHANGE_TYPE)
        
        log_leave_func('MainWindowMo', 'on_text_selected')   
               
    @overrides
    def set_text(self):
        '''
        '''
        log_enter_func('MainWindowMo', 'set_text')
        text_elements = []

        for text,text_conf in self.__loaded_project_dict[TEXT].items():
            for text_frag_conf in text_conf['content'].values():
                text_elements.append((text, text_frag_conf['id'], 
                                      text_frag_conf[INTERNAL_ID], 
                                      text_frag_conf[TEXT]))
                
                     
        log_set_var('MainWindowMo', 'set_text', 'text_elements', text_elements)
        
        SelectText(text_elements, self)
        
        log_leave_func('MainWindowMo', 'set_text')   
    
    @overrides
    def is_sub_selected(self) -> bool:
        '''
        Returns True if a sub element is selcted. 
        '''
        log_enter_func('MainWindowMo', 'is_sub_selected')
        
        _is = not self.__selected_sub == None
        
        log_leave_func('MainWindowMo', 'is_sub_selected', '_is',_is) 
        
        return _is
        
    @overrides
    def delete_property(self, property_id:str):
        '''
        '''
        log_enter_func('MainWindowMo', 'delete_property', {'property_id':property_id})
        
        log_leave_func('MainWindowMo', 'delete_property')   
        
    @overrides
    def on_create_tag_closed(self, result=None):
        '''
        '''
        log_enter_func('MainWindowMo', 'on_create_tag_closed', {'result':result})
        if not result == None:
            
            split_selected_id = self.__selected_id.split('.')
            log_set_var('MainWindowMo', 'on_create_tag_closed', 'text_elements', split_selected_id)
            
            selected_page_conf = self.__loaded_project_dict[PAGES][split_selected_id[-1]]
            log_set_var('MainWindowMo', 'on_create_tag_closed', 'selected_page_conf', selected_page_conf)

            parent_iid = ''

            if not self.__selected_sub == None:
                parent_iid = self.__selected_sub.split('.')[-1]
            else:
                if 'root' in selected_page_conf['struct']:
                    # Check if root is already set
                    messagebox.showerror('Input Error', 'Root element already exists!')
                    return
            
            log_set_var('MainWindowMo', 'on_create_tag_closed', 'parent_iid', parent_iid)
            
            self.__insert_tag(result, split_selected_id[-1], parent_iid)
            self.__notify_observer(ABSMainWindowModelObserver.CONFIGURATION_CHANGE_TYPE)
         
        log_leave_func('MainWindowMo', 'on_create_tag_closed')             
    
    def __create_internal_id(self):
        
        log_enter_func('MainWindowMo', '__create_internal_id')
        
        internal_id = str(time.time()).replace('.', '_')
        
        log_leave_func('MainWindowMo', '__create_internal_id','internal_id',internal_id)
        
        return internal_id
                    
    def __insert_tag(self, tag_basic_data, page_id, parent_iid):
        
        log_enter_func('MainWindowMo', '__insert_tag', {'tag_basic_data':tag_basic_data,'page_id':page_id,'parent_iid':parent_iid})
        
        internal_id = self.__create_internal_id()
        log_set_var('MainWindowMo', '__insert_tag', 'internal_id', internal_id)
        
        tag = {
            'id': tag_basic_data[0],
            'name': tag_basic_data[1],
            INTERNAL_ID: internal_id,
            'parent_id': parent_iid
        }
        log_set_var('MainWindowMo', '__insert_tag', 'tag', tag)
        
        page = self.__loaded_project_dict[PAGES][page_id]
        log_set_var('MainWindowMo', '__insert_tag', 'page', page)
        
        page['content'][internal_id] = tag
        log_set_var('MainWindowMo', '__insert_tag', 'page', page)
        
        self.__update_page_struct(tag_basic_data[2], internal_id, page['struct'], parent_iid)
        
        log_leave_func('MainWindowMo', '__insert_tag')  
        
    def __update_page_struct(self, position, internal_id, struct, parent_iid):
        # logging next
        
        log_enter_func('MainWindowMo', '__update_page_struct', {'position':position,'internal_id':internal_id,
                                                                'struct':struct, 'parent_iid':parent_iid})
        
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
            
            log_set_var('MainWindowMo', '__update_page_struct', 'children_for_parent_iid', children_for_parent_iid)
                
            # position must be converted to str
            # and decremented by 1
            
            idx = int(position) - 1
            
            children_for_parent_iid.insert(idx, internal_id)
            
            log_set_var('MainWindowMo', '__update_page_struct', 'children_for_parent_iid', children_for_parent_iid)
            
            struct[parent_iid] = ','.join(children_for_parent_iid)
                    
            # add internal_id to to struct with empty child info
            struct[internal_id] = ''
            
        
        log_set_var('MainWindowMo', '__update_page_struct', 'struct', struct)
        
        log_leave_func('MainWindowMo', '__update_page_struct')  
    
    @overrides
    def create_child(self)-> bool:
        '''
        '''
        log_enter_func('MainWindowMo', 'create_child')
        
        if self.__selected_id.startswith(PAGES):
            CreateTagDialog(self)
        elif self.__selected_id.startswith(TEXT):
            self.__create_new_text_element()
        elif self.__selected_id.startswith('css_rules'):
            CreateCssRuleSet(self)
    
        log_leave_func('MainWindowMo', 'create_child', True) 
        
        return True
    
    def __create_new_text_element(self):
        
        log_enter_func('MainWindowMo', '__create_new_text_element')
        
        name = ''
        initial_value = name
        
        while name == '':
        
            name = simpledialog.askstring('New Text ...', 
                                          'Enter the name of the text element:',
                                          initialvalue=initial_value)
            
            log_set_var('MainWindowMo', '__create_new_text_element', 'name', name)
        
            content = self.__current_content()
        
            if self.__exists_name(name, content):
                messagebox.showerror('Name exists',
                                     'Item "%s" already exists.' %(name))
                initial_value = name
                name = ''
                
                log_msg('MainWindowMo', '__create_new_text_element', 'name exists')
                
            elif name == None:
                
                log_msg('MainWindowMo', '__create_new_text_element', 'user cancelled')
                
                return
            else:
                internal_id = self.__create_internal_id()
                
                log_set_var('MainWindowMo', '__create_new_text_element', 'internal_id', internal_id)  
                
                new_text = {
                    'id': name,
                    'name': name,
                    INTERNAL_ID: internal_id,
                    TEXT: ''
                }
                
                log_set_var('MainWindowMo', '__create_new_text_element', 'new_text', new_text)  
                
                content[internal_id] = new_text
                self.__notify_observer(ABSMainWindowModelObserver.CONFIGURATION_CHANGE_TYPE)
        
        log_leave_func('MainWindowMo', '__create_new_text_element', True) 
                
    
    def __exists_name(self, name, content):
        '''
        Returns True if the given name exists
        in the given content, otherwise False.
        '''
        log_enter_func('MainWindowMo', '__exists_name',{'name':name,'content':content})
        
        exists = True if name in self.__names_in_content(content) else False
        
        log_leave_func('MainWindowMo', '__exists_name', exists) 
        
        return exists
        
    def __names_in_content(self, content):
        '''
        Returns all names within the given content,
        or an empty array if none is conatined.
        '''
        log_enter_func('MainWindowMo', '__names_in_content',{'content':content})

        names = []
        
        for value in content.values():
            names.append(value['name'])
        
        log_leave_func('MainWindowMo', '__names_in_content', names) 
        
        return names
        
    def __current_conf(self):
        '''
        Returns the configuration to 
        which the currently selected id (e.g. selected page)
        points
        '''
        log_enter_func('MainWindowMo', '__current_conf')
        
        current_conf = self.__conf_of(self.__selected_id)
        
        log_leave_func('MainWindowMo', '__current_conf', current_conf)
        
        return current_conf
    
    def __conf_of(self, id_path):
        '''
        Returns the configuration to which
        the given id_path points.
        '''
        log_enter_func('MainWindowMo', '__conf_of',{'id_path':id_path})
        
        conf = None
        
        if not id_path == None:
            
            conf = self.__loaded_project_dict
            split = id_path.split('.')
            
            for _id in split:
                if _id in conf:
                    conf = conf[_id]
        
        log_leave_func('MainWindowMo', '__conf_of', conf)
        
        return conf
    
    def __current_content(self):
        '''
        Returns the content of the currently selected page, css rule, ...       
        If nothing is selected None will be returned.
        '''
        log_enter_func('MainWindowMo', '__current_content')
        
        current_content = self.__content_of(self.__selected_id)
        
        log_leave_func('MainWindowMo', '__current_content', current_content)
        
        return current_content

    def __content_of(self, id_path):
        '''
        Returns the content which can be found
        at the given id_path (e.g.: pages.login_page)
        If id_path == None or there is no content element
        None will be returned
        '''
        log_enter_func('MainWindowMo', '__content_of',{'id_path':id_path})
        
        content = self.__conf_of(id_path)
        
        if 'content' in content:
            content = content['content']
        else:
            content = None
        
        log_leave_func('MainWindowMo', '__content_of', content)
            
        return content
    
    @overrides
    def rename(self)->None:
        '''
        '''
        log_enter_func('MainWindowMo', 'rename')
        
        split_selected_id = self.__selected_id.split('.')
        
        log_set_var('MainWindowMo', 'rename', 'split_selected_id', split_selected_id)  
        
        existing_names = self.__names_in_content(self.__loaded_project_dict[split_selected_id[0]])
        
        log_set_var('MainWindowMo', 'rename', 'existing_names', existing_names)  
        
        current_conf = self.__current_conf()
        
        initial_value = current_conf['name']
        
        log_set_var('MainWindowMo', 'rename', 'initial_value', initial_value)  
        
        new_name = ''
        
        while new_name == '':
            
            new_name = simpledialog.askstring('Rename ...', 
                                              'Enter the new name:',
                                              initialvalue=initial_value)
            
            log_set_var('MainWindowMo', 'rename', 'new_name', new_name) 
            
            if new_name in existing_names:
                messagebox.showerror('Name exists',
                                     'Item "%s" already exists.' %(new_name))
                initial_value = new_name
                new_name = ''
                
                log_msg('MainWindowMo', 'rename', 'name exists') 
        
        if not new_name == None:
            
            current_conf['name'] = new_name
            
            log_set_var('MainWindowMo', 'rename', 'current_conf', current_conf) 
            
            self.__notify_observer(ABSMainWindowModelObserver.OVERVIEW_CHANGE_TYPE)
        
        log_leave_func('MainWindowMo', 'rename')
        
        
    @overrides
    def is_selected(self)->bool:
        '''
        '''
        log_enter_func('MainWindowMo', 'is_selected')
        
        is_selected = (not self.__selected_id == None)
        
        log_leave_func('MainWindowMo', 'is_selected', is_selected)
        
        return is_selected
        
    @overrides
    def create_variable(self) -> None:
        '''
        '''
        log_enter_func('MainWindowMo', 'create_variable')
        
        variable_name = ''
        
        existing_variables = self.__loaded_project_dict['variables'].keys()
        
        log_set_var('MainWindowMo', 'create_variable', 'existing_variables', existing_variables)
        
        while variable_name == '':
            
            variable_name = simpledialog.askstring("Create Variable", 
                                                  'Enter the name of the variable:')
            
            log_set_var('MainWindowMo', 'create_variable', 'variable_name', variable_name)
            
            if variable_name in existing_variables:
                msg = 'Variable "%s" already exists.' %(variable_name)
                
                messagebox.showerror('Variable exists',msg)
                
                log_msg('MainWindowMo', 'create_variable', msg) 
                
                variable_name = ''
                
                log_set_var('MainWindowMo', 'create_variable', 'variable_name', variable_name)
            
        if not variable_name == None:
            
            new_variable = {
                'content': {},
                'name': variable_name
            }
            
            log_set_var('MainWindowMo', 'create_variable', 'new_variable', new_variable)
            
            self.__loaded_project_dict['variables'][variable_name] = new_variable
            self.save()
        
        log_leave_func('MainWindowMo', 'create_variable')
            
    @overrides
    def create_text(self) -> None:
        '''
        '''
        log_enter_func('MainWindowMo', 'create_text')
        text_name = ''
        
        existing_texts = self.__loaded_project_dict[TEXT].keys()
        
        log_set_var('MainWindowMo', 'create_text', 'existing_texts', existing_texts)
        
        while text_name == '':
            
            text_name = simpledialog.askstring("Create Text", 
                                                  'Enter the name of the Text')
            
            log_set_var('MainWindowMo', 'create_text', 'text_name', text_name)
            
            if text_name in existing_texts:
                msg = 'Text "%s" already exists.' %(text_name)
                
                messagebox.showerror('Text exists',msg)
                
                log_msg('MainWindowMo', 'create_text', msg) 
                
                text_name = ''
                
                log_set_var('MainWindowMo', 'create_text', 'text_name', text_name)
            
        if not text_name == None:
            
            new_text = {
                'content': {},
                'name': text_name
            }
            
            log_set_var('MainWindowMo', 'create_text', 'new_text', new_text)
            
            self.__loaded_project_dict[TEXT][text_name] = new_text
            self.save()
        
        
        log_leave_func('MainWindowMo', 'create_text')
   
    @overrides
    def create_javascript(self) -> None:
        '''
        '''
        log_enter_func('MainWindowMo', 'create_javascript')
        
        script_name = ''
        
        existing_scripts = self.__loaded_project_dict['javascripts'].keys()
        
        log_set_var('MainWindowMo', 'create_javascript', 'existing_scripts', existing_scripts)
        
        while script_name == '':
            
            script_name = simpledialog.askstring("Create JavaScript", 
                                                  'Enter the name of the JS')
            
            log_set_var('MainWindowMo', 'create_javascript', 'script_name', script_name)
        
            if script_name in existing_scripts:
                
                msg = 'JavaScript "%s" already exists.' %(script_name)
                
                messagebox.showerror('JavaScript exists', msg)

                log_msg('MainWindowMo', 'create_javascript', msg) 
                
                script_name = ''
                
                log_set_var('MainWindowMo', 'create_javascript', 'script_name', script_name)
                
            
        if not script_name == None:
            
            new_script = {
                'content': {},
                'name': script_name
            }
            
            log_set_var('MainWindowMo', 'create_javascript', 'new_script', new_script)
            
            self.__loaded_project_dict['javascripts'][script_name] = new_script
            self.save()
        
        
        log_leave_func('MainWindowMo', 'create_javascript') 
    
    @overrides
    def create_css_rule(self) -> None:
        '''
        '''
        log_enter_func('MainWindowMo', 'create_css_rule')
        
        new_css_rule = ''
        
        existing_rules = self.__loaded_project_dict['css_rules'].keys()
        
        log_set_var('MainWindowMo', 'create_css_rule', 'existing_rules', existing_rules)
        
        while new_css_rule == '':
            
            new_css_rule = simpledialog.askstring("Create CSS Rule", 
                                                  'Enter the name of the rule')
            
            log_set_var('MainWindowMo', 'create_css_rule', 'new_css_rule', existing_rules)
            
            if new_css_rule in existing_rules:
                msg = 'CSS Rule "%s" already exists.' %(new_css_rule)
                
                messagebox.showerror('CSS Rule exists',msg)
                
                log_msg('MainWindowMo', 'create_css_rule', msg) 
                
                new_css_rule = ''
                log_set_var('MainWindowMo', 'create_css_rule', 'new_css_rule', existing_rules)
            
        if not new_css_rule == None:
            
            new_rule = {
                'content': {},
                'name': new_css_rule
            }
            
            log_set_var('MainWindowMo', 'create_css_rule', 'new_rule', new_rule)
            
            self.__loaded_project_dict['css_rules'][new_css_rule] = new_rule
            self.save()
        
        log_leave_func('MainWindowMo', 'create_css_rule') 
            
    @overrides
    def set_property(self, property_id:str) -> None:
        '''
        
        :param property_id:
        '''
        log_enter_func('MainWindowMo', 'set_property', {'property_id':property_id})
        
        split_property_id = property_id.split('.')
        
        log_set_var('MainWindowMo', 'set_property', 'split_property_id', split_property_id)
        
        answer = simpledialog.askstring("Input", ''.join(['Set: ', split_property_id[-1]]),
                                        initialvalue=self.get_property_value(property_id))
        
        log_set_var('MainWindowMo', 'set_property', 'answer', answer)
            
        if answer == None:
            return
            
        #At the end this variable contains 
        #the reference to configuration item for which
        # the proerty must be set. 
        conf = self.__loaded_project_dict
        log_set_var('MainWindowMo', 'set_property', 'conf', conf)
        
        #The index when the loop has to be left
        #The loop must be left after the second to last item
        break_idx = len(split_property_id) - 1
        log_set_var('MainWindowMo', 'set_property', 'break_idx', break_idx)
        
        current_idx = 0
        
        while current_idx < break_idx:
            conf = conf[split_property_id[current_idx]]            
            current_idx += 1
        
        log_set_var('MainWindowMo', 'set_property', 'conf', conf)
        
        conf[split_property_id[-1]] = answer
        
        log_set_var('MainWindowMo', 'set_property', 'conf', conf)
        
        self.__notify_observer(ABSMainWindowModelObserver.PROPERTY_CHANGE_TYPE)
    
        log_leave_func('MainWindowMo', 'set_property') 
            
        
    @overrides
    def get_property_value(self, property_id:str) -> str:
        '''
        '''
        log_enter_func('MainWindowMo', 'get_property_value', {'property_id':property_id})
        
        split_property_id = property_id.split('.')
        log_set_var('MainWindowMo', 'get_property_value', 'split_property_id', split_property_id)
        
        value = self.__loaded_project_dict
        log_set_var('MainWindowMo', 'get_property_value', 'value', value)
        
        for _id in split_property_id:
            if _id in value:
                value = value[_id]
            else:
                value = ''
                break
            
        
        log_leave_func('MainWindowMo', 'get_property_value', value) 
            
        return value
            
        
    @overrides
    def get_sub_data(self) -> [TreeViewItem]:
        '''
        '''
        log_enter_func('MainWindowMo', 'get_sub_data')
        
        split_sub_id = self.__selected_sub.split('.')
        
        log_set_var('MainWindowMo', 'get_sub_data','split_sub_id', split_sub_id)
        
        sub_data = self.__loaded_project_dict
        
        for _id in split_sub_id:
            sub_data = sub_data[_id]
            
        log_set_var('MainWindowMo', 'get_sub_data','sub_data', sub_data)
        
        properties = []
        
        defined_property = []
        
        '''
        treeview_item = TreeViewItem()
            treeview_item.id = _property[0]
            treeview_item.key =  _property[1]
            treeview_item.value =  _property[2]
            treeview_item.parent_id =  _property[3]
            treev
        '''
        
        for key,value in sub_data.items():
            if key in self.__NONE_DISPLAY_PROPERTIES:
                continue
            
            treeview_item = TreeViewItem()
            treeview_item.id = '.'.join([self.__selected_sub, key])
            treeview_item.key =  key
            treeview_item.value = value
            
            properties.append(treeview_item)
            # properties.append(('.'.join([self.__selected_sub, key]),key,value,None))
            defined_property.append(key)
            
        #Add other possible attributes/properties for which no value is defined.
        if split_sub_id[0] == PAGES:
            
            properties += self.__prepare_html_attr_sub_data(defined_property, sub_data['name'])
        
        elif split_sub_id[0] == 'css_rules':
            
            properties += self.__prepare_css_sub_data(defined_property)
            
        log_leave_func('MainWindowMo', 'get_sub_data', properties)
                      
        return properties
    
    def __prepare_html_attr_sub_data(self, defined_properties, tag_name):
        '''
        Prepares the html attributes for which no value is defined
        :param defined_properties: the names of the attributes for which a value is defined
        :param tag_name: name of the html tag for the attributes shall be prepared.
        '''
        log_enter_func('MainWindowMo', '__prepare_html_attr_sub_data', 
                       {'defined_properties':defined_properties, 'tag_name':tag_name})
        
        properties = []
        
        treeview_item = TreeViewItem()
        treeview_item.id = 'Attributes'
        treeview_item.key =  'Attributes'
        treeview_item.value = None
        treeview_item.is_double_clickable = False
        treeview_item.is_selectable = False
            
        properties.append(treeview_item)
        
        #properties.append(('Attributes','Attributes',None,None))
        
        treeview_item = TreeViewItem()
        treeview_item.id = 'Events'
        treeview_item.key =  'Events'
        treeview_item.value = None
        treeview_item.is_double_clickable = False
        treeview_item.is_selectable = False
            
        properties.append(treeview_item)
        #properties.append(('Events','Events',None,None))
        
        html_tag_data = conf_loader.load_html_tag(tag_name)
        for attribute in html_tag_data['attributes']:
                
            if attribute in defined_properties:
                continue
            treeview_item = TreeViewItem()
            treeview_item.id = '.'.join([self.__selected_sub, attribute])
            treeview_item.key =  attribute
            treeview_item.value = None
            treeview_item.parent_id = 'Attributes'
            
            properties.append(treeview_item)
                              
            #properties.append(('.'.join([self.__selected_sub, attribute]),attribute,'','Attributes'))
                  
        for event in html_tag_data['events']:
                
            if event in defined_properties:
                continue
            treeview_item = TreeViewItem()
            treeview_item.id = '.'.join([self.__selected_sub, event])
            treeview_item.key =  event
            treeview_item.value = None
            treeview_item.parent_id = 'Events'
            
            properties.append(treeview_item)                   
            #properties.append(('.'.join([self.__selected_sub, event]),event,'','Events'))
            
        log_leave_func('MainWindowMo', '__prepare_html_attr_sub_data', properties)
        
        return properties
    
    def __prepare_css_sub_data(self, defined_properties):
        '''
        Returns all css properties for which is not a value defined.
        :param defined_properties: Contains the names of these properties for which a value is defined.
        '''
       
        log_enter_func('MainWindowMo', '__prepare_html_attr_sub_data', 
                       {'defined_properties':defined_properties}) 
        
        properties = []
        
        treeview_item = TreeViewItem()
        treeview_item.id = 'Properties'
        treeview_item.key =  'Properties'
        treeview_item.value = None
        treeview_item.is_double_clickable = False
        treeview_item.is_selectable = False
            
        properties.append(treeview_item)
        
        #properties.append(('Properties','Properties','Properties',None))
        
        for css_property in conf_loader.get_css_properties():
            if css_property in defined_properties:
                    continue
                
            shorthand = conf_loader.get_css_shorthand(css_property)
            
            log_set_var('MainWindowMo', '__prepare_css_sub_data', 'shorthand', shorthand)
            
            treeview_item = TreeViewItem()
            treeview_item.id = '.'.join([self.__selected_sub, css_property])
            treeview_item.key =  css_property
            treeview_item.value = None
            treeview_item.parent_id = 'Properties' if shorthand == '' else '.'.join([self.__selected_sub, shorthand])
            
            properties.append(treeview_item)
                
            #properties.append(('.'.join([self.__selected_sub, css_property]), css_property, '', 'Properties' if shorthand == '' else '.'.join([self.__selected_sub, shorthand])))
        
        log_leave_func('MainWindowMo', '__prepare_css_sub_data', properties)
        
        return properties
    
    @overrides
    def selected_sub(self) -> str:
        '''
        '''
        log_getter('MainWindowMo', '__selected_sub', self.__selected_sub)
        return self.__selected_sub
    
    @overrides
    def select_sub(self, sub_id:str) -> None:
        '''
        Sets the selected configuration item in the model.
        '''
        self.__selected_sub = sub_id

        log_setter('MainWindowMo', '__selected_sub', self.__selected_sub)
    
    @overrides
    def __iter__(self):
        
        log_enter_func('MainWindowMo', '__iter__') 
        
        if not self.is_project_open():
            raise ValueError('No Project opened!')
        elif self.__selected_id == None:
            raise ValueError('No page selected!')
        
        self.__iteration_current = 0
        
        selected_split = self.__selected_id.split(sep='.')
        log_set_var('MainWindowMo', '__iter__', 'selected_split', selected_split)
        
        content = self.__current_content()
        log_set_var('MainWindowMo', '__iter__', 'content', content)
        
        #Check if the dict to be iterated has a sub-dict: struct
        if 'struct' in self.__loaded_project_dict[selected_split[0]][selected_split[1]]:
            #Sub-struct -> the structure must be built before iteration can be start.
            for _id in self.__build_struct(selected_split):
                self.__iterate_this[_id] = content[_id]
                log_set_var('MainWindowMo', '__iter__', 'self.__iterate_this', self.__iterate_this)
        else:
            #No sub-dict -> there is no structure to be built up
            self.__iterate_this = content
            log_set_var('MainWindowMo', '__iter__', 'self.__iterate_this', self.__iterate_this)
        
        
        log_leave_func('MainWindowMo', '__iter__', self)
        
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
        
        print('MainWindowMo.__next__')
        
        if self.__iteration_current < len(self.__iterate_this):
            
            print('MainWindowMo.__next__    __iteration_current=' + str(self.__iteration_current))
            
            _data = list(self.__iterate_this.values())[self.__iteration_current]
            
            print('MainWindowMo.__next__    _data=' + str(_data))
            
            self.__iteration_current += 1
            
            #ret_val = (id, parent_id, display_name)
            # parent_id is the id of the element within the conf
            # not within the json file -> eg. css_rule has no parent_id
            
            internal_id =  '.'.join([self.__selected_id, 'content', _data[INTERNAL_ID]])
            parent_id = None
            
            if 'parent_id' in _data and not _data['parent_id'] == '':
                parent_id = '.'.join([self.__selected_id, 'content', _data['parent_id']])
                
            appendix = ''
            
            if self.__selected_id.startswith(TEXT):
                appendix = _data[TEXT]
            else:
                appendix = _data['id']
            
            display_name = display_name = ''.join([_data['name'],' (', appendix ,')'])
            
            if INNER_TEXT in _data:
                print('MainWindowMo.__next__    has inner_text')
                display_name = ''.join([display_name, ' [', 
                                        self.__conf_of(_data[INNER_TEXT])[TEXT], ']'])
            
            print('MainWindowMo.__next__    internal_id=' + str(internal_id) 
                  + ' parent_id=' + str(parent_id) + ' display_name=' + display_name)
            
            return (internal_id, parent_id, display_name)
        
        self.__iterate_this = {}
        
        print('MainWindowMo.__next__    stop iteration')
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
            overview_data.update(self.__get_for_overview(PAGES))
            overview_data.update(self.__get_for_overview('css_rules'))
            overview_data.update(self.__get_for_overview('javascripts'))
            overview_data.update(self.__get_for_overview(TEXT))
            overview_data.update(self.__get_for_overview('variables'))
            
            '''
            items = self.__loaded_project_dict[PAGES]
            for page_id in items.keys():
                overview_data['.'.join([PAGES, page_id])] = page_id
            '''
            
        return overview_data
        
    def __get_for_overview(self, base):
        
        print('MainWindowMo.__get_for_overview    base=' + str(base))
        
        _data = {}
        
        if base in self.__loaded_project_dict:
            
            items = self.__loaded_project_dict[base]
        
            for _id in items.keys():
                _data['.'.join([base, _id])] = items[_id]['name']
         
        print('MainWindowMo.__get_for_overview    _data=' + str(_data))   
        return _data
                
    @overrides
    def create_page(self) -> None:
        '''
        Creates a new HTML page within the selected project.
        Duplicated pages are prevented.
        '''
        page_name = self.__name_page('New Page', 'Please enter page name.')
        
        if not page_name == None:
            
            internal_id = self.__create_internal_id()
            
            self.__loaded_project_dict[PAGES][internal_id] = {
                'name': page_name,
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
                
                pages = self.__loaded_project_dict[PAGES]
                
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
        print('MainWindowMo.create_new_project')
        
        selected_dir = askdirectory(initialdir = self.__last_project_folder,
                                    title = 'Select Project Folder')
        
        print('MainWindowMo.create_new_project    selected_dir=' + str(selected_dir))
        
        if len(selected_dir) > 0:
            self.__last_project_folder = selected_dir
            
            project_names  = self.__name_project('Project Name', 
                                                'Please enter an unique name for the new project.')
            
            print('MainWindowMo.create_new_project    project_names=' + str(project_names))
            
            if not project_names == None:
                
                self.__full_project_path = project_names[1]
                print('MainWindowMo.create_new_project    __full_project_path=' + str(self.__full_project_path))
                
                
                self.__loaded_project_dict = {
                    'project_name': project_names[0],
                    PAGES: {},
                    'css_rules': {},
                    'javascripts': {},
                    TEXT: {},
                    'variables': {}                         
                    }
                
                print('MainWindowMo.create_new_project    __loaded_project_dict=' + str(self.__loaded_project_dict))
                        
                self.save()
                
                self.__selected_id = None
                self.__has_changes = False
                
                self.__notify_observer(ABSMainWindowModelObserver.PROJECT_CREATED)
                
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
        return not self.__loaded_project_dict == None
    
    @overrides
    def open_project(self) -> bool:
        '''
        Opens askopenfilename dialog.
        The root of the dialog is the last used directory.
        If for the first time the is opened the user home
        directory will be the root. 
        '''
        print('MainWindowMo.open_project')
        # Open file selection dialog
        file_name = askopenfilename(initialdir = self.__last_project_folder,
                                    title = 'Select Project',
                                    filetypes =(('json files','*.json'),))
        
        print('MainWindowMo.open_project    file_name=' + str(file_name))
        
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
            
            print('MainWindowMo.open_project    True')
            
            return True
        
        print('MainWindowMo.open_project    False')
        
        return False
    
    def __load_project(self, file_name):
        '''
        '''
        print('MainWindowMo.__load_project    file_name=' + str(file_name))
        with open(file_name, 'r') as file:
            self.__loaded_project_dict = json.load(file)
        print('MainWindowMo.__load_project    __loaded_project=' + str(self.__loaded_project_dict))
            
    def __notify_observer(self,change_typ):
        '''
        '''
        print('MainWindowMo.__notify_observer    change_type=' + str(change_typ))

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
        
    @overrides
    def on_create_css_rule_set_closed(self, result=None):
        
        print('MainWindowMo.on_create_css_rule_set_closed    result=' + str(result))
        
        if not result == None:
            
            internal_id = self.__create_internal_id()
            print('MainWindowMo.on_create_css_rule_set_closed    internal_id=' + str(internal_id))
            
            name = ''.join([result[1],result[4],result[2]])
            print('MainWindowMo.on_create_css_rule_set_closed    name=' + str(name))
            
            new_css_rule_set = {
                INTERNAL_ID: internal_id,
                'is_compound': result[3],
                'selector_type': result[0],
                'selector_element': result[1],
                'selector_specifier': result[2],
                'selector_sep': result[4],
                'name': name,
                'id': name
                }
            print('MainWindowMo.on_create_css_rule_set_closed    new_css_rule_set=' + str(new_css_rule_set))
            
            css_file_content = self.__current_content()
            css_file_content[internal_id] = new_css_rule_set
            
            print('MainWindowMo.on_create_css_rule_set_closed    css rule set added')
            
            self.__notify_observer(ABSMainWindowModelObserver.CONFIGURATION_CHANGE_TYPE)
            
        else:
            print('MainWindowMo.on_create_css_rule_set_closed    result is None, process is cancelled')
        
        
        print('MainWindowMo.on_create_css_rule_set_closed    leave')
        
###################################################################
###################################################################
###################################################################
        
        
        
        
        
        
        