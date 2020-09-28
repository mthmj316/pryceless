'''
Created on 22.06.2020

@author: mthoma
'''

import os
from string import Template


ASSERT_EQUALS_TEMPLATE = 'assert-equals.template'
ASSERT_NOTNULL_TEMPLATE = 'assert-notnull.template'
ASSERT_NULL_TEMPLATE = 'assert-null.template'
ASSERT_THROWS_TEMPLATE = 'assert-throws.template'
TAG_UNDER_TEST_VAR_ASSIGNMENT_TEMPLATE = 'tag-under-test-var-assignment.template'
SELENIUM_BY_XPATH_TEMPLATE = 'selenium_by_xpath.template'
SELENIUM_BY_ID_TEMPLATE = 'selenium_by_id.template'
SELENIUM_FIND_ELEMENT_TEMPLATE = 'selenium_find_element.template'
SELENIUM_WEBELEMENT_DECLARATION_TEMPLATE = 'selenium_webelement_declaration.template'
UNIT_TEST_METHOD_TEMPLATE = 'unit_test_method.template'
UNIT_PARAMETERIZED_TEST_METHOD_TEMPLATE = 'unit_parameterized_test_method.template'
ANNOTATION_TEMPLATE = 'annotation.template'
SELENIUM_TES_CLASS__TEMPALTE = 'selenium_test_class.template'

CSV_SOURCE_PARAMETER = '"%s,%s"'

def create_selenium_unittest_class(http_address, test_cases):
    '''
    Creates a test class
    test_cases: the code of the test cases as string
    '''
    return get_template(SELENIUM_TES_CLASS__TEMPALTE).substitute(http_address=http_address, test_cases=test_cases)

def create_csvsource_annotation(parameter_dictionary):
    '''
    Creates a CsvSource annotation as follows.
    @CsvSource({"parameter_dictionary.key,parameter_dictionary.value" ...)
    example
    @CsvSource({"display,table","position,absolute","top,0px","left,0px"})
    ''' 
    if len(parameter_dictionary) == 0:
        return create_annotation('CsvSource', '')
    
    parameter_list = []
    
    for key,value in parameter_dictionary.items():
        parameter_list.append(CSV_SOURCE_PARAMETER %(key,value))
        
    return create_annotation('CsvSource', '{' + ','.join(parameter_list) + '}') 


def create_annotation(annotation_name, annotation_parameters):
    '''
    Creates an annotation
    '''
    return get_template(ANNOTATION_TEMPLATE).substitute(annotation_name=annotation_name,\
                                          annotation_parameters=annotation_parameters)


def create_method_parameter_list(parameter_dict):
    '''
    Creates by the means of the given parameter dictionary the parameters for a java method declaration.
    If the dictionary is empty an empty string will be returned.
    key -> parameter name
    value -> parameter type
    '''
    if len(parameter_dict) == 0:
        return ''
    
    parameter_list = []
    
    for key,value in parameter_dict.items():
        parameter_list.append(' '.join([value, key]))
        
        
    return ', '.join(parameter_list)  
    


def create_parameterized_unittest_method(variable_dict):
    '''
    Create parameterized test method.
    The variable_dict dictionary must contain the following key-value-pairs:
        parameter_sources     -> parameter source annotation(s)
        what_is_tested        -> part of the method name which depicts the test case
        parameters            -> list of the function parameters which
        test_method_content   -> content of the method
        
        @ParameterizedTest
        <parameter_sources>
        public void test<what_is_tested>(<parameters>){

            <test_method_content>
        }
    '''
    return get_template(UNIT_PARAMETERIZED_TEST_METHOD_TEMPLATE).substitute(variable_dict)


def create_unittest_method(what_is_tested, test_method_content):
    return get_template(UNIT_TEST_METHOD_TEMPLATE).substitute(what_is_tested=what_is_tested,\
                                          test_method_content=test_method_content)
    

'''
    Creates the following expression: WebElement var_name = var_assignment;
'''
def create_selenium_webelement_declaration(var_name, var_assignment):
    '''
    Creates junit method
    
    @Test
    public void testwhat_is_tested(){

        test_method_content
    }
    '''
    return get_template(SELENIUM_WEBELEMENT_DECLARATION_TEMPLATE).substitute(var_name=var_name,\
                                          var_assignment=var_assignment)


def create_selenium_find_element(tag_var_name, by_expression):
    '''
    Creates the following expression: tag_var_name.findElement(by_expression)
    '''
    return get_template(SELENIUM_FIND_ELEMENT_TEMPLATE).substitute(tag_var_name=tag_var_name,\
                                          by_expression=by_expression)


def create_selenium_by_id(identifier):
    '''
    Creates the following expression: By.id(id))
    '''
    return get_template(SELENIUM_BY_ID_TEMPLATE).substitute(identifier=identifier)


def create_selenium_by_xpath(xpath_expression):
    '''
    Creates the following expression: By.xpath(xpath_expression))
    '''
    return get_template(SELENIUM_BY_XPATH_TEMPLATE).substitute(xpath_expression=xpath_expression)


def create_assert_throws(expected_exception, executable):
    '''
    Creates the assertThrows method call: assertThrows(ExpectedException.class, executable);
    '''
    return get_template(ASSERT_THROWS_TEMPLATE).substitute(expected_exception=expected_exception,\
                                          executable=executable)


def create_tag_under_unittest_var_assignment(tag_id):
    '''
       Creates the code for the tag under test variable assignment:
       e.g: final WebElement tag = DRIVER.findElement(By.id("login_form"));
    '''
    return get_template(TAG_UNDER_TEST_VAR_ASSIGNMENT_TEMPLATE).substitute(tag_id=tag_id)


def create_assert_null(actual_value):
    '''
    Creates the assertNull method call: assertNull(null);
    '''
    return get_template(ASSERT_NULL_TEMPLATE).substitute(actual=actual_value)


def create_assert_notnull(actual_value):
    '''
    Replaces in the assert-notnull.template template all occurrences of the variables:
    actual_value replaces actual.
    '''
    return get_template(ASSERT_NOTNULL_TEMPLATE).substitute(actual=actual_value)


def create_assert_equals(expected_value, actual_value, attribute_name):
    '''
    Replaces in the assert-equals.template template all occurrences of the variables:
    expected_value replaces expected
    actual_value replaces actual
    and attribute_name replaces actual.
    '''
    return get_template(ASSERT_EQUALS_TEMPLATE).substitute(expected=expected_value, \
                                          actual=actual_value, attribute=attribute_name)  

  
def get_template(template_name):
    '''
    Returns the content of the template with the given name
        template_name: fully qualified name of the template

    '''
    path_to_templates = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates/' + template_name)
    
    with open(path_to_templates, 'r') as file:
        _template = file.read()
    return Template(_template)
