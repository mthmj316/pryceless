'''
Created on 04.08.2020

@author: mthoma
'''
from controls.configuration_control import ConfigurationControl, \
    ConfigurationControlObserver
from controls.overview_control import OverviewControl, \
    OverviewControlObserver
from main_window.abs_main_window import ABSMainWindowUI, ABSMainWindowObserver, \
    ABSMainWindowMo, MainWindowMenuKeys, ABSMainWindowModelObserver
from main_window.main_window_mo import MainWindowMo
from main_window.main_window_ui import MainWindowUI
from overrides.overrides import overrides
import tkinter as tk
from tkinter.messagebox import askyesnocancel
from utils.utils import Event
from controls.treeview_control import TreeViewObserver, TreeViewConfiguration,\
    TreeViewControl, TreeViewItem
from utils.logger import log_enter_func, log_leave_func, log_set_var


class MainWindowCNTLR(ABSMainWindowObserver, OverviewControlObserver,
                      ConfigurationControlObserver,
                      TreeViewObserver,
                      ABSMainWindowModelObserver):
    '''
    classdocs
    '''
    __root: tk.Tk = tk.Tk()

    __gui: ABSMainWindowUI = MainWindowUI(__root)
    
    __model: ABSMainWindowMo = MainWindowMo()
    
    __overview: OverviewControl = None
    
    __configuration: ConfigurationControl = None
    
    #Window title which is displayed directly after application start.
    __base_title: str = None

    def __init__(self):
        '''
        Constructor
        '''
        log_enter_func('MainWindowCNTLR', '__init__')
        
        
        self.__overview = OverviewControl(self.__gui.get_page_overview_frame())
        self.__overview.add_obeserver(self)
        
        self.__configuration = ConfigurationControl(self.__gui.get_page_config_frame())
        self.__configuration.add_obeserver(self)
        
        treeview_conf = TreeViewConfiguration()
        treeview_conf.column_count = 2
        treeview_conf.add_column_name('Property', 0)
        treeview_conf.add_column_name('Value', 1)
                
        log_set_var('MainWindowCNTLR', '__init__', 'treeview_conf', treeview_conf)
        
        self.__properties = TreeViewControl(self.__gui.get_attributes_frame(), treeview_conf)
        self.__properties.add_observer(self)
        
        self.__model.add_observer(self)
        
        log_leave_func('MainWindowCNTLR', '__init__')
        
        
    def show(self, title:str='TITLE'):
        '''
        '''  
        log_enter_func('MainWindowCNTLR', 'show', {'title':title})
        
        
        self.__gui.pack(side="top", fill="both", expand=True)
        self.__gui.register_observer(self)        
        
        try:
            self.__root.attributes('-zoomed', True)
        except:
            pass
            
        
        self.__base_title = title
        
        self.__root.title(self.__base_title)
        self.__root.mainloop()
        
        log_leave_func('MainWindowCNTLR', 'show')
        
    @overrides
    def on_save_as(self, event:Event) -> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_save_as', {'event':event})
        
        log_leave_func('MainWindowCNTLR', 'on_save_as')
        
    @overrides
    def on_save(self, event:Event) -> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_save', {'event':event})
        self.__model.save()
        log_leave_func('MainWindowCNTLR', 'on_save')
        
    @overrides
    def on_open(self, event:Event) -> None:  # @UnusedVariable
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_open', {'event':event})
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
                
        log_set_var('MainWindowCNTLR', 'on_open', 'is_project_open', is_project_open)
        
        open_askopenfilename = False
        
        if is_project_open:
            
            open_askopenfilename = self.__check_and_save_changes()
            
        else:
            open_askopenfilename = True
            
        
        if open_askopenfilename:
            is_project_open = self.__model.open_project()       
            log_set_var('MainWindowCNTLR', 'on_open', 'is_project_open', is_project_open)

        if is_project_open:
            #Load data into the ui
            self.__load_data_in_view()
        
        self.__enable_menu()
        
        log_leave_func('MainWindowCNTLR', 'on_open')
    
    def __load_data_in_view(self):
        log_enter_func('MainWindowCNTLR', '__load_data_in_view')
        
        self.__update_title()
        self.__load_page_config()
        self.__load_page_overview()
        self.__configuration.select(self.__model.selected_sub())
        
        log_leave_func('MainWindowCNTLR', '__load_data_in_view')
        
    def __update_title(self):
        log_enter_func('MainWindowCNTLR', '__update_title')
        
        self.__root.title(' - '.join([self.__base_title,
                                      self.__model.get_project_name()]))
        
        log_leave_func('MainWindowCNTLR', '__update_title')
    
    def __load_page_config(self):
        '''
        Loads the model data into the view
        '''
        log_enter_func('MainWindowCNTLR', '__load_page_config')
        
        self.__configuration.remove_all()
        self.__properties.remove()
        
        if not self.__model.selected() == None:
            for item in self.__model:
                self.__configuration.insert_conf(item[0], item[2], item[1])
        
        log_leave_func('MainWindowCNTLR', '__load_page_config')
    
    def __load_page_overview(self):
        log_enter_func('MainWindowCNTLR', '__load_page_overview')
        
        self.__overview.remove_all()
        
        overview = self.__model.get_overview_data()
        
        for page_id in overview.keys():
            self.__overview.insert(page_id, overview[page_id])
            
        self.__overview.select(self.__model.selected())   
        
        log_leave_func('MainWindowCNTLR', '__load_page_overview') 
                
        
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
        log_enter_func('MainWindowCNTLR', '__enable_menu')
        
        self.__gui.enable_menu_project_depending(self.__model.is_project_open())
        self.__gui.enable_menu_overview_depending(self.__model.is_selected())
        self.__gui.enable_menu_conf_depending(self.__model.is_sub_selected())
        
        log_leave_func('MainWindowCNTLR', '__enable_menu') 
        
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
        log_enter_func('MainWindowCNTLR', '__check_and_save_changes')
        
        if self.__model.has_changes():
            #Model is changed -> ask user if changes shall be saved.                
                user_answer = askyesnocancel('Save on close', 
                                     'Save changes before closing the project?')  
                              
                log_set_var('MainWindowCNTLR', '__check_and_save_changes', 'user_answer', user_answer)
                
                if not user_answer == None:
                    #Either 'yes' or 'no' has been pressed
                    #Hence True must be returned
                    if user_answer:
                        #'yes' has been pressed.
                        #Save project and open a new one
                        self.__model.save()
                        
                    log_leave_func('MainWindowCNTLR', '__check_and_save_changes', True) 
                    return True
                else:
                    # cancel has been pressed 
                    #-> process must be discontinued
                    log_leave_func('MainWindowCNTLR', '__check_and_save_changes', False) 
                    return False
        else:
            #Model is unchanged
            log_leave_func('MainWindowCNTLR', '__check_and_save_changes', True) 
            return True
        
        
    @overrides
    def on_new(self, event:Event) -> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_new', {'event':event})
        
        log_set_var('MainWindowCNTLR', 'on_new', 'event.event_source', event.event_source)
        
        if event.event_source == MainWindowMenuKeys.KEY_PROJECT:
            
            if self.__model.is_project_open() \
                and not self.__check_and_save_changes():
                # user has cancelled the process
                return
            
            self.__model.create_new_project()
            
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
        
        log_leave_func('MainWindowCNTLR', 'on_new') 
            
            
    @overrides
    def on_exit(self, event:Event) -> None:  # @UnusedVariable
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_exit', {'event':event})
        
        perform_exit = True
        
        if self.__model.is_project_open():
            perform_exit = self.__check_and_save_changes()
        
        log_set_var('MainWindowCNTLR', 'on_exit', 'perform_exit', perform_exit)
        
        #if perform_exit == False, then the user has canceled
        # the exit during the check and save changes process.
        if perform_exit:
            self.__gui.unregister_observer(self)
            self.__root.quit()
        
        log_leave_func('MainWindowCNTLR', 'on_exit') 
        
    @overrides
    def on_undo(self, event:Event) -> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_undo', {'event':event})
        
        log_leave_func('MainWindowCNTLR', 'on_undo') 
    
    @overrides
    def on_rename(self, event:Event) -> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_rename', {'event':event})
        
        log_set_var('MainWindowCNTLR', 'on_rename', 'event.event_source', event.event_source)
        
        if event.event_source == MainWindowMenuKeys.KEY_RENAME_PROJECT:
            self.__model.rename_project()
            self.__load_data_in_view()
            
        elif event.event_source == MainWindowMenuKeys.KEY_RENAME:
            self.__model.rename()
            self.__load_data_in_view()
            
        log_leave_func('MainWindowCNTLR', 'on_rename') 
        
    @overrides
    def on_edit(self, event:Event) -> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_edit', {'event':event})
        
        log_leave_func('MainWindowCNTLR', 'on_edit') 
        
    @overrides
    def on_add(self, event:Event) -> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_add', {'event':event})
        
        if event.event_source == MainWindowMenuKeys.KEY_ADD_CHILD:
            self.__model.create_child()
        elif event.event_source == MainWindowMenuKeys.KEY_ADD_ATTRIBUTE:
            self.__model.add_property()
        elif event.event_source == MainWindowMenuKeys.KEY_ADD_TEXT:
            self.__model.set_text()
            
        log_leave_func('MainWindowCNTLR', 'on_add') 
        
    @overrides
    def on_delete(self, event:Event) -> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_edit', {'event':event})
        
        log_leave_func('MainWindowCNTLR', 'on_edit') 
        
    @overrides
    def on_generate(self, event:Event) -> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_generate', {'event':event})
        
        log_leave_func('MainWindowCNTLR', 'on_generate') 
        
    @overrides
    def on_move(self, event:Event) -> None:
        '''
        '''  
        log_enter_func('MainWindowCNTLR', 'on_move', {'event':event})
        
        log_leave_func('MainWindowCNTLR', 'on_move') 
    
    @overrides
    def on_page_selected(self, page_id:str)-> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_page_selected', {'page_id':page_id})
        
        self.__model.select(page_id)
        self.__load_page_config()
        self.__enable_menu()
        
        log_leave_func('MainWindowCNTLR', 'on_page_selected') 
        
    @overrides
    def on_conf_selected(self, sub_id:str)->None:
        
        log_enter_func('MainWindowCNTLR', 'on_conf_selected', {'sub_id':sub_id})
        
        self.__model.select_sub(sub_id)
        self.__properties.remove()
        self.__enable_menu()
        
        if not sub_id == None:
            self.__load_properties()
            
        log_leave_func('MainWindowCNTLR', 'on_conf_selected') 
            
    def __load_properties(self):
        
        log_enter_func('MainWindowCNTLR', '__load_properties')
        
        for treeview_item in self.__model.get_sub_data():
            self.__properties.insert(treeview_item)    
            
        log_leave_func('MainWindowCNTLR', '__load_properties')    
        

    @overrides
    def on_error(self, error_msg:str)->None:
        log_enter_func('MainWindowCNTLR', 'on_error', {'error_msg':error_msg})
        
        log_leave_func('MainWindowCNTLR', 'on_error')

    @overrides
    def on_select(self, item:TreeViewItem)->None:
        log_enter_func('MainWindowCNTLR', 'on_select', {'item':item})
        
        log_leave_func('MainWindowCNTLR', 'on_select')
        

    @overrides
    def on_double_click(self, item:TreeViewItem)->None:
        
        log_enter_func('MainWindowCNTLR', 'on_double_click', {'item':item})
        
        if not item == None:
            self.__model.set_property(item.id)
    
        log_leave_func('MainWindowCNTLR', 'on_double_click')
        
    @overrides
    def on_model_changed(self, change_typ:int) -> None:
        '''
        '''
        log_enter_func('MainWindowCNTLR', 'on_model_changed', {'change_typ':change_typ})
        
        if change_typ == ABSMainWindowModelObserver.PROPERTY_CHANGE_TYPE:
            self.__properties.remove()
            self.__load_properties()
            return
        
        self.__load_data_in_view()
        
        log_leave_func('MainWindowCNTLR', 'on_model_changed')
        
###################################################################
###################################################################
###################################################################
        