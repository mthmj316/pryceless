'''
Created on 24.07.2020

@author: mthoma
'''
import tkinter as tk
from scripts import configuration_loader
from tkinter.constants import BUTT
from pip._internal import self_outdated_check

TABLE_COLOR_BACK = "#D9D9D9"
TABLE_COLOR_GRID = "#000000"
TABLE_GRID_PAD = 1
class Table(tk.Frame):
    
    def __init__(self, master, columns, content):
        
        tk.Frame.__init__(self, master)
        self.row_idx = 0;
        
        self.column_header_width = {}
        self.column_body_width = {}
        self.column_width_to_apply = {}
              
        self.header = tk.Frame(self, background=TABLE_COLOR_BACK)
        self.header.pack(fill=tk.X)
        self.header_frames = []
        
        self.__create_header(columns)
        
        self.__create_body()
        
        for table_row in content:
            self.__add_row(table_row)
            
        self.__calulate_column_width_to_apply()
            
        print(self.column_header_width)
        print(self.column_body_width)
        print(self.column_width_to_apply)
        
        self.__revise_column_width()
        
    def __revise_column_width(self):
        
        # revise table header columns
        for col_idx, col_width in self.column_width_to_apply.items():
            
            print(col_idx + ' -> ' + str(col_width))
            
            btn_frame = self.header_frames[int(col_idx)]
            btn_frame.config(width=col_width)
            btn_frame.update()
            
            btn = btn_frame.winfo_children()[0]
            btn.update()
            
            print(btn.winfo_width())
            print(btn_frame.winfo_reqwidth())
        
        
        # revise table body
        
        
    def __calulate_column_width_to_apply(self):
        
        if len(self.column_header_width.keys()) > 0:
            
            for col_idx, col_width in self.column_header_width.items():
                
                max_col_width = col_width;
                
                if col_idx in self.column_width_to_apply and max_col_width < self.column_width_to_apply[col_idx]:
                    max_col_width = self.column_width_to_apply[col_idx]
                    
                if max_col_width < self.column_body_width[col_idx]:
                    max_col_width = self.column_body_width[col_idx]
                    
                self.column_width_to_apply[col_idx] = max_col_width                    
                
      
    def __add_row(self, table_row):
        
        col_idx = 0;
        
        row_frame = self.__create_row_frame()

        for cell in table_row:
            
            cell_frame = self.__create_cell_frame(row_frame)
            cell_ui = self.__create_cell(cell, cell_frame)
            
            cell_width = cell_ui.winfo_reqwidth()
            key = str(col_idx)
            
            if (not key in self.column_body_width) or (cell_width > self.column_body_width[key]):
                self.column_body_width[key] = cell_width
            
            col_idx += 1
            
        self.row_idx += 1
        
    def __create_row_frame(self):
        
        cell_row = tk.Frame(self.body, background='#625425', width=200, height=30)
        cell_row.grid(row=self.row_idx, column=0, sticky=tk.NSEW, padx=TABLE_GRID_PAD, pady=TABLE_GRID_PAD)            
        cell_row.grid_propagate(False)
        
        return cell_row
    
    def __create_cell_frame(self, row_frame):
            
        cell_frame = tk.Frame(row_frame, background='#625425', width=200, height=30)
        cell_frame.pack(fill=tk.BOTH, side=tk.LEFT, padx=TABLE_GRID_PAD, pady=TABLE_GRID_PAD)            
        cell_frame.propagate(False)
        
        return cell_frame
        
    def __create_cell(self, cell_def, cell_frame):
        
        if cell_def['type'] == 'boolean':
            var = tk.IntVar()
            cell_ui = tk.Checkbutton(cell_frame, variable=var)
            cell_ui.val = var
            if cell_def['content'] == 'selected':
                cell_ui.select()
        else:
            cell_ui = tk.Label(self.body, text=cell_def['content'], 
                               anchor=tk.W, justify=tk.LEFT, wraplength=500)
        
        cell_ui.pack(expand=1, fill=tk.BOTH, side=tk.LEFT, padx=TABLE_GRID_PAD, pady=TABLE_GRID_PAD)
        cell_ui.update()
            
        return cell_ui
            
            
        
    def __create_body(self):
        
        self.canvas = tk.Canvas(self, borderwidth=0, background=TABLE_COLOR_GRID)
        
        self.body = tk.Frame(self.canvas, background=TABLE_COLOR_GRID)
        self.body.pack(fill=tk.BOTH, expand=1, padx=TABLE_GRID_PAD, pady=TABLE_GRID_PAD)
        
        self.vsb = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.canvas.create_window((4,4), window=self.body, anchor='nw', tags='self.body')

        self.body.bind('<Configure>', self.onFrameConfigure)
        
        
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
                
    def __create_header(self, columns):
        
        column_idx = 0
        for column in columns:
            btn_frame = tk.Frame(self.header, background='#625425', width=200, height=30)
            btn_frame.pack(fill=tk.BOTH, side=tk.LEFT, padx=TABLE_GRID_PAD, pady=TABLE_GRID_PAD)            
            btn_frame.propagate(False)
            
            b = tk.Button(btn_frame,text=column, 
                          command=lambda column_idx=column_idx: self.on_column_select(column_idx))
            #b.grid(row=0, column=column_idx, sticky=tk.NSEW, padx=TABLE_GRID_PAD, pady=TABLE_GRID_PAD)
            b.pack(expand=1, fill=tk.BOTH, side=tk.LEFT)
            
            b.update()            
            b_width = b.winfo_reqwidth()
            b_heigth = b.winfo_reqheight()
            
            print(b_width)
            
            btn_frame.config(width=b_width, height=b_heigth)            
            btn_frame.update()
            
            self.column_header_width[str(column_idx)] = btn_frame.winfo_reqwidth()
            
            self.header_frames.append(btn_frame)
            
            column_idx += 1
            
    def on_column_select(self, column_idx):
        print(column_idx)   
        
def request_tag_attr_popup(tag_name, master, respond_recipient):
    
    table_content = create_attribute_popup_content(tag_name)
    
    popup = tk.Toplevel(master)
    popup.wm_geometry("%dx%d" % (1000, 500))
    popup.title(popup.title() + ' - %s Attribute Selection' %(tag_name.upper()))
    table = Table(popup, ['X', 'Attribute Name', 'Attribute Description'], table_content)
    table.pack(fill=tk.BOTH, expand=1)
        
    button_row = tk.Frame(popup)
    button_row.pack(fill=tk.X)
    
    select_btn = tk.Button(button_row,text='Select', command=lambda: respond_tag_attr_popup(popup, table, respond_recipient))
    select_btn.grid(row=1, column=0, sticky=tk.NSEW, pady=2, padx=2) 
    
    cancel_btn = tk.Button(button_row,text='Cancel', command=lambda: popup.destroy())
    cancel_btn.grid(row=1, column=1, sticky=tk.NSEW, pady=2, padx=2) 
    
    popup.mainloop()
    
def create_attribute_popup_content(tag_name):
    
    tag_conf = configuration_loader.load_html_tag(tag_name)
    
    attributes_events = []
    attributes_events += tag_conf['attributes']
    attributes_events += tag_conf['events']
    
    table_content = []
    
    for attribute in attributes_events:
        table_row = []
        
        attribute_def = configuration_loader.load_attribute(attribute)
        
        cell_select={
            'type':'boolean',
            'content':'None'
            }
        table_row.append(cell_select)
        
        cell_attr_name={
            'type': 'rText',
            'content': attribute_def['name']
            }
        table_row.append(cell_attr_name)
        
        cell_attr_desc = {
            'type': 'rText',
            'content': attribute_def['description']
            }
        table_row.append(cell_attr_desc)
        
        table_content.append(table_row)
        
    return table_content

def respond_tag_attr_popup(popup, table, respond_recipient):

    row = 0
    selected_attributes = []
    while row < table.body.grid_size()[1]:
        
        if table.body.grid_slaves(row,0)[0].val.get() == 1:
            
            selected_attribute = {
                'name': table.body.grid_slaves(row,1)[0]['text'],
                'description': table.body.grid_slaves(row,2)[0]['text']
                }
            selected_attributes.append(selected_attribute)
        
        row += 1
    
    popup.destroy()
    
    respond_recipient(selected_attributes)
    
def create_html_tag_popup(self, tag):
    '''
    window = tk.Toplevel()

    label = tk.Label(window, text=tag)
    label.pack(fill='x', padx=50, pady=5)

    button_close = tk.Button(window, text="Cancel", command=window.destroy)
    button_close.pack(fill='x')
    '''
    pass