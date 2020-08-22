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
from tkinter import simpledialog



class MainWindowCNTLR(ABSMainWindowObserver):
    '''
    classdocs
    '''
    __root: tk.Tk = tk.Tk()

    __gui: ABSMainWindowUI = MainWindowUI(__root)
    
    __model: ABSMainWindowMo = MainWindowMo()
    
    #Window title which is displayed directly after application start.
    __base_title: str = None

    def __init__(self):
        '''
        Constructor
        '''
        
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
            self.__root.title(' - '.join([self.__base_title, 
                                         self.__model.get_project_name()]))
    
     
           
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
        if event.event_source == MainWindowMenuKeys.KEY_PROJECT:
            self.__model.create_new_project()
            
    
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
        
    @overrides
    def on_edit(self, event:Event) -> None:
        '''
        '''
    
    @overrides
    def on_select_page(self, event:Event) -> None:
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