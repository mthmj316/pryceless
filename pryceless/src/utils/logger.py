'''
Created on 25.09.2020

@author: mthoma
'''
from _datetime import datetime

def log_error(__source, __function, msg:str='', e:Exception=None):
    
    time_stamp = __create_timestamp()
    source_function_str = __create_source_function_str(__source, __function)
    
    print(' '.join(['ERR', time_stamp, source_function_str, msg, str(e)]))

def log_msg(__source, __function, msg:str=''):
    
    time_stamp = __create_timestamp()
    source_function_str = __create_source_function_str(__source, __function)
    
    print(' '.join(['DBG', time_stamp, source_function_str, msg]))

def log_set_var(__source, __function, name, value):
    
    time_stamp = __create_timestamp()
    source_function_str = __create_source_function_str(__source, name)
    
    print(' '.join(['DBG', time_stamp, 'SET VAR', source_function_str, create_key_value_str(name, value)]))

def log_delete(__source, name):
    
    time_stamp = __create_timestamp()
    source_function_str = __create_source_function_str(__source, name)
    
    print(' '.join(['DBG', time_stamp, 'DEL', source_function_str]))

def log_setter(__source, name, value):
    
    time_stamp = __create_timestamp()
    source_function_str = __create_source_function_str(__source, name)
    
    print(' '.join(['DBG', time_stamp, 'SET', source_function_str, str(value)]))

def log_getter(__source, name, value):
    
    time_stamp = __create_timestamp()
    source_function_str = __create_source_function_str(__source, name)
    
    print(' '.join(['DBG', time_stamp, 'GET', source_function_str, str(value)]))

def log_leave_func(__source, __function, value):
    
    time_stamp = __create_timestamp()
    source_function_str = __create_source_function_str(__source, __function)
    
    print(' '.join(['DBG', time_stamp, 'LEAVE', source_function_str, value]))

def log_enter_func(__source, __function, parameters:dict):
    
    time_stamp = __create_timestamp()          
    parameter_str = __create_parameter_str(parameters)
    source_function_str = __create_source_function_str(__source, __function)
    
    print(' '.join(['DBG', time_stamp, 'ENTER', source_function_str, parameter_str]))

def __create_source_function_str(__source, __function):
    return '#'.join([__source,__function])

def __create_parameter_str(parameters:dict):
    
    parameter_str = ''
    key_value = ''
    #create key value string
    if not parameters == None:
        for key,value in dict.items():
            
            key_value = create_key_value_str(key, value)
            
            if len(parameter_str) == 0:                
                parameter_str = key_value                
            else:                
                parameter_str = ','.join([parameter_str,key_value])
            
    
    return parameter_str
 
def create_key_value_str(key, value):   
    return '='.join([key,str(value)])
    
def __create_timestamp():
    
    now = datetime.now()
    
    return now