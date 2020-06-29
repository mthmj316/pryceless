'''
Created on 25.06.2020

@author: mthoma
'''
import unittest
from scripts.code_generation.selenium_testcase_creator import convert_tag_id_to_name_in_method,\
    create_unit_test_tag_name, create_unit_test_parent,\
    create_unit_test_siblings
from test_scripts.code_generation.test_constants import SIBLING_EXPECTED_RESULT,\
    NO_PRECIDING_SIBLING_EXPECTED_RESULT, NO_FOLLOWING_SIBLING_EXPECTED_RESULT,\
    NO_SIBLING_EXPECTED_RESULT
    


class Test(unittest.TestCase):
    
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