'''
Created on 13.07.2020

@author: mthoma
'''
import tkinter as tk

class Navbar(tk.Frame):
    '''
    classdocs
    '''
    def __init__(self, parent, *args, **kwargs):
        '''
        doc
        '''
        pass
        
        
class Toolbar(tk.Frame):
    '''
    classdocs
    '''
    def __init__(self, master):
        '''
        doc
        '''
        tk.Frame.__init__(self, master)        
        # creating a menu instance
        
        self.master = master        
        
    
    
class Statusbar(tk.Frame):
    '''
    classdocs
    '''
    def __init__(self, master):
        '''
        doc
        '''
        tk.Frame.__init__(self, master)
        self.variable=tk.StringVar()        
        self.label=tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W,
                           textvariable=self.variable,
                           font=('arial',16,'normal'))
        self.variable.set('Status Bar')
        self.label.pack(fill=tk.X)        
        self.pack(side=tk.BOTTOM, fill=tk.X)


        
class Main(tk.Frame):
    '''
    classdocs
    '''
    def __init__(self, parent, *args, **kwargs):
        '''
        doc
        '''
        pass


class MainWindow(tk.Frame):
    '''
    classdocs
    '''
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title('Pryceless')

        
        self.statusbar = Statusbar(self)
        self.toolbar = Toolbar(self)
        
        self.menu = tk.Menu(self.master)        
        self.master.config(menu=self.menu)

        # create the file object)
        file = tk.Menu(self.menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        self.menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = tk.Menu(self.menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        self.menu.add_cascade(label="Edit", menu=edit)
        '''
        self.toolbar = Toolbar(self, parent, *args, **kwargs)
        self.navbar = Navbar(self, parent, *args, **kwargs)
        self.main = Main(self, parent, *args, **kwargs)
       

        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)
        '''
        


if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.attributes('-zoomed', True)
    root.mainloop()