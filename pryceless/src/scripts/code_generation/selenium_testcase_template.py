'''
Created on 22.06.2020

@author: mthoma
'''
import os
from string import Template

ASSERT_EQUALS_TEMPLATE = '/home/mthoma/software-dev/code-generator/templates/assert-equals.template'

'''
    Replaces in the given template all occurrences of the
    variable with the given variable_name by given variable_value.
'''
def create_assert_equals(expected, actual, attribute):
    pass

'''
    Returns the content of the template with the given name
        template_name: fully qualified name of the template
'''
def get_template(template_name):
    with open(template_name, 'r') as file:
        return file.read()
    