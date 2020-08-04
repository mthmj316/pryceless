'''
Created on 04.08.2020

@author: mthoma
'''
import tkinter as tk
from gui.main_window_ui import MainWindowUI

if __name__ == '__main__':
    root = tk.Tk()
    MainWindowUI(root).pack(side="top", fill="both", expand=True)
    root.attributes('-zoomed', True)
    root.mainloop()