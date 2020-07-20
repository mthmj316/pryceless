'''
Created on 20.07.2020

@author: mthoma
'''
import os
import io



def load_conf_files(conf_file_name):
    
    path_to_templates = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../conf/' + conf_file_name)
    
    with open(path_to_templates, 'r') as file:
        return file.read()
    
def load_html_description():
    
    descriptions = load_conf_files('html_tag_description.conf')
    
    io_desc = io.StringIO(descriptions)
    
    html_desc = {}
    
    for line in io_desc:
        line_splitted = line.split('::')
        html_desc[line_splitted[0]] = line_splitted[1]
    
    return html_desc
        