'''
Created on 24.07.2020

@author: mthoma
'''
import tkinter as tk

class Table(object):
    
    def __init__(self, master):
        self.table_ui = tk.Toplevel(master)

    def open(self):
        self.table_ui.mainloop()
        
    def add_row(self):
        pass
    
    def define_columns(self, columns):
        
        idx = 0
        for column in columns:
            b = tk.Button(self.table_ui,text=column, command=lambda column_idx=idx: self.on_column_select(column_idx))
            b.grid(row=0, column=idx, sticky=tk.W, pady=2)
            idx += 1
            
    def on_column_select(self, column_idx):
        print(column_idx)
    
    def set_title(self, title_suffix):
        new_title = self.table_ui.title()
        new_title += title_suffix
        self.table_ui.title(new_title)
        
        
def create_tag_attr_table(tag, master):
    table = Table(master)
    table.set_title(' - %s Attribute Selection' %(tag.upper()))
    table.define_columns(['Select', 'Attribute Name', 'Attribute Description'])
    table.open()
    
    
def create_html_tag_popup(self, tag):
    window = tk.Toplevel()

    label = tk.Label(window, text=tag)
    label.pack(fill='x', padx=50, pady=5)

    button_close = tk.Button(window, text="Cancel", command=window.destroy)
    button_close.pack(fill='x')