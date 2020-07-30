'''
Created on 24.07.2020

@author: mthoma
'''
import tkinter as tk
from scripts import configuration_loader

class Table(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.row_idx = 0;
        
    def add_row(self, row_cells):
        
        col_idx = 0;
        for cell in row_cells:
            cell_ui = None
            if cell['type'] == 'boolean':
                var = tk.IntVar()
                cell_ui = tk.Checkbutton(self, variable=var)
                cell_ui.val = var
                if cell['content'] == 'selected':
                    cell_ui.select()
            else:
                cell_ui = tk.Label(self, text=cell['content'], anchor=tk.W)
            
            cell_ui.grid(row=self.row_idx, column=col_idx, sticky=tk.NSEW, pady=2)
            
            col_idx += 1
            
        self.row_idx += 1
                
    
    def define_columns(self, columns):
        
        idx = 0
        for column in columns:
            b = tk.Button(self,text=column, 
                          command=lambda column_idx=idx: self.on_column_select(column_idx))
            b.grid(row=self.row_idx, column=idx, sticky=tk.NSEW, pady=2)
            idx += 1
            
        self.row_idx += 1
            
    def on_column_select(self, column_idx):
        print(column_idx)
        
        
def request_tag_attr_popup(tag_name, master, respond_recipient):
    
    popup = tk.Toplevel(master)
    popup.transient(master)
    popup.title(popup.title() + ' - %s Attribute Selection' %(tag_name.upper()))
    popup.resizable(0, 0)
    table = Table(popup)
    table.define_columns(['Select', 'Attribute Name', 'Attribute Description'])
    
    tag_conf = configuration_loader.load_html_tag(tag_name)
    
    for attribute in tag_conf['attributes']:
        cells_def = []
        
        attribute_def = configuration_loader.load_attribute(attribute)
        
        cell_select={
            'type':'boolean',
            'content':'None'
            }
        cells_def.append(cell_select)
        
        cell_attr_name={
            'type': 'rText',
            'content': attribute_def['name']
            }
        cells_def.append(cell_attr_name)
        
        cell_attr_desc = {
            'type': 'rText',
            'content': attribute_def['description']
            }
        cells_def.append(cell_attr_desc)
        
        table.add_row(cells_def)
    
    table.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, pady=2)
    
    select_btn = tk.Button(popup,text='Select', command=lambda: respond_tag_attr_popup(popup, table, respond_recipient))
    select_btn.grid(row=1, column=0, sticky=tk.NSEW, pady=2) 
    
    
    cancel_btn = tk.Button(popup,text='Cancel', command=lambda: popup.destroy())
    cancel_btn.grid(row=1, column=1, sticky=tk.NSEW, pady=2) 
    
    popup.mainloop()

def respond_tag_attr_popup(popup, table, respond_recipient):

    row = 1
    while row < table.grid_size()[1]:
        
        val = table.grid_slaves(row,0)[0].val
        
        print(val.get())
        
        print(table.grid_slaves(row,1)[0]['text'])
        
        row += 1
    
    popup.destroy()
    
    respond_recipient('World!')
    
def create_html_tag_popup(self, tag):
    '''
    window = tk.Toplevel()

    label = tk.Label(window, text=tag)
    label.pack(fill='x', padx=50, pady=5)

    button_close = tk.Button(window, text="Cancel", command=window.destroy)
    button_close.pack(fill='x')
    '''
    pass