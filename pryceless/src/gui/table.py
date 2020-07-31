'''
Created on 24.07.2020

@author: mthoma
'''
import tkinter as tk
from scripts import configuration_loader
from tkinter.constants import BUTT

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
        #self.header.grid(row=0, column=0, sticky=tk.NSEW, pady=2)
        self.header.pack(fill=tk.X)
        
        self.__define_columns(columns)
        
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
            button = self.header.grid_slaves(row=0,column=int(col_idx))[0]
            button.config(width=col_width)
            button.grid_propagate()
            button.update()
            print(button.winfo_width())
        
        
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
        
        for cell in table_row:
            cell_ui = None
            if cell['type'] == 'boolean':
                var = tk.IntVar()
                cell_ui = tk.Checkbutton(self.body, variable=var)
                cell_ui.val = var
                if cell['content'] == 'selected':
                    cell_ui.select()
            else:
                cell_ui = tk.Label(self.body, text=cell['content'], anchor=tk.W, justify=tk.LEFT, wraplength=500)
            
            cell_ui.grid(row=self.row_idx, column=col_idx, sticky=tk.NSEW, padx=TABLE_GRID_PAD,
                         pady=TABLE_GRID_PAD)
            
            cell_ui.update()
            
            cell_width = cell_ui.winfo_width()
            key = str(col_idx)
            
            if (not key in self.column_body_width) or (cell_width > self.column_body_width[key]):
                self.column_body_width[key] = cell_width
            
            col_idx += 1
            
        self.row_idx += 1
        
    def __create_body(self):
        
        self.canvas = tk.Canvas(self, borderwidth=1, background=TABLE_COLOR_GRID)
        
        self.body = tk.Frame(self.canvas, background=TABLE_COLOR_GRID)
        self.body.pack(fill=tk.BOTH, expand=1)
        
        self.vsb = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.canvas.create_window((4,4), window=self.body, anchor='nw', tags='self.body')

        self.body.bind('<Configure>', self.onFrameConfigure)
        
        
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
                
    def __define_columns(self, columns):
        
        column_idx = 0
        for column in columns:
            b = tk.Button(self.header,text=column, command=lambda column_idx=column_idx: self.on_column_select(column_idx))
            b.grid(row=0, column=column_idx, sticky=tk.NSEW, padx=TABLE_GRID_PAD, pady=TABLE_GRID_PAD)
            
            b.update()
            
            self.column_header_width[str(column_idx)] = b.winfo_width()
            
            column_idx += 1
            
    def on_column_select(self, column_idx):
        print(column_idx)

'''
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

root=Tk()
sizex = 800
sizey = 600
posx  = 100
posy  = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

myframe=Frame(root,relief=GROOVE,width=50,height=100,bd=1)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
data()
root.mainloop()



import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        Put in some fake data
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1",
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        Reset the scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    example = Example(root)
    example.pack(side="top", fill="both", expand=True)
    root.mainloop()


'''       
        
def request_tag_attr_popup(tag_name, master, respond_recipient):
    
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
    
    popup = tk.Toplevel(master)
    popup.wm_geometry("%dx%d" % (1000, 500))
    popup.transient(master)
    popup.title(popup.title() + ' - %s Attribute Selection' %(tag_name.upper()))
    popup.resizable(0, 0)
    table = Table(popup, ['X', 'Attribute Name', 'Attribute Description'], table_content)
        
    #table.add_row(table_row)
    
    #table.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, pady=2)
    table.pack(fill=tk.BOTH, expand=1)
        
    button_row = tk.Frame(popup)
    button_row.pack(fill=tk.X)
    
    select_btn = tk.Button(button_row,text='Select', command=lambda: respond_tag_attr_popup(popup, table, respond_recipient))
    select_btn.grid(row=1, column=0, sticky=tk.NSEW, pady=2, padx=2) 
    
    cancel_btn = tk.Button(button_row,text='Cancel', command=lambda: popup.destroy())
    cancel_btn.grid(row=1, column=1, sticky=tk.NSEW, pady=2, padx=2) 
    
    popup.mainloop()

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