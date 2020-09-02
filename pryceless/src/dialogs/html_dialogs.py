'''
Created on 31.08.2020

@author: mthoma
'''
import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox

class ABSHTMLDialogObserver(ABC):
    
    @abstractmethod
    def on_create_tag_closed(self, result=None):
        '''
        '''
class CreateTagDialog():
    '''
    '''
    __observer: ABSHTMLDialogObserver = None
     
    __dialog: tk.Toplevel = None
    
    __id_var: tk.StringVar = None
    
    __tag_var: tk.StringVar = None
    
    __position_var: tk.StringVar = None
    
    def __init__(self, observer:ABSHTMLDialogObserver, master=None):
         
        self.__observer = observer
        
        self.__id_var = tk.StringVar()
        self.__tag_var = tk.StringVar()
        self.__position_var = tk.StringVar()

        self.__tag_dialog(master)

    def __tag_dialog(self, master):
        '''
        '''
        self.__dialog = tk.Toplevel(master)
        self.__dialog.title('Create New Tag')
        
        top_frame = tk.Frame(self.__dialog)
        top_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=10, pady=10)
        
        tk.Label(top_frame, text='ID:', anchor=tk.W).grid(row=0,column=0, padx=10, sticky=tk.W)
        id_entry = tk.Entry(top_frame, textvariable=self.__id_var)
        id_entry.grid(row=0,column=1, columnspan=1,sticky=tk.W, padx=10)
    
        tk.Label(top_frame, text='Tag:', anchor=tk.W).grid(row=1,column=0, padx=10, sticky=tk.W)
        tag_entry = tk.Entry(top_frame, textvariable=self.__tag_var)
        tag_entry.grid(row=1,column=1, columnspan=1,sticky=tk.W, padx=10)
        
        tk.Label(top_frame, text='Position:', anchor=tk.W).grid(row=2,column=0, padx=10, sticky=tk.W)
        position_entry = tk.Entry(top_frame, textvariable=self.__position_var)
        position_entry.grid(row=2,column=1, columnspan=1,sticky=tk.W, padx=10)
        
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
            self.__observer.on_create_tag_closed((tag_id, tag, position))
        
    def __on_cancel(self):
        self.__dialog.destroy()
        self.__observer.on_dialog_closed()
        
    
    def unregister_observer(self):
        '''
        '''
        del self.__observer