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


class Statusbar(tk.Frame):
    '''
    classdocs
    '''
    def __init__(self, master):
        '''
        doc
        '''
        tk.Frame.__init__(self, master)
        
        self.opened_file_var = tk.StringVar()
        self.opened_file_lbl = tk.Label(self, bd=2, relief=tk.SUNKEN, anchor=tk.W,
                                      textvariable=self.opened_file_var,
                                      font=('arial',10,'normal'))
        
        self.opened_file_var.set('opened: ')       
        self.opened_file_lbl.grid(row=0, column=0)
        #self.opened_file_lbl.pack(fill=tk.X)
        
        self.variable=tk.StringVar()    
        
        self.label=tk.Label(self, bd=2, relief=tk.SUNKEN, anchor=tk.W,
                           textvariable=self.variable,
                           font=('arial',10,'normal'))
        
        self.variable.set('state')  
        self.label.grid(row=0, column=1)       
        #self.label.pack(fill=tk.X)
              
        self.pack(side=tk.BOTTOM, fill=tk.X)
        
    def set_status_text(self, text):
        '''
        Sets the 'opened:' part of the status bar
        if text == None the section will contain: opened: None
        otherwise: opened: <text>
        '''
        if text == None:
            text = 'None'
        
        self.opened_file_var.set('opened: ' + text)
        
class MainInput(tk.Frame):
    '''
    classdocs
    '''
    def __init__(self, master):
        '''
        doc
        '''
        tk.Frame.__init__(self, master)
        self.text_area = tk.Text(master=master)
        self.text_area.pack(fill=tk.BOTH, expand=1)
             
    def set_input(self, value):
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, value)  

            
    def get_input(self):
        return self.text_area.get('1.0', tk.END)

class TagOverview(tk.Frame):
    '''
    classdocs
    '''
    def on_html_tag_selected(self, evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        
        index = w.curselection()[0]
        value = w.get(index)
        self.description.config(state=tk.NORMAL)
        self.description.delete('1.0', tk.END)
        self.description.insert(tk.END, list_creator.get_tag_description(value))
        self.description.config(state=tk.DISABLED) 
    
    def on_html_tag_double_click(self, event):
        
        if self.state == 'normal':
            index = event.widget.curselection()[0]
            selected_tag = event.widget.get(index)
            
            table.create_tag_attr_table(selected_tag, self.master)
        
    def enable(self, enable):
        
        self.state = 'normal' if enable else 'disable'
        
        self.html_overvew_lbx.config(state=self.state)
        self.description.config(state=self.state)
        
    
    def __init__(self, master):
        '''
        doc
        '''
        tk.Frame.__init__(self, master)
        self.html_overvew_lbx = create_html_list_box(self)
        self.html_overvew_lbx.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.html_overvew_lbx.bind('<<ListboxSelect>>', self.on_html_tag_selected)
        self.html_overvew_lbx.bind('<Double-Button>', self.on_html_tag_double_click)
        
        #self.description = tk.Text(master=self, state=tk.DISABLED)
        self.description = scrolledtext.ScrolledText(self, undo=True, wrap=tk.WORD)
        self.description.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=0)
        

class MainWindow(tk.Frame):
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


if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.attributes('-zoomed', True)
    root.mainloop()