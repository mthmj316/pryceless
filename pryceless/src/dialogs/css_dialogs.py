'''
Created on 08.09.2020

@author: mthoma
'''
from abc import ABC, abstractmethod

from tkinter import messagebox
import tkinter as tk


class ABSCreateCssRuleSetObserver(ABC):
    
    @abstractmethod
    def on_create_css_rule_set_closed(self, result=None):
        '''
        '''

class CreateCssRuleSet(object):
    '''
    classdocs
    '''
    
    __CLASS_SELECTOR = 'Class Selector'
    
    __ID_SELECTOR = 'ID Selector'
    
    __ELEMENT_SELECTOR = 'Element Selector'
    
    __ELEMENT_CLASS_SELECTOR = 'Element Class Selector'
    
    __ELEMENT_ID_SELECTOR = 'Element ID Selector'
    
    __selectors = [__CLASS_SELECTOR, __ID_SELECTOR, __ELEMENT_SELECTOR, 
                   __ELEMENT_CLASS_SELECTOR, __ELEMENT_ID_SELECTOR]
    
    __SELECTOR_TYPE_MAP = {
        __CLASS_SELECTOR: 'class',
        __ID_SELECTOR: 'id',
        __ELEMENT_SELECTOR: 'element',
        __ELEMENT_CLASS_SELECTOR: 'element.class',
        __ELEMENT_ID_SELECTOR: 'element#id'
        }
    
    __SELECTOR_TYPE_SEP = {
        __CLASS_SELECTOR: '.',
        __ID_SELECTOR: '#',
        __ELEMENT_SELECTOR: '',
        __ELEMENT_CLASS_SELECTOR: '.',
        __ELEMENT_ID_SELECTOR: '#'
        }
    
    def __init__(self, observer:ABSCreateCssRuleSetObserver, master=None):
        '''
        Constructor
        '''
        
        print('CreateCssRuleSet.__init__    observer=' + str(observer) + 
              ' master' + str(master))
        
        self.__observer = observer
        self.__selector_type_var = tk.StringVar(master)
        self.__selector_type_var.set('Class Selector')
        
        self.__selector_var = tk.StringVar(master)
        self.__selector_sec_part_var = tk.StringVar(master)
        
        self.__css_dialog(master)
        

    def __on_selector_type_selected(self, event):
        
        print('CreateCssRuleSet.__on_selector_type_selected    event=' + str(event))
        
        if self.__is_compound(event):
            
            print('CreateCssRuleSet.__on_selector_type_selected    second selector input visible')
                    
            self.__selector_part_2_lbl.grid(row=0,column=2, padx=0, sticky=tk.W)
            self.__selector_part_2_entry.grid(row=0,column=3, columnspan=1,sticky=tk.W, padx=0)
            
            if event == CreateCssRuleSet.__ELEMENT_CLASS_SELECTOR:
                
                print('CreateCssRuleSet.__on_selector_type_selected    selector compound separator=.')
            
                self.__selector_part_2_lbl.config(text='.')
            else:
                
                print('CreateCssRuleSet.__on_selector_type_selected    selector compound=#')
                
                self.__selector_part_2_lbl.config(text='#')
            
        else:
            
            print('CreateCssRuleSet.__on_selector_type_selected    second selector input invisible')
            
            self.__selector_part_2_lbl.grid_forget()
            self.__selector_part_2_entry.grid_forget()
        
    def __is_compound(self, selector_type):
        
        if selector_type in [CreateCssRuleSet.__ELEMENT_CLASS_SELECTOR, CreateCssRuleSet.__ELEMENT_ID_SELECTOR]:
            return True
        else:
            return False
        
    
    def __on_ok(self):
        
        print('CreateCssRuleSet.__on_ok')
        
        selector_type = self.__selector_type_var.get()
        print('CreateCssRuleSet.__on_ok    selector_type=' + str(selector_type))
        
        is_compound = self.__is_compound(selector_type)
        print('CreateCssRuleSet.__on_ok    is_compound=' + str(is_compound))
        
        if not self.__check_user_input(is_compound):
            print('CreateCssRuleSet.__on_ok    user input check failed')
            return
            
        
        selector_element = self.__get_selector_element(selector_type)
        print('CreateCssRuleSet.__on_ok    selector_element=' + str(selector_element))
        
        selector_specifier = self.__get_selector_specifier(selector_type, is_compound)
        print('CreateCssRuleSet.__on_ok    selector_specifier=' + str(selector_specifier))
        
        self.__dialog.destroy()
        
        self.__observer.on_create_css_rule_set_closed((self.__SELECTOR_TYPE_MAP[selector_type], 
                                                       selector_element, 
                                                       selector_specifier, 
                                                       is_compound,
                                                       self.__SELECTOR_TYPE_SEP.get(selector_type)))
    
    def __check_user_input(self, is_compound):
        
        print('CreateCssRuleSet.__check_user_input    is_compound' + str(is_compound))
        
        if self.__selector_var.get() == '':
            
            messagebox.showerror('Input Error', 'Selector not set!')

            return False
        
        
        if is_compound and self.__selector_sec_part_var.get() == '':
            messagebox.showerror('Input Error', 'Selector second part not set!')
            return False
        
        return True
            
        
    
    def __get_selector_specifier(self, selector_type, is_compound):
        
        print('CreateCssRuleSet.__get_selector_specifier    selector_type' + str(selector_type) +
              ' is_compound=' + str(is_compound))
        
        if not selector_type.startswith('Element'):
            return self.__selector_var.get()
        else:
            return self.__selector_sec_part_var.get() if is_compound else ''
        
    
    def __get_selector_element(self, selector_type):
        
        print('CreateCssRuleSet.__get_selector_element    selector_type' + str(selector_type))
        
        if not selector_type.startswith('Element'):
            return ''
        else:
            return self.__selector_var.get()
        
        
        
    def __on_cancel(self):
        
        print('CreateCssRuleSet.__on_cancel')
        
        self.__dialog.destroy()
        self.__observer.on_create_css_rule_set_closed()
    
    
    def __css_dialog(self, master):
        '''
        '''
        
        print('CreateCssRuleSet.__css_dialog    master=' + str(master))
        
        self.__dialog = tk.Toplevel(master)
        self.__dialog.title('Create New CSS Rule Set')
        self.__top_frame = tk.Frame(self.__dialog)
        self.__top_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=10, pady=10)
        
        print('CreateCssRuleSet.__css_dialog    topLevel and main frame created')

        tk.Label(self.__top_frame, text='Selector Type:', anchor=tk.W).grid(row=0,column=0, padx=10, sticky=tk.W)
        tk.OptionMenu(self.__top_frame, self.__selector_type_var, 
                      *CreateCssRuleSet.__selectors,
                      command=self.__on_selector_type_selected).grid(row=0,column=1, columnspan=3,sticky=tk.EW, padx=10)
        
        
        print('CreateCssRuleSet.__css_dialog    selector type selection created')
        
        selector_frame = tk.Frame(self.__top_frame)
        selector_frame.grid(row=1,column=0, columnspan=2, padx=10, sticky=tk.W)
        
        tk.Label(selector_frame, text='Selector:', anchor=tk.W).grid(row=0,column=0, padx=10, sticky=tk.W)
        selector_entry = tk.Entry(selector_frame, textvariable=self.__selector_var)
        selector_entry.grid(row=0,column=1, columnspan=1,sticky=tk.W, padx=0)
    
        self.__selector_part_2_lbl = tk.Label(selector_frame, text='#', anchor=tk.W)
        self.__selector_part_2_entry = tk.Entry(selector_frame, textvariable=self.__selector_sec_part_var)
        
        print('CreateCssRuleSet.__css_dialog    selector input created')
        
        buttons_frame = tk.Frame(self.__dialog)
        buttons_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=20)
        
        tk.Button(buttons_frame, text='Ok', command=self.__on_ok).pack(side=tk.LEFT, padx=1)
        tk.Button(buttons_frame, text='Cancel', command=self.__on_cancel).pack(side=tk.LEFT, padx=1)
        
        print('CreateCssRuleSet.__css_dialog    button row created')
        