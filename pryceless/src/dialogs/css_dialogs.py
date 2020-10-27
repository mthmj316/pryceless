'''
Created on 08.09.2020

@author: mthoma
'''
from abc import ABC, abstractmethod

from tkinter import messagebox
import tkinter as tk
from utils.logger import log_enter_func, log_leave_func, log_msg, log_set_var,\
    log_error


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
        
        log_enter_func('CreateCssRuleSet', '__init__', {'observer':observer, 'master':master})
        
        self.__observer = observer
        self.__selector_type_var = tk.StringVar(master)
        self.__selector_type_var.set('Class Selector')
        
        self.__selector_var = tk.StringVar(master)
        self.__selector_sec_part_var = tk.StringVar(master)
        
        self.__css_dialog(master)
        
        log_leave_func('CreateCssRuleSet', '__init__')
        

    def __on_selector_type_selected(self, event):
        
        log_enter_func('CreateCssRuleSet', '__on_selector_type_selected', {'event':event})
        
        if self.__is_compound(event):
            
            log_msg('CreateCssRuleSet', '__on_selector_type_selected', 'second selector input visible')
                    
            self.__selector_part_2_lbl.grid(row=0,column=2, padx=0, sticky=tk.W)
            self.__selector_part_2_entry.grid(row=0,column=3, columnspan=1,sticky=tk.W, padx=0)
            
            if event == CreateCssRuleSet.__ELEMENT_CLASS_SELECTOR:
            
                log_msg('CreateCssRuleSet', '__on_selector_type_selected', 'selector compound separator="."')
            
                self.__selector_part_2_lbl.config(text='.')
            else:
            
                log_msg('CreateCssRuleSet', '__on_selector_type_selected', 'selector compound="#"')
                
                self.__selector_part_2_lbl.config(text='#')
            
        else:
            
            log_msg('CreateCssRuleSet', '__on_selector_type_selected', 'second selector input invisible')
            
            self.__selector_part_2_lbl.grid_forget()
            self.__selector_part_2_entry.grid_forget()
        
        log_leave_func('CreateCssRuleSet', '__on_selector_type_selected')
        
    def __is_compound(self, selector_type):
        
        log_enter_func('CreateCssRuleSet', '__is_compound', {'selector_type':selector_type})
        
        is_compound = False
        
        if selector_type in [CreateCssRuleSet.__ELEMENT_CLASS_SELECTOR, CreateCssRuleSet.__ELEMENT_ID_SELECTOR]:
        
            is_compound = True
        
        log_leave_func('CreateCssRuleSet', '__is_compound', is_compound)
        
        return is_compound
    
    def __on_ok(self):
        
        log_enter_func('CreateCssRuleSet', '__on_ok')
        
        selector_type = self.__selector_type_var.get()
        log_set_var('CreateCssRuleSet', '__on_ok', 'selector_type', selector_type)
        
        is_compound = self.__is_compound(selector_type)
        log_set_var('CreateCssRuleSet', '__on_ok', 'is_compound', is_compound)
        
        if not self.__check_user_input(is_compound):
            
            log_error('CreateCssRuleSet', '__on_ok', 'user input check failed')
            log_leave_func('CreateCssRuleSet', '__on_ok')
            
            return
        
        selector_element = self.__get_selector_element(selector_type)
        log_set_var('CreateCssRuleSet', '__on_ok', 'selector_element', selector_element)
        
        selector_specifier = self.__get_selector_specifier(selector_type, is_compound)
        log_set_var('CreateCssRuleSet', '__on_ok', 'selector_specifier', selector_specifier)
        
        self.__dialog.destroy()
        
        self.__observer.on_create_css_rule_set_closed((self.__SELECTOR_TYPE_MAP[selector_type], 
                                                       selector_element, 
                                                       selector_specifier, 
                                                       is_compound,
                                                       self.__SELECTOR_TYPE_SEP.get(selector_type)))
        
        log_leave_func('CreateCssRuleSet', '__on_ok')
    
    def __check_user_input(self, is_compound):
        
        log_enter_func('CreateCssRuleSet', '__check_user_input', {'is_compound':is_compound})
        
        user_input_ok = True
        
        if self.__selector_var.get() == '':
            
            log_error('CreateCssRuleSet', '__check_user_input', 'Selector not set!', None)
            
            messagebox.showerror('Input Error', 'Selector not set!')

            user_input_ok = False
        
        
        if is_compound and self.__selector_sec_part_var.get() == '':
            
            log_error('CreateCssRuleSet', '__check_user_input', 'Selector second part not set!', None)
            
            user_input_ok = False
            
        log_leave_func('CreateCssRuleSet', '__check_user_input', user_input_ok)
        
        return user_input_ok
            
        
    
    def __get_selector_specifier(self, selector_type, is_compound):
        
        log_enter_func('CreateCssRuleSet', '__get_selector_specifier', 
                       {'selector_type':selector_type, 'is_compound':is_compound})
        
        selector_specifier = None
        
        if not selector_type.startswith('Element'):
            selector_specifier = self.__selector_var.get()
        else:
            selector_specifier = self.__selector_sec_part_var.get() if is_compound else ''
        
        log_leave_func('CreateCssRuleSet', '__get_selector_specifier', selector_specifier)
        
        return selector_specifier
        
    
    def __get_selector_element(self, selector_type):
        
        log_enter_func('CreateCssRuleSet', '__get_selector_element', {'selector_type':selector_type})
        
        selector_element = None
        
        if not selector_type.startswith('Element'):
            selector_element = ''
        else:
            selector_element = self.__selector_var.get()
        
        log_leave_func('CreateCssRuleSet', '__get_selector_element', selector_element)
        
        return selector_element
        
        
        
    def __on_cancel(self):
        
        log_enter_func('CreateCssRuleSet', '__on_cancel')
        
        self.__dialog.destroy()
        self.__observer.on_create_css_rule_set_closed()
        
        log_leave_func('CreateCssRuleSet', '__on_cancel')
    
    
    def __css_dialog(self, master):
        '''
        '''
        
        log_enter_func('CreateCssRuleSet', '__css_dialog', {'master':master})
        
        self.__dialog = tk.Toplevel(master)
        self.__dialog.title('Create New CSS Rule Set')
        self.__top_frame = tk.Frame(self.__dialog)
        self.__top_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=10, pady=10)
            
        log_msg('CreateCssRuleSet', '__css_dialog', 'topLevel and main frame created')
        
        tk.Label(self.__top_frame, text='Selector Type:', anchor=tk.W).grid(row=0,column=0, padx=10, sticky=tk.W)
        tk.OptionMenu(self.__top_frame, self.__selector_type_var, 
                      *CreateCssRuleSet.__selectors,
                      command=self.__on_selector_type_selected).grid(row=0,column=1, columnspan=3,sticky=tk.EW, padx=10)
        
        log_msg('CreateCssRuleSet', '__css_dialog', 'selector type selection created')
        
        selector_frame = tk.Frame(self.__top_frame)
        selector_frame.grid(row=1,column=0, columnspan=2, padx=10, sticky=tk.W)
        
        tk.Label(selector_frame, text='Selector:', anchor=tk.W).grid(row=0,column=0, padx=10, sticky=tk.W)
        selector_entry = tk.Entry(selector_frame, textvariable=self.__selector_var)
        selector_entry.grid(row=0,column=1, columnspan=1,sticky=tk.W, padx=0)
    
        self.__selector_part_2_lbl = tk.Label(selector_frame, text='#', anchor=tk.W)
        self.__selector_part_2_entry = tk.Entry(selector_frame, textvariable=self.__selector_sec_part_var)
        
        log_msg('CreateCssRuleSet', '__css_dialog', 'selector input created')
        
        buttons_frame = tk.Frame(self.__dialog)
        buttons_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=20)
        
        tk.Button(buttons_frame, text='Ok', command=self.__on_ok).pack(side=tk.LEFT, padx=1)
        tk.Button(buttons_frame, text='Cancel', command=self.__on_cancel).pack(side=tk.LEFT, padx=1)
        
        log_leave_func('CreateCssRuleSet', '__css_dialog')
        
    ###################################################################
    ###################################################################
    ###################################################################
        