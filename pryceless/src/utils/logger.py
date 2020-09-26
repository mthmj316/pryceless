'''
Created on 25.09.2020

@author: mthoma
'''
from _datetime import datetime
def log_enter_func(source, function, parameters:dict):
    
    time_stamp = __create_timestamp()          
    parameter_str = __create_parameter_str(parameters)


def __create_

def __create_parameter_str(parameters:dict):
    
    parameter_str = ''
    key_value = ''
    #create key value string
    if not parameters == None:
        for key,value in dict.items():
            
            key_value = '='.join([key,value])
            
            if len(parameter_str) == 0:                
                parameter_str = key_value                
            else:                
                parameter_str = ','.join([parameter_str,key_value])
            
    
    return parameter_str
    
    
def __create_timestamp():
    
    now = datetime.now()
    
    return now