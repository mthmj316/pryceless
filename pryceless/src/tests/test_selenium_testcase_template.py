'''
Created on 23.06.2020

@author: mthoma
'''

import unittest

from scripts.selenium_testcase_template import \
    create_assert_equals, create_assert_notnull, \
    create_tag_under_unittest_var_assignment, create_assert_null, \
    create_assert_throws, create_selenium_by_xpath, create_selenium_by_id, \
    create_selenium_find_element, create_selenium_webelement_declaration, \
    create_unittest_method, create_parameterized_unittest_method, \
    create_method_parameter_list, create_annotation, create_csvsource_annotation, \
    create_selenium_unittest_class
import os

SELENIUM_TEST_CLASS_1_TESTCASE = 'selenium_class.1.expected'

WRONG_ASSERT_EQUALS = 'wrong assertEquals'

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    
    def test_create_selenium_test_class(self):
        path_to_templates = os.path.join(os.path.dirname(os.path.abspath(__file__)), SELENIUM_TEST_CLASS_1_TESTCASE)
            
        with open(path_to_templates, 'r') as file:
            expected = file.read()
        actual = create_selenium_unittest_class('https://some.super.webpage:8080',\
                                            '//Das ist nur ein Test.')
        self.maxDiff = None
        self.assertEqual(expected, actual)
    
    def test_create_csvsource_annotation_no_param(self):
        expected = '@CsvSource()'
        parameter_dictionary = {
        }
        actual = create_csvsource_annotation(parameter_dictionary)
        self.assertEqual(expected, actual)
    
    def test_create_csvsource_annotation_one_param(self):
        expected = '@CsvSource({"key_1,value_1"})'
        parameter_dictionary = {
            'key_1':'value_1'
        }
        actual = create_csvsource_annotation(parameter_dictionary)
        self.assertEqual(expected, actual)
    
    def test_create_csvsource_annotation_many_param(self):
        expected = '@CsvSource({"key_1,value_1","key_2,value_2","key_3,value_3"})'
        parameter_dictionary = {
            'key_1':'value_1',
            'key_2':'value_2',
            'key_3':'value_3'
        }
        actual = create_csvsource_annotation(parameter_dictionary)
        self.assertEqual(expected, actual)
    

    def test_create_annotation_with_para(self):
        '''
        test the selenium_testcase.create_annotation(annotation_name, annotation_parameters) function
        With annotation parameters
        '''
        expected = '@some_annotation(para, para1)'
        actual = create_annotation('some_annotation', 'para, para1')
        self.assertEqual(expected, actual)
    

    def test_create_annotation_no_para(self):
        '''
        test the selenium_testcase.create_annotation(annotation_name, annotation_parameters) function
        No annotation parameters
        '''
        expected = '@some_annotation()'
        actual = create_annotation('some_annotation', '')
        self.assertEqual(expected, actual)
  

    def test_create_method_parameter_list_many_para(self):
        '''
            test the selenium_testcase.create_method_parameter_list(parameter_dict)
            Many parameter
        '''
        para_dic = {'name': 'String', 'age':'int', 'sex':'char', 'surname':'String'}
        expected = 'String name, int age, char sex, String surname'
        actual = create_method_parameter_list(para_dic)
        self.assertEqual(expected, actual)
      

    def test_create_method_parameter_list_two_para(self):
        '''
            test the selenium_testcase.create_method_parameter_list(parameter_dict)
            Two parameter
        '''
        para_dic = {'name': 'String', 'age':'int'}
        expected = 'String name, int age'
        actual = create_method_parameter_list(para_dic)
        self.assertEqual(expected, actual)
   

    def test_create_method_parameter_list_no_para(self):
        '''
        test the selenium_testcase.create_method_parameter_list(parameter_dict)
        No parameter
        '''
        para_dic = {}
        expected = ''
        actual = create_method_parameter_list(para_dic)
        self.assertEqual(expected, actual)

    def test_create_method_parameter_list_one_para(self):
        '''
            test the selenium_testcase.create_method_parameter_list(parameter_dict)
            One parameter
        '''
        para_dic = {'name': 'String'}
        expected = 'String name'
        actual = create_method_parameter_list(para_dic)
        self.assertEqual(expected, actual)
    

    def test_create_parameterized_test_method(self):
        '''
        test the selenium_testcase.create_parameterized_test_method(variable_dict)
        '''
        var_dict = {'parameter_sources':'@annotation',
                    'what_is_tested':'ARealyCoolTest',
                    'parameters':'String name', 
                    'test_method_content':'assert(name,this.getName());'
        }
        
        expected = '@ParameterizedTest\n@annotation\npublic void testARealyCoolTest(String name){\n\tassert(name,this.getName());\n}'
        actual = create_parameterized_unittest_method(var_dict)
        self.assertEqual(expected, actual)


    def test_create_unit_test_method_single_line_content(self):
        '''
           tests the selenium_testcase_template.create_create_unit_test_method() function
        '''
        expected = '@Test\npublic void testHTMLLang(){\n\tthis is a single line content\n}'
        actual = create_unittest_method('HTMLLang', '\tthis is a single line content')
        self.assertEqual(expected, actual)


    def test_create_selenium_webelement_declaration(self):
        '''
           tests the selenium_testcase_template.create_selenium_webelement_declaration() function
        '''
        expected = 'final WebElement otherTag = someTag.findElement(By.id("some id"));'
        actual = create_selenium_webelement_declaration('otherTag', 'someTag.findElement(By.id("some id"))')
        self.assertEqual(expected, actual)


    def test_create_selenium_find_element(self):
        '''
           tests the selenium_testcase_template.create_selenium_find_element() function
        '''
        expected = 'someTag.findElement(By.id("some id"))'
        actual = create_selenium_find_element('someTag', 'By.id("some id")')
        self.assertEqual(expected, actual)


    def test_create_selenium_by_id(self):
        '''
           tests the selenium_testcase_template.create_selenium_by_id() function
        '''
        expected = 'By.id("some id")'
        actual = create_selenium_by_id('"some id"')
        self.assertEqual(expected, actual)
    

    def test_create_selenium_by_xpath(self):
        '''
           tests the selenium_testcase_template.create_selenium_by_xpath() function
        '''
        expected = 'By.xpath("this is a xpath expression")'
        actual = create_selenium_by_xpath('"this is a xpath expression"')
        self.assertEqual(expected, actual)
    
 
    def test_create_assert_throws(self):
        '''
           tests the selenium_testcase_template.create_assert_throws() function
        '''
        expected = 'assertThrows(NullpointerException.class, () -> do something);'
        actual = create_assert_throws('NullpointerException.class', '() -> do something')
        self.assertEqual(expected, actual)
    

    def test_create_tag_under_test_var_assignment(self):
        '''
           tests the selenium_testcase_template.create_tag_under_test_var_assignment() function
           tag_id == login_form
        '''
        expected = 'final WebElement tag = DRIVER.findElement(By.id("login_form"));'
        actual = create_tag_under_unittest_var_assignment('login_form')
        self.assertEqual(expected, actual)
    

    def test_create_assert_null_space(self):
        '''
           tests the selenium_testcase_template.create_assert_null() function
           testing replacement by string==space
        '''
        expected = 'assertNull(" ");\n'
        actual = create_assert_null('" "')
        self.assertEqual(expected, actual)
    

    def test_create_assert_null_emptystring(self):
        '''
           tests the selenium_testcase_template.create_assert_null() function
           testing replacement by string==<empty string>
        '''
        expected = 'assertNull("");\n'
        actual = create_assert_null('""')
        self.assertEqual(expected, actual)
        

    def test_create_assert_null_null(self):
        '''
           tests the selenium_testcase_template.create_assert_null() function
           testing replacement by string==null
        '''
        expected = 'assertNull(null);\n'
        actual = create_assert_null('null')
        self.assertEqual(expected, actual)
    

    def test_create_assert_notnull_space(self):
        '''
           tests the selenium_testcase_template.create_assert_notnull() function
           testing replacement by string==space
        '''
        expected = 'assertNotNull(" ");\n'
        actual = create_assert_notnull('" "')
        self.assertEqual(expected, actual)
    

    def test_create_assert_notnull_emptystring(self):
        '''
           tests the selenium_testcase_template.create_assert_notnull() function
           testing replacement by string==<empty string>
        '''
        expected = 'assertNotNull("");\n'
        actual = create_assert_notnull('""')
        self.assertEqual(expected, actual)
        

    def test_create_assert_notnull_null(self):
        '''
           tests the selenium_testcase_template.create_assert_notnull() function
           testing replacement by string==null
        '''
        expected = 'assertNotNull(null);\n'
        actual = create_assert_notnull('null')
        self.assertEqual(expected, actual)
    
   
    def test_create_assert_equals_semikolon_whitespace(self):
        '''
            tests the selenium_testcase_template.create_assert_equals() function
            testing replacement by whitespaces within double quotes
        '''   
        expected = 'assertEquals( , ,"wrong iam-a-attribute");'
        actual = create_assert_equals(' ', '', 'iam-a-attribute')
        self.assertEqual(expected, actual, WRONG_ASSERT_EQUALS)


    def test_create_assert_equals_whitespace(self):
        '''
            tests the selenium_testcase_template.create_assert_equals() function
            testing replacement by whitespaces
        '''   
        expected = 'assertEquals("", " ","wrong iam-a-attribute");'
        actual = create_assert_equals('""', '" "', 'iam-a-attribute')
        self.assertEqual(expected, actual, WRONG_ASSERT_EQUALS)


    def test_create_assert_equals(self):
        '''
            tests the selenium_testcase_template.create_assert_equals() function
            testing replacement by strings which are not empty
        '''
        expected = 'assertEquals(that is what is expected, that is what is actually is,"wrong iam-a-attribute");'
        actual = create_assert_equals('that is what is expected', \
                                      'that is what is actually is', \
                                      'iam-a-attribute')
        self.assertEqual(expected, actual, WRONG_ASSERT_EQUALS)

    
if __name__ == "__main__":
    unittest.main()
