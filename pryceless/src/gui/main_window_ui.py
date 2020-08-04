'''
Created on 13.07.2020

@author: mthoma
'''
import os
from pathlib import Path

from gui import list_creator, table
from gui.list_creator import create_html_list_box
import tkinter as tk
import tkinter.filedialog as file_dialog
import tkinter.scrolledtext as scrolledtext
import tkinter.messagebox as msg_box
from scripts import selenium_testcase_template
from gui.table import Table
#from utils.observable import Observable
#from utils.observer import Observer
from typing import List

'''
_____________________________________________________
|          |                              |         |
|          |                              |  Attr.  |
|   HTML   |                              |         |
|   Tag    |                              |         |
| Overview |     Page Config              |         |
|          |                              |---------|
|          |                              |         |
|          |                              |   CSS   |
|          |                              |         |
|----------|------------------------------|---------|
|          |               |              |         |
|          |               |              |         |
|    JS    |      Events   |    G-Var     |  Var    |
|          |               |              |         |
|__________|_______________|______________|_________|


'''
class MainWindowUI(tk.Frame):
    '''
    classdocs
    '''
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title('Pryceless')
        
        self.statusbar = Statusbar(self)
        
        self.menu = tk.Menu(self.master)        
        self.master.config(menu=self.menu)

        self.create_file_menu()
        
        self.last_selected_dir = Path().home()
        self.set_current_file()
        self.file_is_open = False
        
        #Create html tag overview
        self.tag_overview = TagOverview(self)
        self.tag_overview.pack(side=tk.LEFT, fill=tk.Y)
        self.tag_overview.enable(False)


    def create_file_menu(self):
        # create the file top menu item
        self.file = tk.Menu(self.menu)
        
        self.file.add_command(label="New", command=lambda: self.on_new())  
        self.file.add_command(label="Open", command=lambda: self.on_open())        
        
        self.file.add_separator()
        
        self.file.add_command(label="Generate", command=lambda: self.on_generate())
        self.file.entryconfig("Generate", state=tk.DISABLED)
        
        self.file.add_separator()
        
        self.file.add_command(label="Save", command=lambda: self.on_save())
        self.file.entryconfig("Save", state=tk.DISABLED)
        
        self.file.add_separator()
        
        # add exit sub menu item
        self.file.add_command(label="Exit", command=self.on_exit)

        #added "file" to our menu
        self.menu.add_cascade(label="File", menu=self.file)
            
    def on_exit(self):
        self.statusbar.set_status_text('exit')
        self.quit()
        
    def on_generate(self):
        pass

    def on_save(self):
        # Check if a file has been opened
        if not self.file_is_open:
            # no, there is no file open
            #    -> ask the user for the file name
            file_name =  file_dialog.asksaveasfilename(initialdir = self.last_selected_dir,
                                                       title = 'Select file',
                                                       filetypes = (('Text Files','*.txt'),)
                                                       )
            if file_name:
                # set last_selected_dir -> next file_dialog will use that as entry point
                self.last_selected_dir =  os.path.dirname(file_name)
                # set current_file
                self.set_current_file(file_name)
        
        
        # check if current_file is set
        if self.current_file != None:
            # now, the current_file is set -> save the file
            with open(self.current_file,'w') as file:
                file.write(self.main_input.get_input())
            
    def set_current_file(self, file_name=None):
        '''
        Sets the current_file attribute, file_is_opem and the status bar info about
        currently opened file.
        '''
        self.current_file = file_name
        self.statusbar.set_status_text(file_name)
        self.file_is_open = True if file_name != None else False
    
    def on_open(self): 
        # Check if there is already a file open
        if self.file_is_open:
            #ask user if really a new file shall be opened
            user_answer = msg_box.askyesno('Question', 'Do you really want to open a new file?')
            if user_answer:
                # User decided to open a new file
                # Ask if the old file shall be saved before closing it.
                user_answer = msg_box.askyesno('Question', 'Are there changes to be saved?')
                if user_answer:
                    # yes save it
                    self.on_save()
            else:
                # User decided not to open a new file.
                return
               
        # Open file selection dialog
        file_name = file_dialog.askopenfilename(initialdir = self.last_selected_dir,
                                                title = 'Select file',
                                                filetypes =(('txt files','*.txt'),))
        # check if file has been select or the process cancelled
        if file_name:
            # file_name is set:
            # set new working dir
            self.last_selected_dir = os.path.dirname(file_name)
            #set the current_file
            self.set_current_file(file_name)
            # prepare the input section
            self.prepare_main_input()
            # write the file content to the main_input section
            with open(file_name, 'r') as file:
                self.main_input.set_input(file.read())
        
    def on_new(self):
        # Check if there is already a file open or new unsaved file.
        if self.file_is_open or (hasattr(self, 'main_input') and len(self.main_input.get_input()) > 0):
            # User has to decide if there is a change to be saved.
            user_answer = msg_box.askyesno('Question', 'Are there changes to be saved?')
            if user_answer:
                # User has decided that changes have to changed.
                self.on_save()
                # since in the save function the current_file has been set
                # it needs to be set to None again
                self.set_current_file()
            
        # prepare the main_input for user input
        self.prepare_main_input()
    
    def prepare_main_input(self):
        if not hasattr(self, 'main_input'):
            #Create the main_input frame
            self.main_input = MainInput(self)
            #Enable menu entries; Generate and Save
            self.file.entryconfig("Generate", state=tk.NORMAL)
            self.file.entryconfig("Save", state=tk.NORMAL)
            self.tag_overview.enable(True)
        
        # Write the basic html template to the main input text
        self.main_input.set_input(selenium_testcase_template.get_template('basic_html_file.template').substitute())
