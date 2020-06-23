'''
Created on 22.06.2020

@author: mthoma
'''
from string import Template

ASSERT_EQUALS_TEMPLATE = '/home/mthoma/software-dev/code-generator/templates/assert-equals.template'
ASSERT_NOTNULL_TEMPLATE = '/home/mthoma/software-dev/code-generator/templates/assert-notnull.template'


'''
    Replaces in the assert-notnull.template template all occurrences of the variables:
    actual_value replaces actual.
'''
def create_assert_notnull(actual_value):
    _template = get_template(ASSERT_NOTNULL_TEMPLATE)
    return Template(_template).substitute(actual=actual_value)

'''
    Replaces in the assert-equals.template template all occurrences of the variables:
    expected_value replaces expected
    actual_value replaces actual
    and attribute_name replaces actual.
'''
def create_assert_equals(expected_value, actual_value, attribute_name):
    _template = get_template(ASSERT_EQUALS_TEMPLATE)    
    return Template(_template).substitute(expected=expected_value, \
                                          actual=actual_value, attribute=attribute_name)  

'''
    Returns the content of the template with the given name
        template_name: fully qualified name of the template
'''
def get_template(template_name):
    with open(template_name, 'r') as file:
        return file.read()
    