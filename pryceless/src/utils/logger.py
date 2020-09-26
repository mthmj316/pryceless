'''
Created on 25.09.2020

@author: mthoma
'''
from _datetime import datetime


def log_setter(__source, name, value):
    
    time_stamp = __create_timestamp()
    source_function_str = __create_source_function_str(__source, name)
    
    return ' '.join(['DBG', time_stamp, 'SET', source_function_str, value])

def log_getter(__source, name, value):
    
    time_stamp = __create_timestamp()
    source_function_str = __create_source_function_str(__source, name)
    
    return ' '.join(['DBG', time_stamp, 'GET', source_function_str, value])

def log_enter_func(__source, __function, parameters:dict):
    
    time_stamp = __create_timestamp()          
    parameter_str = __create_parameter_str(parameters)
    source_function_str = __create_source_function_str(__source, __function)
    
    return ' '.join(['DBG', time_stamp, 'ENTER', source_function_str, parameter_str])

def __create_source_function_str(__source, __function):
    return '#'.join([__source,__function])

def __create_parameter_str(parameters:dict):
    
    parameter_str = ''
    key_value = ''
    #create key value string
    if not parameters == None:
        for key,value in dict.items():
            
            key_value = __create_key_value_str(key, value)
            
            if len(parameter_str) == 0:                
                parameter_str = key_value                
            else:                
                parameter_str = ','.join([parameter_str,key_value])
            
    
    return parameter_str
 
def __create_key_value_str(key, value):   
    return '='.join([key,value])
    
def __create_timestamp():
    
    now = datetime.now()
    
    return now