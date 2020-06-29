'''
Created on 22.06.2020

@author: mthoma
'''
from string import Template

ASSERT_EQUALS_TEMPLATE = '../../templates/assert-equals.template'
ASSERT_NOTNULL_TEMPLATE = '../../templates/assert-notnull.template'
ASSERT_NULL_TEMPLATE = '../../templates/assert-null.template'
ASSERT_THROWS_TEMPLATE = '../../templates/assert-throws.template'
TAG_UNDER_TEST_VAR_ASSIGNMENT_TEMPLATE = '../../templates/tag-under-test-var-assignment.template'
SELENIUM_BY_XPATH_TEMPLATE = '../../templates/selenium_by_xpath.template'
SELENIUM_BY_ID_TEMPLATE = '../../templates/selenium_by_id.template'
SELENIUM_FIND_ELEMENT_TEMPLATE = '../../templates/selenium_find_element.template'
SELENIUM_WEBELEMENT_DECLARATION_TEMPLATE = '../../templates/selenium_webelement_declaration.template'
UNIT_TEST_METHOD_TEMPLATE = '../../templates/unit_test_method.template'
UNIT_PARAMETERIZED_TEST_METHOD_TEMPLATE = '../../templates/unit_parameterized_test_method.template'
ANNOTATION_TEMPLATE = '../../templates/annotation.template'

CSV_SOURCE_PARAMETER = '"%s,%s"'

'''
    Creates a CsvSource annotation as follows.
    @CsvSource({"parameter_dictionary.key,parameter_dictionary.value" ...)
    example
    @CsvSource({"display,table","position,absolute","top,0px","left,0px"})
'''
def create_csvsource_annotation(parameter_dictionary):
    if len(parameter_dictionary) == 0:
        return create_annotation('CsvSource', '')
    
    parameter_list = []
    
    for key,value in parameter_dictionary.items():
        parameter_list.append(CSV_SOURCE_PARAMETER %(key,value))
        
    return create_annotation('CsvSource', ','.join(parameter_list)) 

'''
    Creates an annotation
'''
def create_annotation(annotation_name, annotation_parameters):
    _template = get_template(ANNOTATION_TEMPLATE)
    return Template(_template).substitute(annotation_name=annotation_name,\
                                          annotation_parameters=annotation_parameters)

'''
    Creates by the means of the given parameter dictionary the parameters for a java method declaration.
    If the dictionary is empty an empty string will be returned.
    key -> parameter name
    value -> parameter type
'''
def create_method_parameter_list(parameter_dict):
    if len(parameter_dict) == 0:
        return ''
    
    parameter_list = []
    
    for key,value in parameter_dict.items():
        parameter_list.append(' '.join([value, key]))
        
        
    return ', '.join(parameter_list)  
    

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
def create_parameterized_test_method(variable_dict):
    _template = get_template(UNIT_PARAMETERIZED_TEST_METHOD_TEMPLATE)
    return Template(_template).substitute(variable_dict)

'''
    Creates junit method
    
    @Test
    public void testwhat_is_tested(){

        test_method_content
    }
'''
def create_unit_test_method(what_is_tested, test_method_content):
    _template = get_template(UNIT_TEST_METHOD_TEMPLATE)
    return Template(_template).substitute(what_is_tested=what_is_tested,\
                                          test_method_content=test_method_content)
    

'''
    Creates the following expression: WebElement var_name = var_assignment;
'''
def create_selenium_webelement_declaration(var_name, var_assignment):
    _template = get_template(SELENIUM_WEBELEMENT_DECLARATION_TEMPLATE)
    return Template(_template).substitute(var_name=var_name,\
                                          var_assignment=var_assignment)

'''
    Creates the following expression: tag_var_name.findElement(by_expression)
'''
def create_selenium_find_element(tag_var_name, by_expression):
    _template = get_template(SELENIUM_FIND_ELEMENT_TEMPLATE)
    return Template(_template).substitute(tag_var_name=tag_var_name,\
                                          by_expression=by_expression)

'''
    Creates the following expression: By.id(id))
'''
def create_selenium_by_id(identifier):
    _template = get_template(SELENIUM_BY_ID_TEMPLATE)
    return Template(_template).substitute(identifier=identifier)

'''
    Creates the following expression: By.xpath(xpath_expression))
'''
def create_selenium_by_xpath(xpath_expression):
    _template = get_template(SELENIUM_BY_XPATH_TEMPLATE)
    return Template(_template).substitute(xpath_expression=xpath_expression)

'''
    Creates the assertThrows method call: assertThrows(ExpectedException.class, executable);
'''
def create_assert_throws(expected_exception, executable):
    _template = get_template(ASSERT_THROWS_TEMPLATE)
    return Template(_template).substitute(expected_exception=expected_exception,\
                                          executable=executable)

'''
   Creates the code for the tag under test variable assignment:
   e.g: final WebElement tag = DRIVER.findElement(By.id("login_form"));
'''
def create_tag_under_test_var_assignment(tag_id):
    _template = get_template(TAG_UNDER_TEST_VAR_ASSIGNMENT_TEMPLATE)
    return Template(_template).substitute(tag_id=tag_id)

'''
    Creates the assertNull method call: assertNull(null);
'''
def create_assert_null(actual_value):
    _template = get_template(ASSERT_NULL_TEMPLATE)
    return Template(_template).substitute(actual=actual_value)

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
    
