'''
Created on 04.08.2020

@author: mthoma
'''
import tkinter as tk
from main_window.abs_main_window import ABSMainWindowUI, ABSMainWindowObserver,\
    ABSMainWindowMo
from main_window.main_window_ui import MainWindowUI
from overrides.overrides import overrides
from utils.utils import Event
from main_window.main_window_mo import MainWindowMo
from tkinter.messagebox import askyesnocancel



class MainWindowCNTLR(ABSMainWindowObserver):
    '''
    classdocs
    '''
    __root: tk.Tk = tk.Tk()

    __gui: ABSMainWindowUI = MainWindowUI(__root)
    
    __model: ABSMainWindowMo = MainWindowMo()

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
        self.__root.title(title)
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
            
            if self.__model.has_changes():
                
                user_answer = askyesnocancel('Save on close', 
                                     'Save changes before closing the project?')
                if not user_answer == None:
                    #Either 'yes' or 'no' has been pressed
                    #Hence project selection must be opened.
                    open_askopenfilename = True
                    if user_answer:
                        #'yes' has been pressed.
                        #Save project and open a new one
                        self.__model.save()
                #else: cancel has been pressed 
                #-> don't ask for project
                
            else:
                open_askopenfilename = True
            
        else:
            open_askopenfilename = True
            
        
        if open_askopenfilename:
            is_project_open = self.__model.open_project()

        if is_project_open:
            #Load data into the ui
            pass
        
    @overrides
    def on_new(self, event:Event) -> None:
        '''
        '''
        
    @overrides
    def on_exit(self, event:Event) -> None:  # @UnusedVariable
        '''
        '''
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