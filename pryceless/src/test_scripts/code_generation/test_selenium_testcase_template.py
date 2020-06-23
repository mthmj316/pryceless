'''
Created on 23.06.2020

@author: mthoma
'''
import unittest

from scripts.code_generation.selenium_testcase_template import get_template,\
    ASSERT_EQUALS_TEMPLATE, create_assert_equals, create_assert_notnull,\
    create_tag_under_test_var_assignment, create_assert_null
    
WRONG_ASSERT_EQUALS = 'wrong assertEquals'

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass
    
    '''
       tests the selenium_testcase_template.create_tag_under_test_var_assignment() function
       tag_id == login_form
    '''
    def test_create_tag_under_test_var_assignment(self):
        expected = 'final WebElement tag = DRIVER.findElement(By.id("login_form"));\n'
        actual = create_tag_under_test_var_assignment('login_form')
        self.assertEqual(expected, actual)
    
    '''
       tests the selenium_testcase_template.create_assert_null() function
       testing replacement by string==space
    '''
    def test_create_assert_null_space(self):
        expected = 'assertNull(" ");\n'
        actual = create_assert_null('" "')
        self.assertEqual(expected, actual)
    
    '''
       tests the selenium_testcase_template.create_assert_null() function
       testing replacement by string==<empty string>
    '''
    def test_create_assert_null_emptystring(self):
        expected = 'assertNull("");\n'
        actual = create_assert_null('""')
        self.assertEqual(expected, actual)
        
    '''
       tests the selenium_testcase_template.create_assert_null() function
       testing replacement by string==null
    '''
    def test_create_assert_null_null(self):
        expected = 'assertNull(null);\n'
        actual = create_assert_null('null')
        self.assertEqual(expected, actual)
    
    '''
       tests the selenium_testcase_template.create_assert_notnull() function
       testing replacement by string==space
    '''
    def test_create_assert_notnull_space(self):
        expected = 'assertNotNull(" ");\n'
        actual = create_assert_notnull('" "')
        self.assertEqual(expected, actual)
    
    '''
       tests the selenium_testcase_template.create_assert_notnull() function
       testing replacement by string==<empty string>
    '''
    def test_create_assert_notnull_emptystring(self):
        expected = 'assertNotNull("");\n'
        actual = create_assert_notnull('""')
        self.assertEqual(expected, actual)
        
    '''
       tests the selenium_testcase_template.create_assert_notnull() function
       testing replacement by string==null
    '''
    def test_create_assert_notnull_null(self):
        expected = 'assertNotNull(null);\n'
        actual = create_assert_notnull('null')
        self.assertEqual(expected, actual)
    
    '''
        tests the selenium_testcase_template.create_assert_equals() function
        testing replacement by whitespaces within double quotes
    '''      
    def test_create_assert_equals_semikolon_whitespace(self):
        expected = 'assertEquals( , ,"wrong iam-a-attribute");\n'
        actual = create_assert_equals(' ', '', 'iam-a-attribute')
        self.assertEqual(expected, actual, WRONG_ASSERT_EQUALS)

    '''
        tests the selenium_testcase_template.create_assert_equals() function
        testing replacement by whitespaces
    '''   
    def test_create_assert_equals_whitespace(self):
        expected = 'assertEquals("", " ","wrong iam-a-attribute");\n'
        actual = create_assert_equals('""', '" "', 'iam-a-attribute')
        self.assertEqual(expected, actual, WRONG_ASSERT_EQUALS)

    '''
        tests the selenium_testcase_template.create_assert_equals() function
        testing replacement by strings which are not empty
    '''
    def test_create_assert_equals(self):
        expected = 'assertEquals(that is what is expected, that is what is actually is,"wrong iam-a-attribute");\n'
        actual = create_assert_equals('that is what is expected', \
                                      'that is what is actually is', \
                                      'iam-a-attribute')
        self.assertEqual(expected, actual, WRONG_ASSERT_EQUALS)

    '''
        tests the selenium_testcase_template.get_template() function
    '''
    def test_get_template(self):
        template_content = get_template(ASSERT_EQUALS_TEMPLATE)
        self.assertEqual('assertEquals($expected, $actual,"wrong $attribute");\n', \
                         template_content, 'wrong template content')


if __name__ == "__main__":
    unittest.main()