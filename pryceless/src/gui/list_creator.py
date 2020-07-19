'''
Created on 19.07.2020

@author: mthoma
'''
from tkinter import Listbox

html_tag_dict = {}

def create_html_list_box(master):
    
    html_listbx = Listbox(master)
    
    index = 1
    for tag in get_html_tags():
        html_listbx.insert(index, tag)
    
    return html_listbx
    
def get_tag_description(tag_name):
    return get_html_tags()[tag_name];   
    
def get_html_tags():
    
    if len(html_tag_dict) == 0:
        html_tag_dict['html'] = 'Root tag'
        html_tag_dict['head'] = 'Meta data tag'
        html_tag_dict['body'] = 'Page content tag'
        html_tag_dict['input'] = 'User input tag'
    

    return html_tag_dict
        