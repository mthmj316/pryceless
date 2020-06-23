'''
Created on 19.06.2020

@author: mthoma
'''

import os, shutil
from string import Template

PYTHON_SANDBOX_DIR = '/home/mthoma/python-sandbox'

def main():
    
    '''
        Change into the python-sandbox directory
    '''
    os.chdir(PYTHON_SANDBOX_DIR)
    
    '''
        Create dir=new_folder
    '''
    create_new_folder()
    
    '''
        Create a text file
    '''
    create_text_file()
    
    '''
        Read template file content and replace variable
    '''
    replace_var()  
    
    '''
        Delete all files and directories in the python sandbox
    '''
    clean_sandbox()
    
def replace_var():
    
    file_name = create_text_file_name()
   
    file_content = get_file_content(file_name)
    
    print('file_content before substitution: ' + file_content)
    
    file_content = Template(file_content).substitute(var__='Hello world!')
    
    print('file_content after substitution: ' + file_content)
    
def create_text_file_name():
    return os.path.join(PYTHON_SANDBOX_DIR, r'text-file.txt')

def get_file_content(file_name):
    
    with open(file_name, 'r') as file:
        return file.read()

def create_text_file():
    file_name = create_text_file_name()
    
    with open(file_name,'w') as file:
        file.write('This just a text $var__. file with one this var: $var__.') 
        
    print('Creating file %s' % file_name)

def create_new_folder():
    new_folder = os.path.join(os.getcwd(), r'new_folder')
    
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        
    print('Creating dir %s' % new_folder)

def clean_sandbox():
    for filename in os.listdir(PYTHON_SANDBOX_DIR):
        file_path = os.path.join(PYTHON_SANDBOX_DIR, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                print('Removing file: %s' % file_path)
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                print('Removing dir: %s' % file_path)
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
        

if __name__ == '__main__':
    main()