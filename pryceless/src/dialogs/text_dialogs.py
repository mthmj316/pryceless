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

    def __init__(self, text_elements, observer:ABSTextDialogObserver, master=None):
        '''
        Constructor
        '''
        self.__text_elements = text_elements
        self.__observer = observer
        
        self.__selected_txt_coll_var = tk.StringVar()
        self.__selected_txt_item_var = tk.StringVar()
        
        print(text_elements)
        
        self.__text_collections = []
        for _tuple in self.__text_elements:
            if not _tuple[0] in self.__text_collections:
                self.__text_collections.append(_tuple[0])
                
        print(self.__text_collections)
        
        self.__text_items = ['test']
        self.__text_select_dialog(master)
    
    
    def __text_select_dialog(self, master):
        '''
        '''
        
        self.__dialog = tk.Toplevel(master)
        self.__dialog.title('Select Text')
        
        top_frame = tk.Frame(self.__dialog)
        top_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=10, pady=10)
        
    
        tk.Label(top_frame, text='Text Collections:', anchor=tk.W).grid(row=0,column=0, padx=10, sticky=tk.W)
        text_collection_opm = tk.OptionMenu(top_frame, self.__selected_txt_coll_var, 
                                            *self.__text_collections, 
                                            command=self.__on_collection_select)
        text_collection_opm.grid(row=0,column=1, columnspan=1,sticky=tk.W, padx=10)
        
        tk.Label(top_frame, text='Text Items:', anchor=tk.W).grid(row=1,column=0, padx=10, sticky=tk.W)
        self.__text_items_opm = tk.OptionMenu(top_frame, self.__selected_txt_item_var, 
                                              *self.__text_items)
        self.__text_items_opm.grid(row=1,column=1, columnspan=1,sticky=tk.W, padx=10)
        
        if len(self.__text_collections) == 1:
            text_collection_opm.set(self.__text_collections[0])
        
        buttons_frame = tk.Frame(self.__dialog)
        buttons_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=20)
        
        tk.Button(buttons_frame, text='Ok', command=self.__on_ok).pack(side=tk.LEFT, padx=1)
        tk.Button(buttons_frame, text='Cancel', command=self.__on_cancel).pack(side=tk.LEFT, padx=1)
        
    
    def __on_ok(self):
        
        selected_collection = self.__selected_txt_coll_var.get()
        selected_text_item = self.__selected_txt_item_var.get()

        if selected_text_item == '':
            messagebox.showerror('Input Error', 'Please select the text item!')
        else:
            self.__dialog.destroy()
            self.__observer.on_text_selected((selected_collection, selected_text_item))
        
    def __on_cancel(self):
        self.__dialog.destroy()
        self.__observer.on_text_selected()
        
    
    def unregister_observer(self):
        '''
        '''
        del self.__observer   

    def __on_collection_select(self, event):
        '''
        '''
        self.__selected_txt_item_var.set('')
        selected_collection = self.__selected_txt_coll_var.get()
        self.__text_items_opm['menu'].delete(0, 'end')
        
        for _tuple in self.__text_elements:
            if _tuple[0] == selected_collection:
                self.__text_items_opm['menu'].add_command(label=_tuple[1], 
                                                          command=tk._setit(self.__selected_txt_item_var, _tuple[1]))
                
                
                