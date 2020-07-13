'''
Created on 13.07.2020

@author: mthoma
'''
import tkinter as tk

class MainWindow(tk.Frame):
    '''
    classdocs
    '''
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        # add other uis


if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()