'''
Created on 19.07.2020

@author: mthoma
'''
from tkinter import Listbox, Scrollbar

from scripts import configuration_loader


html_tag_dict = {}

def create_html_list_box(master):
    
    html_listbx = Listbox(master)
    
    scrollbar = Scrollbar(html_listbx, orient="vertical")
    scrollbar.config(command=html_listbx.yview)
    scrollbar.pack(side="right", fill="y")

    html_listbx.config(yscrollcommand=scrollbar.set)
    
    index = 1
    for tag in get_html_tags():
        html_listbx.insert(index, tag)
    
    return html_listbx
    
def get_tag_description(tag_name):
    return get_html_tags()[tag_name];   
    
def get_html_tags():
    
    if len(html_tag_dict) == 0:
        html_tag_dict.update(configuration_loader.load_html_description())
    

    return html_tag_dict
        