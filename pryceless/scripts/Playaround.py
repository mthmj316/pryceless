'''
Created on 19.06.2020

@author: mthoma
'''

import os, shutil

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
        Delete all files and directories in the python sandbox
    '''
    clean_sandbox()
    

def create_new_folder():
    new_folder = os.path.join(os.getcwd(), r'new_folder')
    
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        
    print('Folder %s has been created.' % new_folder)

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