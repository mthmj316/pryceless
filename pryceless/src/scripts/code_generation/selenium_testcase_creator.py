'''
Created on 25.06.2020

The following test case can be created by this script:
    - test tag name

@author: mthoma
'''

JAVA_DOC_TEST_TAG_NAM = '/**\n* Test if the tag with id==%s has the tag name==%s.\n*/'

from scripts.code_generation.selenium_testcase_template import create_tag_under_test_var_assignment,\
    create_unit_test_method, create_assert_equals

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
    
    return '\n'.join([JAVA_DOC_TEST_TAG_NAM %(tag_id, expected_tag_name), unit_test_method])

'''
    Converts the given tag_id to the name which is inserted in the test case method.
    link_main_theme --> LinkMainTheme
'''
def convert_tag_id_to_name_in_method(tag_id):
    
    wrk_name = tag_id.replace('_', ' ')    
    wrk_name = wrk_name.title()
    
    return wrk_name.replace(' ', '')