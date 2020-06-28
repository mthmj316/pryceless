'''
Created on 25.06.2020

The following test case can be created by this script:
    - test tag name

@author: mthoma
'''

JAVA_DOC_TEST_TAG_NAME = '/**\n* Test if the tag with id==%s has the tag name==%s.\n*/'
JAVA_DOC_TEST_PARENT = '/**\n* Test if the tag with id==%s has the parent with the id==%s.\n*/'
SELENIUM_GET_ATTRIBUTE = '%s.getAttribute("%s")'
SIBLING_CSV_SOURCE_ANNOTATION = '@CsvSource({"%s,preceding-sibling::*[1]", "%s,following-sibling::*[1]"})'

NO_SUCH_ELEMENT_EXCEPTION_CLASS = 'org.openqa.selenium.NoSuchElementException.class'

from scripts.code_generation.selenium_testcase_template import create_tag_under_test_var_assignment,\
    create_unit_test_method, create_assert_equals,\
    create_selenium_webelement_declaration, create_selenium_find_element,\
    create_selenium_by_xpath, create_assert_throws,\
    create_parameterized_test_method

'''
    Creates the test methods for testing the siblings of the html tag with id==tag_id
    If both predecessor_id and  successor_id is set then one unit test method will be created 
    tag_id -> html id of the tag for which the siblings are tested
    predecessor_id  -> id of the tag which must be directly before the tag under test
                    -> if none then the test will be 
'''
def create_unit_test_siblings(tag_id, predecessor_id, successor_id):
    code = ['']
    code.append(create_tag_under_test_var_assignment(tag_id))
    code.append('if(expectedSiblingId == null) {')
    code.append(__create_unit_test_no_sibling_assertion())
    code.append('} else {')
    code.append(__create_unit_test_sibling())
    code.append('}')
    
    variable_dict = {'parameter_sources': __create_unit_test_sibling_csv_source(predecessor_id, successor_id),
                     'what_is_tested': convert_tag_id_to_name_in_method(tag_id) + 'Sibling',
                     'parameters': 'final String expectedSiblingId, final String xpath',
                     'test_method_content': '\n\t'.join(code)}
    
    return create_parameterized_test_method(variable_dict)

def __create_unit_test_sibling_csv_source(predecessor_id, successor_id):
    return SIBLING_CSV_SOURCE_ANNOTATION %(predecessor_id, successor_id)

'''
    Creates the test for when a sibling is expected.
    example:
        final WebElement sibling = tag.findElement(By.xpath(xpath));
        assertEquals(expectedSiblingId, sibling.getAttribute("id"), "wrong sibling");
        
'''
def __create_unit_test_sibling():
    code = ['']
    code.append(create_selenium_webelement_declaration('sibling', create_selenium_find_element('tag', create_selenium_by_xpath('xpath'))))
    code.append(create_assert_equals('expectedSiblingId', SELENIUM_GET_ATTRIBUTE %('sibling', 'id'), 'sibling'))
    
    return '\n\t'.join(code) 

'''
    Creates the asserThrows expression for the case when no sibling is expected
    examle:
        assertThrows(NoSuchElementException.class, () -> tag.findElement(By.xpath(xpath)));
'''
def __create_unit_test_no_sibling_assertion():
    by_xpath = create_selenium_by_xpath('xpath')
    find_by = create_selenium_find_element('tag', by_xpath)
    
    return '\t' + create_assert_throws(NO_SUCH_ELEMENT_EXCEPTION_CLASS, find_by)

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
def create_unit_test_parent(tag_id, parent_tag_id):
    test_case_content = ['']
    test_case_content.append(create_tag_under_test_var_assignment(tag_id))
    
    parent_xpath_expr = create_selenium_by_xpath('"./.."');
    parent_find_expr = create_selenium_find_element('tag',parent_xpath_expr)
    parent_tag_var = create_selenium_webelement_declaration('parent',parent_find_expr)
    
    test_case_content.append(parent_tag_var)
    test_case_content.append(create_assert_equals('"%s"' %parent_tag_id, SELENIUM_GET_ATTRIBUTE %('parent', 'id'), 'parent'))
    
    method_name = convert_tag_id_to_name_in_method(tag_id) + 'Parent'
    
    unit_test_method = create_unit_test_method(method_name, '\n\t'.join(test_case_content))
    
    return '\n'.join([JAVA_DOC_TEST_PARENT %(tag_id, parent_tag_id), unit_test_method])
    

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
def create_unit_test_tag_name(tag_id, expected_tag_name):
    
    test_case_content = ['']
    test_case_content.append(create_tag_under_test_var_assignment(tag_id))
    test_case_content.append(create_assert_equals('"%s"' %(expected_tag_name),'tag.getTagName()', 'tag name'))
    
    method_name = convert_tag_id_to_name_in_method(tag_id) + 'TagName'
    
    unit_test_method = create_unit_test_method(method_name, '\n\t'.join(test_case_content))
    
    return '\n'.join([JAVA_DOC_TEST_TAG_NAME %(tag_id, expected_tag_name), unit_test_method])

'''
    Converts the given tag_id to the name which is inserted in the test case method.
    link_main_theme --> LinkMainTheme
'''
def convert_tag_id_to_name_in_method(tag_id):
    
    wrk_name = tag_id.replace('_', ' ')    
    wrk_name = wrk_name.title()
    
    return wrk_name.replace(' ', '')
