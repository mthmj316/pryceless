'''
Created on 25.06.2020

@author: mthoma
'''
import unittest
from scripts.selenium_test_generator.selenium_testcase_creator import create_unit_test_css_rule,\
    create_unit_test_attribute, create_unit_test_siblings,\
    create_unit_test_parent, create_unit_test_tag_name,\
    convert_tag_id_to_name_in_method

from tests.prycelesstest_constants import MULTIPLE_CSS_RULE_TEST,\
    SINGLE_CSS_RULE_TEST, MULTIPLE_TEST_ATTRIBUTES, SINGLE_TEST_ATTRIBUTES,\
    NO_SIBLING_EXPECTED_RESULT, NO_FOLLOWING_SIBLING_EXPECTED_RESULT,\
    NO_PRECIDING_SIBLING_EXPECTED_RESULT, SIBLING_EXPECTED_RESULT


class Test(unittest.TestCase):

    def test_create_unit_test_css_rule_multiple_css_rule(self):
        attribute_directory = {'color':'#323454',
                               'font':'new-times-roman',
                               'stressed':'bold'}
        actual = create_unit_test_css_rule('login_name', attribute_directory)
        self.maxDiff = None
        self.assertEqual(MULTIPLE_CSS_RULE_TEST, actual)
    
    def test_create_unit_test_css_rule_single_css_rule(self):
        attribute_directory = {'color':'#323454'}
        actual = create_unit_test_css_rule('login_name', attribute_directory)
        self.maxDiff = None
        self.assertEqual(SINGLE_CSS_RULE_TEST, actual)

    def test_create_unit_test_attribute_multiple_attr(self):
        attribute_directory = {'placeholder':'User name',
                               'value':'Hello',
                               'class':'cls_login_form'}
        actual = create_unit_test_attribute('login_name', attribute_directory)
        self.maxDiff = None
        self.assertEqual(MULTIPLE_TEST_ATTRIBUTES, actual)
    
    def test_create_unit_test_attribute_single_attr(self):
        attribute_directory = {'placeholder':'User name'}
        actual = create_unit_test_attribute('login_name', attribute_directory)
        self.maxDiff = None
        self.assertEqual(SINGLE_TEST_ATTRIBUTES, actual)
    
    def test_create_unit_test_no_siblings(self):
        actual = create_unit_test_siblings('login_password', '', '')
        self.maxDiff = None
        self.assertEqual(NO_SIBLING_EXPECTED_RESULT, actual)
    
    def test_create_unit_test_siblings_no_following(self):
        actual = create_unit_test_siblings('login_password', 'login_error_message', '')
        self.maxDiff = None
        self.assertEqual(NO_FOLLOWING_SIBLING_EXPECTED_RESULT, actual)
    
    def test_create_unit_test_siblings_no_preceding(self):
        actual = create_unit_test_siblings('login_password', '', 'login_name')
        self.maxDiff = None
        self.assertEqual(NO_PRECIDING_SIBLING_EXPECTED_RESULT, actual)
    
    def test_create_unit_test_siblings(self):
        actual = create_unit_test_siblings('login_password', 'login_error_message', 'login_name')
        self.maxDiff = None
        self.assertEqual(SIBLING_EXPECTED_RESULT, actual)
    
    def test_create_unit_test_parent(self):
        expected = ('/**\n* Test if the tag with id==main_header has the parent with the id==main_container.\n*/'
                    '\n@Test'
                    '\npublic void testMainHeaderParent(){'
                    '\n'
                    '\n\tfinal WebElement tag = DRIVER.findElement(By.id("main_header"));'
                    '\n\tfinal WebElement parent = tag.findElement(By.xpath("./.."));'
                    '\n\tassertEquals("main_container", parent.getAttribute("id"),"wrong parent");'
                    '\n}'
                    )
        actual = create_unit_test_parent('main_header', 'main_container')
        self.assertEqual(expected, actual)
    
    def test_create_unit_test_tag_name(self):
        expected = ('/**\n* Test if the tag with id==main_center_container has the tag name==div.\n*/'
                    '\n@Test'
                    '\npublic void testMainCenterContainerTagName(){'
                    '\n'
                    '\n\tfinal WebElement tag = DRIVER.findElement(By.id("main_center_container"));'
                    '\n\tassertEquals("div", tag.getTagName(),"wrong tag name");'
                    '\n}'
                    )
        actual = create_unit_test_tag_name('main_center_container', 'div')
        self.assertEqual(expected, actual)
    
    def test_convert_tag_id_to_name_in_method_trailing_underscore(self):
        expected = 'HtmlId'
        actual = convert_tag_id_to_name_in_method('_html_id_')
        self.assertEqual(expected, actual)

    def test_convert_tag_id_to_name_in_method_leading_underscore(self):
        expected = 'HtmlId'
        actual = convert_tag_id_to_name_in_method('_html_id')
        self.assertEqual(expected, actual)

    def test_convert_tag_id_to_name_in_method_with_underscore(self):
        expected = 'HtmlId'
        actual = convert_tag_id_to_name_in_method('html_id')
        self.assertEqual(expected, actual)

    def test_convert_tag_id_to_name_in_method_no_underscore(self):
        expected = 'Html'
        actual = convert_tag_id_to_name_in_method('html')
        self.assertEqual(expected, actual)
        
    def test_convert_tag_id_to_name_in_method_one_letter(self):
        expected = 'H'
        actual = convert_tag_id_to_name_in_method('h')
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()