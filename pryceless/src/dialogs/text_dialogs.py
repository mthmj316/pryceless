'''
Created on 03.09.2020

@author: mthoma
'''
import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox

class ABSTextDialogObserver(ABC):
    
    @abstractmethod
    def on_text_selected(self, result=None):
        '''
        '''

class SelectText(object):
    '''
    classdocs
    '''
    __observer: ABSTextDialogObserver = None
     
    __dialog: tk.Toplevel = None
    
    __id_var: tk.StringVar = None
    
    __tag_var: tk.StringVar = None
    
    __position_var: tk.StringVar = None
    
    __text_elements: dict = {}

    def __init__(self, text_elements, observer:ABSTextDialogObserver, master=None):
        '''
        Constructor
        '''
        self.__text_elements = text_elements
        
        self.__observer = observer
        
        self.__id_var = tk.StringVar()
        self.__tag_var = tk.StringVar()
        self.__position_var = tk.StringVar()

        self.__text_select_dialog(master)
        
    def __text_select_dialog(self, master):
        '''
        '''
        
        self.__dialog = tk.Toplevel(master)
        self.__dialog.title('Select Text')
        
        top_frame = tk.Frame(self.__dialog)
        top_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=10, pady=10)
        
        possible_tags = ['text']
    
        tk.Label(top_frame, text='Text Collections:', anchor=tk.W).grid(row=0,column=0, padx=10, sticky=tk.W)
        tk.OptionMenu(top_frame, self.__tag_var, *possible_tags).grid(row=0,column=1, columnspan=1,sticky=tk.W, padx=10)
        
        tk.Label(top_frame, text='Text :', anchor=tk.W).grid(row=1,column=0, padx=10, sticky=tk.W)
        tk.OptionMenu(top_frame, self.__tag_var, *possible_tags).grid(row=1,column=1, columnspan=1,sticky=tk.W, padx=10)
        
        buttons_frame = tk.Frame(self.__dialog)
        buttons_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=20)
        
        tk.Button(buttons_frame, text='Ok', command=self.__on_ok).pack(side=tk.LEFT, padx=1)
        tk.Button(buttons_frame, text='Cancel', command=self.__on_cancel).pack(side=tk.LEFT, padx=1)
        
    
    def __on_ok(self):
        
        tag_id = self.__id_var.get()
        tag = self.__tag_var.get()
        position = self.__position_var.get()

        if tag_id == '':
            messagebox.showerror('Input Error', 'Tag ID not set!')
        elif tag == '':
            messagebox.showerror('Input Error', 'Tag not set!')
        elif position == '':
            messagebox.showerror('Input Error', 'Position not set!')            
        elif not position.isdigit():
            messagebox.showerror('Input Error', 'Position is not a number!')            
        else:
            self.__dialog.destroy()
            self.__observer.on_text_selected((tag_id, tag, position))
        
    def __on_cancel(self):
        self.__dialog.destroy()
        self.__observer.on_text_selected()
        
    
    def unregister_observer(self):
        '''
        '''
        del self.__observer   