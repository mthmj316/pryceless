'''
Created on 04.08.2020

@author: mthoma
'''
import tkinter as tk
from main_window.abs_main_window import ABSMainWindowUI, ABSMainWindowObserver,\
    ABSMainWindowMo, MainWindowMenuKeys
from main_window.main_window_ui import MainWindowUI
from overrides.overrides import overrides
from utils.utils import Event
from main_window.main_window_mo import MainWindowMo
from tkinter.messagebox import askyesnocancel
from controls.overview_control import OverviewControl,\
    OverviewControlObserver
from controls.configuration_control import ConfigurationControl,\
    ConfigurationControlObserver
from controls.properties_control import PropertiesControl,\
    PropertiesControlObserver
from tkinter import simpledialog

class MainWindowCNTLR(ABSMainWindowObserver, OverviewControlObserver,
                      ConfigurationControlObserver,
                      PropertiesControlObserver):
    '''
    classdocs
    '''
    __root: tk.Tk = tk.Tk()

    __gui: ABSMainWindowUI = MainWindowUI(__root)
    
    __model: ABSMainWindowMo = MainWindowMo()
    
    __overview: OverviewControl = None
    
    __configuration: ConfigurationControl = None
    
    __properties: PropertiesControl = None
    
    #Window title which is displayed directly after application start.
    __base_title: str = None

    def __init__(self):
        '''
        Constructor
        '''
        self.__overview = OverviewControl(self.__gui.get_page_overview_frame())
        self.__overview.add_obeserver(self)
        
        self.__configuration = ConfigurationControl(self.__gui.get_page_config_frame())
        self.__configuration.add_obeserver(self)
        
        self.__properties = PropertiesControl(self.__gui.get_attributes_frame())
        self.__properties.add_obeserver(self)
        
        
    def show(self, title:str='TITLE'):
        '''
        '''   
        self.__gui.pack(side="top", fill="both", expand=True)
        self.__gui.register_observer(self)        
        
        self.__root.attributes('-zoomed', True)
        
        self.__base_title = title
        
        self.__root.title(self.__base_title)
        self.__root.mainloop()
        
    @overrides
    def on_save_as(self, event:Event) -> None:
        '''
        '''
        
    @overrides
    def on_save(self, event:Event) -> None:
        '''
        '''
        
    @overrides
    def on_open(self, event:Event) -> None:  # @UnusedVariable
        '''
        '''
        # if project is open:
        #    if project is changed
        #        open askyesno: save changes
        #        if yes
        #            save changes
        #        open askopenfilename dialog
        #    else
        #        open askopenfilename dialog
        # else
        #    open askopenfilename dialog
        #
        # if project open:
        #    load data into the main window
        
        is_project_open = self.__model.is_project_open()
        
        open_askopenfilename = False
        
        if is_project_open:
            
            open_askopenfilename = self.__check_and_save_changes()
            
        else:
            open_askopenfilename = True
            
        
        if open_askopenfilename:
            is_project_open = self.__model.open_project()

        if is_project_open:
            #Load data into the ui
            self.__load_data_in_view()
        
        self.__enable_menu()
    
    def __load_data_in_view(self):
        self.__update_title()
        self.__load_page_config()
        self.__load_page_overview()
        
    def __update_title(self):
        self.__root.title(' - '.join([self.__base_title,
                                      self.__model.get_project_name()]))
    
    def __load_page_config(self):
        '''
        Loads the model data into the view
        '''
        self.__configuration.remove_all()
        self.__properties.remove_all()
        
        if not self.__model.selected() == None:
            for item in self.__model:
                self.__configuration.insert_conf(item[0], item[2], item[1])
    
    def __load_page_overview(self):
        self.__overview.remove_all()
        
        overview = self.__model.get_overview_data()
        
        for page_id in overview.keys():
            self.__overview.insert(page_id, overview[page_id])
            
        self.__overview.select(self.__model.selected())    
                
        
    def __enable_menu(self):
        
        #save, save as ..., undo may only be enabled if model.has_changes() == True
        #redo -> only if undo has been performed
        #HTML Page, CSS Rule, JavaScript, Text, Variable, and Rename Project
        #may only enabled if an project is open
        #Select Page -> at least two pages must exist
        #Rename Page -> at least one page must exist
        #Edit CSS Rule -> at least one CSS Rule must exist
        #Edit JavaScript -> dto Javascript
        #Edit Text -> dto Text
        #Edit Variable -> dto Variable
        #Generate -> Project must be opend
        #Add ... -> Tag must be selected
        # Delete ... -> dto 
        
        self.__gui.enable_menu_project_depending(self.__model.is_project_open())
        self.__gui.enable_menu_overview_depending(self.__model.is_selected())
        
    def __check_and_save_changes(self) -> bool:
        '''
        Check if the model is changed
        If the model is changed it asks the user if changes shall be saved:
            User answer:
                'yes'    -> changes are saved -> return == True
                'no'     -> changes won't be saved -> return == True
                'cancel' -> changes won't be saved -> return == False
        If the model is unchanged -> return == True
        
        Note: Only if this method returns True the process may be continued.
        If False is returned the process must be discontinued
        '''
        if self.__model.has_changes():
            #Model is changed -> ask user if changes shall be saved.                
                user_answer = askyesnocancel('Save on close', 
                                     'Save changes before closing the project?')
                if not user_answer == None:
                    #Either 'yes' or 'no' has been pressed
                    #Hence True must be returned
                    if user_answer:
                        #'yes' has been pressed.
                        #Save project and open a new one
                        self.__model.save()
                        
                    return True
                else:
                    # cancel has been pressed 
                    #-> process must be discontinued
                    return False
        else:
            #Model is unchanged
            return True
        
    @overrides
    def on_new(self, event:Event) -> None:
        '''
        '''
        print(event.event_source)
        if event.event_source == MainWindowMenuKeys.KEY_PROJECT:
            
            if self.__model.is_project_open() \
                and not self.__check_and_save_changes():
                # user has cancelled the process
                return
            
            self.__model.create_new_project()

            if self.__model.is_project_open():  
                #Only needed when project has been actually created.
                self.__load_page_overview()
                
            self.__enable_menu()
            
        elif event.event_source == MainWindowMenuKeys.KEY_HTML_PAGE:
            self.__model.create_page()
            self.__load_data_in_view()
        elif event.event_source == MainWindowMenuKeys.KEY_CSS_RULE:
            self.__model.create_css_rule()
            self.__load_data_in_view()
        elif event.event_source == MainWindowMenuKeys.KEY_JAVASCRIPT:
            self.__model.create_javascript()
            self.__load_data_in_view()
        elif event.event_source == MainWindowMenuKeys.KEY_TEXT:
            self.__model.create_text()
            self.__load_data_in_view()
        elif event.event_source == MainWindowMenuKeys.KEY_VARIABLE:
            self.__model.create_variable()
            self.__load_data_in_view()
            
            
            
            
            
    
    @overrides
    def on_exit(self, event:Event) -> None:  # @UnusedVariable
        '''
        '''
        
        perform_exit = True
        
        if self.__model.is_project_open():
            perform_exit = self.__check_and_save_changes()
        
        #if perform_exit == False, then the user has canceled
        # the exit during the check and save changes process.
        if perform_exit:
            self.__gui.unregister_observer(self)
            self.__root.quit()
        
    @overrides
    def on_undo(self, event:Event) -> None:
        '''
        '''
    
    @overrides
    def on_rename(self, event:Event) -> None:
        '''
        '''
        if event.event_source == MainWindowMenuKeys.KEY_RENAME_PROJECT:
            self.__model.rename_project()
            self.__load_data_in_view()
            
        elif event.event_source == MainWindowMenuKeys.KEY_RENAME:
            self.__model.rename()
            self.__load_data_in_view()
        
    @overrides
    def on_edit(self, event:Event) -> None:
        '''
        '''
        
    @overrides
    def on_add(self, event:Event) -> None:
        '''
        '''
        
    @overrides
    def on_delete(self, event:Event) -> None:
        '''
        '''
        
    @overrides
    def on_generate(self, event:Event) -> None:
        '''
        '''
        
    @overrides
    def on_move(self, event:Event) -> None:
        '''
        '''  
    
    @overrides
    def on_page_selected(self, page_id:str)-> None:
        '''
        '''
        self.__model.select(page_id)
        self.__load_page_config()
        self.__enable_menu()
        
        '''
        print(page_id)
        
        for item in self.__model:
            print(item)  
        '''
        
    @overrides
    def on_conf_selected(self, sub_id:str)->None:
        
        self.__model.select_sub(sub_id)
        
        self.__properties.remove_all()
        
        if not sub_id == None:
            
            properties = self.__model.get_sub_data()
            for _property in properties:
                self.__properties.insert(_property[0], _property[1], _property[2])
            
        
    @overrides
    def on_property_selected(self, _id:str) -> None:
        '''
        Is called after a page has been selected.
        page_id -> id of the selected page
        if the root element is selected None will be returned.
        '''
        if not _id == None:
            answer = simpledialog.askstring("Input", ''.join(['Set: ', _id.split('.')[-1]]), 
                                            parent=self.__root, initialvalue=self.__model.get_property_value(_id))
            
            print(answer)
        