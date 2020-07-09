'''
Created on 25.06.2020

The following test case can be created by this script:
    - test tag name
    - test parent tag
    - test attributes of a tag
    - test css ruleset of a tag

@author: mthoma
'''

from scripts.selenium_testcase_template import create_tag_under_unittest_var_assignment,\
    create_unittest_method, create_assert_equals,\
    create_selenium_webelement_declaration, create_selenium_find_element,\
    create_selenium_by_xpath, create_assert_throws,\
    create_parameterized_unittest_method, create_csvsource_annotation
from scripts.generator_constants import SIBLING_CSV_SOURCE_ANNOTATION,\
    SELENIUM_GET_ATTRIBUTE, NO_SUCH_ELEMENT_EXCEPTION_CLASS,\
    JAVA_DOC_TEST_PARENT, JAVA_DOC_TEST_TAG_NAME, JAVA_DOC_TEST_SIBLINGS,\
    JAVA_DOC_TEST_ATTRIBUTES, SELENIUM_GET_VARIABLE_ATTRIBUTE,\
    JUNIT_ASSERT_EQUALS, SELENIUM_GET_CSS_VALUE, JAVA_DOC_TEST_CSS_RULES,\
    JAVA_DOC_TEST_ATTRIBUTES_NO_VALUE, JUNIT_ASSERT_NOT_NULL


def create_unittest_css_rule(tag_id, css_rule_directory):
    '''
        Creates a parameterized css rule unit test method
    '''
    
    if len(css_rule_directory) == 0:
        return ''
    
    code = []
    code.append(create_tag_under_unittest_var_assignment(tag_id))
    code.append(JUNIT_ASSERT_EQUALS %('expectedValue',\
                                      SELENIUM_GET_CSS_VALUE %('tag', 'cssRuleName'),\
                                      '"wrong " + cssRuleName'))
    
    variable_dict = {'parameter_sources':create_csvsource_annotation(css_rule_directory),
                     'what_is_tested': convert_tag_id_to_name_in_method(tag_id) + 'CssRule',
                     'parameters': 'final String cssRuleName, final String expectedValue',
                     'test_method_content': '\n\t'.join(code)}
    
    method = []
    method.append(JAVA_DOC_TEST_CSS_RULES %(tag_id))
    method.append(create_parameterized_unittest_method(variable_dict))
    
    return '\n'.join(method)


def create_unittest_attribute(tag_id, attribute_directory):
    '''
    Case 1. attribute_directory contains no attribute without value:
        see create_unittest_attribute(tag_id, attribute_directory)
    Case 2. attribute_directory contains an attribute without value:
        the generated test method contains an if clause which checks
        if the value is set.
         Value is set: assertEqual will be executed
         Value is not set: assertNotNull will be executed
    Case 3. attribute_directory is empty an empty string will be returned
    '''
    
    # check if at least one attribute in attribute_directory without value.
    # Such an attribute could be required    
    for value in attribute_directory.values():
        if value == '':
            return __create_unittest_attribute_assert_eq_nn(tag_id, attribute_directory)
    
    return __create_unittest_attribute_asset_no_nn(tag_id, attribute_directory)
        
def __create_unittest_attribute_assert_eq_nn(tag_id, attribute_directory):
    '''
    Creates attribute unit test method with assertEqual and assertNotNull
    '''
            
    code = []
    code.append(create_tag_under_unittest_var_assignment(tag_id))
    
    get_tag_attribute =  SELENIUM_GET_VARIABLE_ATTRIBUTE %('tag', 'attributeName')
    
    code.append('if(expectedValue != null) {')
    code.append(JUNIT_ASSERT_EQUALS %('expectedValue', get_tag_attribute, \
                                      '"wrong " + attributeName'))
    code.append('} else {')
    code.append(JUNIT_ASSERT_NOT_NULL % (get_tag_attribute))
    code.append('}')
    
    return __generate_unittest_attribute_code(tag_id, attribute_directory, \
                                              code, JAVA_DOC_TEST_ATTRIBUTES_NO_VALUE)

def __create_unittest_attribute_asset_no_nn(tag_id, attribute_directory):
    '''
        Creates a parameterized attribute unit test method withou assertNotNull
    '''
    
    if len(attribute_directory) == 0:
        return ''
    
    code = []
    code.append(create_tag_under_unittest_var_assignment(tag_id))
    code.append(JUNIT_ASSERT_EQUALS %('expectedValue',\
                                      SELENIUM_GET_VARIABLE_ATTRIBUTE %('tag', 'attributeName'),\
                                      '"wrong " + attributeName'))
    
    return __generate_unittest_attribute_code(tag_id, attribute_directory, code, JAVA_DOC_TEST_ATTRIBUTES)
    


def __generate_unittest_attribute_code(tag_id, attribute_directory, code, java_doc):
    '''
    Generates the code for the attribute unit test.
    '''
    variable_dict = {'parameter_sources':create_csvsource_annotation(attribute_directory),
                     'what_is_tested': convert_tag_id_to_name_in_method(tag_id) + 'Attributes',
                     'parameters': 'final String attributeName, final String expectedValue',
                     'test_method_content': '\n\t'.join(code)}
    
    method = []
    method.append(java_doc %(tag_id))
    method.append(create_parameterized_unittest_method(variable_dict))
    
    return '\n'.join(method)


def create_unittest_siblings(tag_id, predecessor_id, successor_id):
    '''
    Creates the test methods for testing the siblings of the html tag with id==tag_id
    If both predecessor_id and  successor_id is set then one unit test method will be created 
    tag_id -> html id of the tag for which the siblings are tested
    predecessor_id  -> id of the tag which must be directly before the tag under test
                    -> if none then the test will be 
    '''
    code = []
    code.append(create_tag_under_unittest_var_assignment(tag_id))
    code.append('if(expectedSiblingId == null) {')
    code.append(__create_unittest_no_sibling_assertion())
    code.append('} else {')
    code.append(__create_unittest_sibling())
    code.append('}')
    
    variable_dict = {'parameter_sources': __create_unittest_sibling_csv_source(predecessor_id, successor_id),
                     'what_is_tested': convert_tag_id_to_name_in_method(tag_id) + 'Sibling',
                     'parameters': 'final String expectedSiblingId, final String xpath',
                     'test_method_content': '\n\t'.join(code)}
    
    method = []
    method.append(JAVA_DOC_TEST_SIBLINGS %(tag_id, predecessor_id, successor_id))
    method.append(create_parameterized_unittest_method(variable_dict))
    
    return '\n'.join(method)

def __create_unittest_sibling_csv_source(predecessor_id, successor_id):
    return SIBLING_CSV_SOURCE_ANNOTATION %(predecessor_id, successor_id)


def __create_unittest_sibling():
    '''
    Creates the test for when a sibling is expected.
    example:
        final WebElement sibling = tag.findElement(By.xpath(xpath));
        assertEquals(expectedSiblingId, sibling.getAttribute("id"), "wrong sibling");
        
    '''
    code = []
    code.append('\t' +\
                create_selenium_webelement_declaration('sibling',\
                                                              create_selenium_find_element('tag',\
                                                                                           create_selenium_by_xpath('xpath'))))
    code.append(create_assert_equals('expectedSiblingId',\
                                     SELENIUM_GET_ATTRIBUTE %('sibling', 'id'), 'sibling'))
    
    return '\n\t\t'.join(code) 


def __create_unittest_no_sibling_assertion():
    '''
    Creates the asserThrows expression for the case when no sibling is expected
    examle:
        assertThrows(NoSuchElementException.class, () -> tag.findElement(By.xpath(xpath)));
    '''
    by_xpath = create_selenium_by_xpath('xpath')
    find_by = create_selenium_find_element('tag', by_xpath)
    
    return '\t' + create_assert_throws(NO_SUCH_ELEMENT_EXCEPTION_CLASS, '() -> ' + find_by)

def create_unittest_parent(tag_id, parent_tag_id):
    '''
    Creates the unit test method for testing the parent of an html tag.
    example:
    /**
     * Test if the tag with id==link_main_theme has the parent with the id==head. 
     */
    @Test
    public void testLinkLinkMainThemeParent() {

        WebElement tag = DRIVER.findElement(By.id("link_main_theme"));
        WebElement parentTag = tag.findElement(By.xpath("./.."));
        assertEquals("head", parentTag.getAttribute("id"), "wrong parent");
    }
    '''
    if parent_tag_id == '':
        return ''
    
    test_case_content = ['']
    test_case_content.append(create_tag_under_unittest_var_assignment(tag_id))
    
    parent_xpath_expr = create_selenium_by_xpath('"./.."');
    parent_find_expr = create_selenium_find_element('tag', parent_xpath_expr)
    parent_tag_var = create_selenium_webelement_declaration('parent', parent_find_expr)

    test_case_content.append(parent_tag_var)
    test_case_content.append(create_assert_equals('"%s"' %parent_tag_id,\
                                                  SELENIUM_GET_ATTRIBUTE %('parent', 'id'), 'parent'))
    
    method_name = convert_tag_id_to_name_in_method(tag_id) + 'Parent'
    
    unit_test_method = create_unittest_method(method_name, '\n\t'.join(test_case_content))
    
    return '\n'.join([JAVA_DOC_TEST_PARENT %(tag_id, parent_tag_id), unit_test_method])
    
def create_unittest_tag_name(tag_id, expected_tag_name):
    '''
    Creates the unit test method for testing the html tag name
    example:
    /**
     * Test if the tag with the id title has the tag name "title".
     */
    @Test
    public void testTitleTagName() {

        final WebElement tag = DRIVER.findElement(By.id("title"));
        assertEquals("title", tag.getTagName());

    }
    '''
    test_case_content = ['']
    test_case_content.append(create_tag_under_unittest_var_assignment(tag_id))
    test_case_content.append(create_assert_equals('"%s"' %(expected_tag_name), 'tag.getTagName()', 'tag name'))
    
    method_name = convert_tag_id_to_name_in_method(tag_id) + 'TagName'
    
    unit_test_method = create_unittest_method(method_name, '\n\t'.join(test_case_content))
    
    return '\n'.join([JAVA_DOC_TEST_TAG_NAME %(tag_id, expected_tag_name), unit_test_method])

def convert_tag_id_to_name_in_method(tag_id):
    '''
    Converts the given tag_id to the name which is inserted in the test case method.
    link_main_theme --> LinkMainTheme
    '''
    wrk_name = tag_id.replace('_', ' ')    
    wrk_name = wrk_name.title()
    
    return wrk_name.replace(' ', '')
