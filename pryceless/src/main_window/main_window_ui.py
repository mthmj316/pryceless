'''
Created on 13.07.2020

@author: mthoma
'''
'''


'''

from typing import List

from main_window.abs_main_window import ABSMainWindowUI, \
    ABSMainWindowObserver
from main_window.abs_main_window import MainWindowMenuKeys as mKey
from overrides import overrides
import tkinter as tk
from tkinter.ttk import Frame
from utils.utils import Event


class MainWindowUI(tk.Frame, ABSMainWindowUI):
    
    __page_config_frame: tk.Frame = None
    
    __attributes_frame: tk.Frame = None
    
    __page_overview_frame: tk.Frame = None
    
    #__cell_width: float = 0
    
    #__cell_height: float = 0
    
    __menubar: tk.Menu = None
    
    __file_menu: tk.Menu = None
    
    __new_menu: tk.Menu = None

    __edit_menu: tk.Menu = None
    
    __html_page_menu: tk.Menu = None
    
    __last_event: Event = Event()
    
    __observers: List[ABSMainWindowObserver] = []
    
    __right_side: Frame = None
    '''
    classdoc
    '''
    
    def __init__(self, master):
        '''
        '''
        tk.Frame.__init__(self, master)
        
        self.__menubar = tk.Menu(self.master)
        self.master.config(menu=self.__menubar)
        
        self.__create_file_menu()
        self.__create_edit_menu()
        self.__create_html_page_menu()
        
        self.__right_side = tk.Frame(self, background='#000000', 
                                            #width=self.__cell_width*2, height=self.__cell_height*3
                                            )
        self.__right_side.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        
        self.__create_attributes_fram()
        self.__create_page_config_frame()
        self.__create_page_overview_frame()
    
    @overrides
    def enable_menu_conf_depending(self, enable:bool) -> None:
        '''
        Enables/disables al menu items which depend on
        that a config item is selected:
            HTML-Page/Add Attribute
        '''
        new_state = tk.NORMAL if enable else tk.DISABLED
        self.__html_page_menu.entryconfig(mKey.KEY_ADD_TEXT, state=new_state)
        
    
    @overrides
    def enable_menu_overview_depending(self, enable:bool) -> None:
        new_state = tk.NORMAL if enable else tk.DISABLED
        
        self.__edit_menu.entryconfigure(mKey.KEY_RENAME, state=new_state)
        self.__html_page_menu.entryconfig(mKey.KEY_ADD_CHILD, state=new_state)
        
    @overrides
    def enable_menu_project_depending(self, enable:bool) -> None:
        '''
        Enables/disbales all menu items which only depend on
        that a project is opened:
            HTML Page, 
            CSS Rule, 
            JavaScript, 
            Text, 
            Variable, 
            Rename Project 
            and Generate
        '''
        new_state = tk.NORMAL if enable else tk.DISABLED
        
        self.__new_menu.entryconfig(mKey.KEY_HTML_PAGE, state=new_state)
        self.__new_menu.entryconfig(mKey.KEY_CSS_RULE, state=new_state)
        self.__new_menu.entryconfig(mKey.KEY_JAVASCRIPT, state=new_state)
        self.__new_menu.entryconfig(mKey.KEY_TEXT, state=new_state)
        self.__new_menu.entryconfig(mKey.KEY_VARIABLE, state=new_state)
        self.__edit_menu.entryconfig(mKey.KEY_RENAME_PROJECT, state=new_state)
        self.__file_menu.entryconfig(mKey.KEY_GENERATE, state=new_state)
        
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
    def get_page_overview_frame(self) -> tk.Frame:
        '''
        '''
        return self.__page_overview_frame

    def __create_page_config_frame(self):
        '''
        '''
        self.__page_config_frame = tk.Frame(self.__right_side, background='#000000', 
                                            #width=self.__cell_width*2, height=self.__cell_height*3
                                            )
        #self.__page_config_frame.grid(row=0, column=1, columnspan=2)
        self.__page_config_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        
    def __create_attributes_fram(self):
        '''
        '''
        self.__attributes_frame = tk.Frame(self.__right_side, background='#222222', 
                                           #width=self.__cell_width, height=self.__cell_height*3
                                           )
        #self.__attributes_frame.grid(row=0, column=3)
        self.__attributes_frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        
        
    def __create_page_overview_frame(self):
        '''
        '''
        self.__page_overview_frame = tk.Frame(self, background='#444444')
        #self.__page_overview_frame.grid(row=0, column=0)
        self.__page_overview_frame.pack(fill=tk.Y, side=tk.LEFT)
        
        

    def __on_new_project(self):
        self.__last_event.event_source = mKey.KEY_PROJECT
        self.notify_new()
    
    
    def __on_new_html_page(self):
        self.__last_event.event_source = mKey.KEY_HTML_PAGE
        self.notify_new()
    
    
    def __on_new_javascript(self):
        self.__last_event.event_source = mKey.KEY_JAVASCRIPT
        self.notify_new()
    
    
    def __on_new_css_rule(self):
        self.__last_event.event_source = mKey.KEY_CSS_RULE
        self.notify_new()
    
    
    def __on_new_text(self):
        self.__last_event.event_source = mKey.KEY_TEXT
        self.notify_new()
    
    
    def __on_open(self):
        '''
        Function which is called
        after the open menu item is pressed.
        '''
        self.__last_event.event_source = mKey.KEY_OPEN
        self.notify_open()
    
    
    def __on_save(self):
        
        self.__last_event.event_source = mKey.KEY_SAVE
        self.notify_save()
    
    
    def __on_save_as(self):
        pass
    
    
    def __on_exit(self):
        '''
        Function which is called when the exit menu
        item is selected.
        '''
        self.__last_event.event_source = mKey.KEY_EXIT
        self.notify_exit()
    
    
    def __on_new_variable(self):
        self.__last_event.event_source = mKey.KEY_VARIABLE
        self.notify_new()
    
    
    def __create_file_menu(self):
        '''
        '''
        self.__file_menu = tk.Menu(self.__menubar, tearoff=0)
        
        self.__new_menu = tk.Menu(self.__menubar, tearoff=0)
        self.__new_menu.add_command(label=mKey.KEY_PROJECT, command=lambda: self.__on_new_project())
        self.__new_menu.add_separator()
        self.__new_menu.add_command(label=mKey.KEY_HTML_PAGE, command=lambda: self.__on_new_html_page())
        self.__new_menu.entryconfig(mKey.KEY_HTML_PAGE, state=tk.DISABLED)
        self.__new_menu.add_command(label=mKey.KEY_CSS_RULE, command=lambda: self.__on_new_css_rule())
        self.__new_menu.entryconfig(mKey.KEY_CSS_RULE, state=tk.DISABLED)
        self.__new_menu.add_command(label=mKey.KEY_JAVASCRIPT, command=lambda: self.__on_new_javascript())
        self.__new_menu.entryconfig(mKey.KEY_JAVASCRIPT, state=tk.DISABLED)
        self.__new_menu.add_separator()
        self.__new_menu.add_command(label=mKey.KEY_TEXT, command=lambda: self.__on_new_text())
        self.__new_menu.entryconfig(mKey.KEY_TEXT, state=tk.DISABLED)
        self.__new_menu.add_command(label=mKey.KEY_VARIABLE, command=lambda: self.__on_new_variable())
        self.__new_menu.entryconfig(mKey.KEY_VARIABLE, state=tk.DISABLED)
        self.__file_menu.add_cascade(label=mKey.KEY_NEW, menu=self.__new_menu)
        
        self.__file_menu.add_command(label=mKey.KEY_OPEN, command=lambda: self.__on_open())
        self.__file_menu.add_separator()
        self.__file_menu.add_command(label=mKey.KEY_SAVE, command=lambda: self.__on_save())
        #self.__file_menu.entryconfig(mKey.KEY_SAVE, state=tk.DISABLED)
        self.__file_menu.add_command(label=mKey.KEY_SAVE_AS, command=lambda: self.__on_save_as())
        self.__file_menu.entryconfig(mKey.KEY_SAVE_AS, state=tk.DISABLED)
                
        self.__file_menu.add_separator()        

        generate_menu = tk.Menu(self.__menubar, tearoff=0)
        generate_menu.add_command(label=mKey.KEY_HTML_PAGE, command=lambda: self.__on_generate_html_page())
        generate_menu.add_command(label=mKey.KEY_CSS, command=lambda: self.__on_generate_css())
        generate_menu.add_command(label=mKey.KEY_JAVASCRIPT, command=lambda: self.__on_generate_javascript())
        
        generate_menu.add_separator()
        
        generate_menu.add_command(label=mKey.KEY_SELENIUM_TEST_CASES, command=lambda: self.__on_selenium_test_cases())
        
        generate_menu.add_separator()
        
        generate_menu.add_command(label=mKey.KEY_ALL, command=lambda: self.__on_generate_all())
                       
        self.__file_menu.add_cascade(label=mKey.KEY_GENERATE, menu=generate_menu)
        self.__file_menu.entryconfig(mKey.KEY_GENERATE, state=tk.DISABLED)
        
        self.__file_menu.add_separator()
        self.__file_menu.add_command(label=mKey.KEY_EXIT, command=lambda: self.__on_exit())
    
        self.__menubar.add_cascade(label=mKey.KEY_FILE, menu=self.__file_menu)
        

    def __on_undo(self):
        pass
    
    
    def __on_redo(self):
        pass
    
    
    def __on_rename_project(self):
        self.__last_event.event_source = mKey.KEY_RENAME_PROJECT
        self.notify_rename()
    
    
    def __on_rename_page(self):
        self.__last_event.event_source = mKey.KEY_RENAME
        self.notify_rename()
    
    def __on_edit_css_rule(self):
        pass
    
    
    def __on_edit_javascript(self):
        pass
    
    
    def __on_edit_text(self):
        pass
    
    
    def __on_edit_variable(self):
        pass
    
    
    def __create_edit_menu(self):
        '''
        '''
        self.__edit_menu = tk.Menu(self.__menubar, tearoff=0)
        
        self.__edit_menu.add_command(label=mKey.KEY_UNDO, command=lambda: self.__on_undo())
        self.__edit_menu.entryconfig(mKey.KEY_UNDO, state=tk.DISABLED)
        self.__edit_menu.add_command(label=mKey.KEY_REDO, command=lambda: self.__on_redo())
        self.__edit_menu.entryconfig(mKey.KEY_REDO, state=tk.DISABLED)

        self.__edit_menu.add_separator()
        
        self.__edit_menu.add_command(label=mKey.KEY_RENAME_PROJECT, command=lambda: self.__on_rename_project())
        self.__edit_menu.entryconfig(mKey.KEY_RENAME_PROJECT, state=tk.DISABLED)
        self.__edit_menu.add_command(label=mKey.KEY_RENAME, command=lambda: self.__on_rename_page())
        self.__edit_menu.entryconfig(mKey.KEY_RENAME, state=tk.DISABLED)
        
        self.__edit_menu.add_separator()
        
        self.__edit_menu.add_command(label=mKey.KEY_CSS_RULE, command=lambda: self.__on_edit_css_rule())
        self.__edit_menu.entryconfig(mKey.KEY_CSS_RULE, state=tk.DISABLED)
        self.__edit_menu.add_command(label=mKey.KEY_JAVASCRIPT, command=lambda: self.__on_edit_javascript())
        self.__edit_menu.entryconfig(mKey.KEY_JAVASCRIPT, state=tk.DISABLED)
        self.__edit_menu.add_command(label=mKey.KEY_TEXT, command=lambda: self.__on_edit_text())
        self.__edit_menu.entryconfig(mKey.KEY_TEXT, state=tk.DISABLED)
        self.__edit_menu.add_command(label=mKey.KEY_VARIABLE, command=lambda: self.__on_edit_variable())
        self.__edit_menu.entryconfig(mKey.KEY_VARIABLE, state=tk.DISABLED)
                
        self.__menubar.add_cascade(label=mKey.KEY_EDIT, menu=self.__edit_menu)

    
    def __on_add_child(self):
        self.__last_event.event_source = mKey.KEY_ADD_CHILD
        self.notify_add()
    
    
    def __on_add_attribute(self):
        self.__last_event.event_source = mKey.KEY_ADD_ATTRIBUTE
        self.notify_add()
    
    
    def __on_add_event(self):
        pass
    
    
    def __on_add_text(self):
        self.__last_event.event_source = mKey.KEY_ADD_TEXT
        self.notify_add()
    
    
    def __on_move_up(self):
        pass
    
    
    def __on_move_down(self):
        pass
    
    
    def __on_change_parent(self):
        pass
    
    
    def __on_delete_tag(self):
        pass
    
    
    def __on_delete_attribute(self):
        pass
    
    
    def __on_delete_event(self):
        pass
    
    
    def __on_delete_text(self):
        pass
    
    
    def __on_generate_html_page(self):
        pass
    
    
    def __on_generate_css(self):
        pass
    
    
    def __on_generate_javascript(self):
        pass
    
    
    def __on_selenium_test_cases(self):
        pass
    
    
    def __on_generate_all(self):
        pass
    
    
    def __create_html_page_menu(self):
        
        self.__html_page_menu = tk.Menu(self.__menubar, tearoff=0)
        
        self.__html_page_menu.add_command(label=mKey.KEY_ADD_CHILD, command=lambda: self.__on_add_child())
        self.__html_page_menu.entryconfig(mKey.KEY_ADD_CHILD, state=tk.DISABLED)
        self.__html_page_menu.add_command(label=mKey.KEY_ADD_TEXT, command=lambda: self.__on_add_text())
        self.__html_page_menu.entryconfig(mKey.KEY_ADD_TEXT, state=tk.DISABLED)
        
        self.__html_page_menu.add_separator()
        
        self.__html_page_menu.add_command(label=mKey.KEY_MOVE_UP, command=lambda: self.__on_move_up())
        self.__html_page_menu.entryconfig(mKey.KEY_MOVE_UP, state=tk.DISABLED)
        self.__html_page_menu.add_command(label=mKey.KEY_MOVE_DOWN, command=lambda: self.__on_move_down())
        self.__html_page_menu.entryconfig(mKey.KEY_MOVE_DOWN, state=tk.DISABLED)
        self.__html_page_menu.add_command(label=mKey.KEY_CHANGE_PARENT, command=lambda: self.__on_change_parent())
        self.__html_page_menu.entryconfig(mKey.KEY_CHANGE_PARENT, state=tk.DISABLED)
        
        self.__html_page_menu.add_separator()

        self.__html_page_menu.add_command(label=mKey.KEY_DELETE_TAG, command=lambda: self.__on_delete_tag())
        self.__html_page_menu.entryconfig(mKey.KEY_DELETE_TAG, state=tk.DISABLED)
        self.__html_page_menu.add_command(label=mKey.KEY_DELETE_ATTRIBUTE, command=lambda: self.__on_delete_attribute())
        self.__html_page_menu.entryconfig(mKey.KEY_DELETE_ATTRIBUTE, state=tk.DISABLED)
        self.__html_page_menu.add_command(label=mKey.KEY_DELETE_EVENT, command=lambda: self.__on_delete_event())
        self.__html_page_menu.entryconfig(mKey.KEY_DELETE_EVENT, state=tk.DISABLED)
        self.__html_page_menu.add_command(label=mKey.KEY_DELETE_TEXT, command=lambda: self.__on_delete_text())
        self.__html_page_menu.entryconfig(mKey.KEY_DELETE_TEXT, state=tk.DISABLED)
                       
        self.__menubar.add_cascade(label=mKey.KEY_HTML_HYPHEN_PAGE, menu=self.__html_page_menu)
    
    
    @overrides
    def register_observer(self, observer:ABSMainWindowObserver) -> None:
        '''
        '''
        self.__observers.append(observer)
       
    @overrides 
    def unregister_observer(self, observer:ABSMainWindowObserver) -> None:
        '''
        '''
        self.__observers.remove(observer)
        
    @overrides
    def notify_save_as(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_save_as(self.__last_event)
        
    @overrides
    def notify_save(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_save(self.__last_event)
        
    @overrides
    def notify_open(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_open(self.__last_event)
        
    @overrides
    def notify_new(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_new(self.__last_event)
        
    @overrides
    def notify_exit(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_exit(self.__last_event)
        
    @overrides
    def notify_undo(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_undo(self.__last_event)
    
    @overrides
    def notify_rename(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_rename(self.__last_event)
        
    @overrides
    def notify_edit(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_edit(self.__last_event)
    
    @overrides
    def notify_add(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_add(self.__last_event)
        
    @overrides
    def notify_delete(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_delete(self.__last_event)
        
    @overrides
    def notify_generate(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_generate(self.__last_event)
        
    @overrides
    def notify_move(self) -> None:
        '''
        '''
        for observer in self.__observers:
            observer.on_move(self.__last_event)