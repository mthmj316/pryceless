'''
Created on 04.08.2020

@author: mthoma
'''
import tkinter as tk
from typing import List
from overrides import overrides
from tkinter import scrolledtext, Listbox, Scrollbar
from interfaces.abs_tag_overview import ABSTagOverviewUI, TagOverviewObserver,\
    TagOverviewObservable
from utils.utils import Event

class TagOverviewUI(tk.Frame, ABSTagOverviewUI, TagOverviewObservable):
    '''
    classdocs
    '''
    __double_click_obervers: List[TagOverviewObserver] = []
    
    __click_observers: List[TagOverviewObserver] = []
    
    __event: Event = Event()
    
    __html_listbx: Listbox = None
    
    __list_index: int = 1
    
    __description_scdtxt: scrolledtext.ScrolledText = None
    
    def __init__(self, master):
        '''
        Constructor
        '''
        tk.Frame.__init__(self, master, background='#111AAA')
        self.configure(width=master.winfo_reqwidth(), height=master.winfo_reqheight())
        self.grid_propagate(False)
        
        self.grid()
        
        print(master.winfo_reqwidth())
        print(master.winfo_reqheight())
        print(master.winfo_width())
        print(master.winfo_height())
        print(self.winfo_reqwidth())
        print(self.winfo_reqheight())
        print(self.winfo_width())
        print(self.winfo_height())
        
        self.__create_html_list_box()   
        
        self.__description_scdtxt = scrolledtext.ScrolledText(self, undo=True, wrap=tk.WORD)
        #self.description.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=0)
        self.__description_scdtxt.grid(row=2, column=0)
    
        
    def __on_html_tag_selected(self, evt):
        
        if self.state == 'normal':
            index = evt.widget.curselection()[0]
            self.__event.event_source = evt.widget.get(index)
        
            self.on_click()
        
    def __on_html_tag_double_click(self, event):
        
        if self.state == 'normal':
            index = event.widget.curselection()[0]
            self.__event.event_source = event.widget.get(index)
            
            self.on_double_click()
    
    def __create_html_list_box(self) -> None:
        
        height=self.winfo_reqheight() / 2
    
        #self.__html_listbx = Listbox(self, width=self.winfo_reqwidth(), height= int(height))
        self.__html_listbx = Listbox(self)        
        #self.__html_listbx.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.__html_listbx.propagate(False)
        self.__html_listbx.configure(width=self.winfo_reqwidth(), height= int(height))
        #self.__html_listbx.pack()
        self.__html_listbx.bind('<<ListboxSelect>>', self.__on_html_tag_selected)
        self.__html_listbx.bind('<Double-Button>', self.__on_html_tag_double_click)
        
        #self.__html_listbx.update()
        print(self.__html_listbx.winfo_reqwidth())
        print(self.__html_listbx.winfo_reqheight())
        print(self.__html_listbx.winfo_width())
        print(self.__html_listbx.winfo_height())
        
        scrollbar = Scrollbar(self.__html_listbx, orient="vertical", width=self.winfo_reqwidth())
        scrollbar.config(command=self.__html_listbx.yview)
        #scrollbar.pack(side="right", fill="y")
    
        self.__html_listbx.config(yscrollcommand=scrollbar.set)
        

    @overrides
    def add_list_item(self, item:str)->None:
        '''
        '''
        self.__html_listbx.insert(self.__list_index, item)
        self.__list_index += 1
    
    @overrides    
    def enable(self, enable) -> None:
        
        self.state = 'normal' if enable else 'disable'
        
        self.html_overvew_lbx.config(state=self.state)
        self.__description_scdtxt.config(state=self.state)
        
    @overrides
    def set_description(self, description:str)->None:
        '''
        '''
        pass
        
    @overrides
    def register_double_click(self, observer:TagOverviewObserver)->None:
        '''
        '''
        self.__double_click_obervers.append(observer)
    
    
    @overrides
    def register_click(self, observer:TagOverviewObserver)->None:
        '''
        '''
        self.__click_observers.append(observer)
    
            
    @overrides
    def unregister_double_click(self, observer:TagOverviewObserver)->None:
        '''
        '''
        self.__double_click_obervers.remove(observer)
    
    
    @overrides
    def unregister_click(self, observer:TagOverviewObserver)->None:
        '''
        '''
        self.__click_observers.remove(observer)
        
    @overrides
    def on_click(self)->None:
        '''
        '''
        for observer in self.__click_observers:
            observer.on_click(self)
        
    @overrides
    def on_double_click(self)->None:
        '''
        '''
        for observer in self.__double_click_obervers:
            observer.on_double_click(self)
        