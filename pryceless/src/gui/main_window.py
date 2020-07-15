'''
Created on 13.07.2020

@author: mthoma
'''
import tkinter as tk
import tkinter.filedialog as file_dialog
import os
from pathlib import Path
from pip._internal import self_outdated_check
from more_itertools.more import side_effect
       
    
    
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
        self.opened_file_var.set('opened: ' + text)

        


        
class MainInput(tk.Frame):
    '''
    classdocs
    '''
    def __init__(self, master):
        '''
        doc
        '''
        self.text_area = tk.Text(master=master)
        self.text_area.pack(fill=tk.BOTH, expand=True)
             
    def set_input(self, value):
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, value)  

            
    def get_input(self):
        return self.text_area.get('1.0', tk.END)


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
        
        self.last_selected_dir = Path().home();
        self.file_is_open = False


    
    def create_file_menu(self):
        # create the file top menu item
        self.file = tk.Menu(self.menu)
        
        self.file.add_command(label="New", command=lambda: self.create_new())  
        self.file.add_command(label="Open", command=lambda: self.open())        
        
        self.file.add_separator()
        
        self.file.add_command(label="Generate", command=lambda: self.generate())
        self.file.entryconfig("Generate", state=tk.DISABLED)
        
        self.file.add_separator()
        
        self.file.add_command(label="Save", command=lambda: self.save())
        self.file.entryconfig("Save", state=tk.DISABLED)
        
        self.file.add_separator()
        
        # add exit sub menu item
        self.file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        self.menu.add_cascade(label="File", menu=self.file)
            

    def client_exit(self):
        self.statusbar.set_status_text('exit')
        self.quit()
        
    def generate(self):
        pass

    def save(self):
               
        if self.file_is_open != True:
            file_name =  file_dialog.asksaveasfilename(initialdir = self.last_selected_dir,title = 'Select file',filetypes = (('txt files','*.txt'), ('jpeg files','*.jpg'),('all files','*.*')))
        else:
            file_name = self.last_selected_dir
        
        if file_name:
            self.last_selected_dir =  os.path.dirname(file_name)
        
            with open(file_name,'w') as file:
                file.write(self.main_input.get_input()) 
        
    
    def open(self):        
        #  file_name = file_dialog.askopenfilename(initialdir = '/',title = 'Select file',filetypes = (('jpeg files','*.jpg'),('all files','*.*')))
        file_name = file_dialog.askopenfilename(initialdir = self.last_selected_dir,title = 'Select file',
                                                filetypes =(('txt files','*.txt'), ('jpeg files','*.jpg'),('all files','*.*')))
        
        if file_name:
            self.last_selected_dir = os.path.dirname(file_name)
            self.statusbar.set_status_text(file_name)
            with open(file_name, 'r') as file:
                self.main_input.set_input(file.read())
        
    
    def create_new(self):
        self.__create_main_input()
    
    def __create_main_input(self):
        if(hasattr(self, 'main_input')):
            self.main_input.set_input('')
        else:
            self.main_input = MainInput(self)
            
        self.file.entryconfig("Generate", state=tk.NORMAL)
        self.file.entryconfig("Save", state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.attributes('-zoomed', True)
    root.mainloop()