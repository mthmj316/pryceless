'''
Created on 22.06.2020

@author: mthoma
'''
from string import Template

'''
    Replaces in the given template all occurrences of the
    variable with the given variable_name by given variable_value.
'''
def replace(code_template, variable_name, variable_value):
    return Template(template=code_template).substitute(variable_name=variable_value)
    