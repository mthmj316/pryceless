'''
Created on 23.06.2020

@author: mthoma
'''
import importlib.resources as pkg_resources
import unittest

from scripts.selenium_test_generator.selenium_testcase_template import \
    ASSERT_EQUALS_TEMPLATE, create_assert_equals, create_assert_notnull, \
    create_tag_under_test_var_assignment, create_assert_null, \
    create_assert_throws, create_selenium_by_xpath, create_selenium_by_id, \
    create_selenium_find_element, create_selenium_webelement_declaration, \
    create_unit_test_method, create_parameterized_test_method, \
    create_method_parameter_list, create_annotation, create_csvsource_annotation,\
    create_selenium_test_class
from scripts import selenium_test_generator
import templates


SELENIUM_TEST_CLASS_1_TESTCASE = 'selenium_test_class.1.testcase'

WRONG_ASSERT_EQUALS = 'wrong assertEquals'

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    
    def test_create_selenium_test_class(self):
        with open(SELENIUM_TEST_CLASS_1_TESTCASE, 'r') as file:
            expected = file.read()
        actual = create_selenium_test_class('https://some.super.webpage:8080',\
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
    
    '''
        test the selenium_testcase.create_annotation(annotation_name, annotation_parameters) function
        With annotation parameters
    '''
    def test_create_annotation_with_para(self):
        expected = '@some_annotation(para, para1)'
        actual = create_annotation('some_annotation', 'para, para1')
        self.assertEqual(expected, actual)
    
    '''
        test the selenium_testcase.create_annotation(annotation_name, annotation_parameters) function
        No annotation parameters
    '''
    def test_create_annotation_no_para(self):
        expected = '@some_annotation()'
        actual = create_annotation('some_annotation', '')
        self.assertEqual(expected, actual)
  
    '''
        test the selenium_testcase.create_method_parameter_list(parameter_dict)
        Many parameter
    '''
    def test_create_method_parameter_list_many_para(self):
        para_dic = {'name': 'String', 'age':'int', 'sex':'char', 'surname':'String'}
        expected = 'String name, int age, char sex, String surname'
        actual = create_method_parameter_list(para_dic)
        self.assertEqual(expected, actual)
      
    '''
        test the selenium_testcase.create_method_parameter_list(parameter_dict)
        Two parameter
    '''
    def test_create_method_parameter_list_two_para(self):
        para_dic = {'name': 'String', 'age':'int'}
        expected = 'String name, int age'
        actual = create_method_parameter_list(para_dic)
        self.assertEqual(expected, actual)
   
    '''
        test the selenium_testcase.create_method_parameter_list(parameter_dict)
        No parameter
    '''
    def test_create_method_parameter_list_no_para(self):
        para_dic = {}
        expected = ''
        actual = create_method_parameter_list(para_dic)
        self.assertEqual(expected, actual)
    
    '''
        test the selenium_testcase.create_method_parameter_list(parameter_dict)
        One parameter
    '''
    def test_create_method_parameter_list_one_para(self):
        para_dic = {'name': 'String'}
        expected = 'String name'
        actual = create_method_parameter_list(para_dic)
        self.assertEqual(expected, actual)
    
    '''
        test the selenium_testcase.create_parameterized_test_method(variable_dict)
    '''
    def test_create_parameterized_test_method(self):
        var_dict = {'parameter_sources':'@annotation',
                    'what_is_tested':'ARealyCoolTest',
                    'parameters':'String name', 
                    'test_method_content':'assert(name,this.getName());'
        }
        
        expected = '@ParameterizedTest\n@annotation\npublic void testARealyCoolTest(String name){\n\tassert(name,this.getName());\n}'
        actual = create_parameterized_test_method(var_dict)
        self.assertEqual(expected, actual)

    '''
       tests the selenium_testcase_template.create_create_unit_test_method() function
    '''
    def test_create_unit_test_method_single_line_content(self):
        expected = '@Test\npublic void testHTMLLang(){\n\tthis is a single line content\n}'
        actual = create_unit_test_method('HTMLLang', '\tthis is a single line content')
        self.assertEqual(expected, actual)

    '''
       tests the selenium_testcase_template.create_selenium_webelement_declaration() function
    '''
    def test_create_selenium_webelement_declaration(self):
        expected = 'final WebElement otherTag = someTag.findElement(By.id("some id"));'
        actual = create_selenium_webelement_declaration('otherTag', 'someTag.findElement(By.id("some id"))')
        self.assertEqual(expected, actual)

    '''
       tests the selenium_testcase_template.create_selenium_find_element() function
    '''
    def test_create_selenium_find_element(self):
        expected = 'someTag.findElement(By.id("some id"))'
        actual = create_selenium_find_element('someTag', 'By.id("some id")')
        self.assertEqual(expected, actual)

    '''
       tests the selenium_testcase_template.create_selenium_by_id() function
    '''
    def test_create_selenium_by_id(self):
        expected = 'By.id("some id")'
        actual = create_selenium_by_id('"some id"')
        self.assertEqual(expected, actual)
    
    '''
       tests the selenium_testcase_template.create_selenium_by_xpath() function
    '''
    def test_create_selenium_by_xpath(self):
        expected = 'By.xpath("this is a xpath expression")'
        actual = create_selenium_by_xpath('"this is a xpath expression"')
        self.assertEqual(expected, actual)
    
    '''
       tests the selenium_testcase_template.create_assert_throws() function
    '''
    def test_create_assert_throws(self):
        expected = 'assertThrows(NullpointerException.class, () -> do something);'
        actual = create_assert_throws('NullpointerException.class', '() -> do something')
        self.assertEqual(expected, actual)
    
    '''
       tests the selenium_testcase_template.create_tag_under_test_var_assignment() function
       tag_id == login_form
    '''
    def test_create_tag_under_test_var_assignment(self):
        expected = 'final WebElement tag = DRIVER.findElement(By.id("login_form"));'
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
        expected = 'assertEquals( , ,"wrong iam-a-attribute");'
        actual = create_assert_equals(' ', '', 'iam-a-attribute')
        self.assertEqual(expected, actual, WRONG_ASSERT_EQUALS)

    '''
        tests the selenium_testcase_template.create_assert_equals() function
        testing replacement by whitespaces
    '''   
    def test_create_assert_equals_whitespace(self):
        expected = 'assertEquals("", " ","wrong iam-a-attribute");'
        actual = create_assert_equals('""', '" "', 'iam-a-attribute')
        self.assertEqual(expected, actual, WRONG_ASSERT_EQUALS)

    '''
        tests the selenium_testcase_template.create_assert_equals() function
        testing replacement by strings which are not empty
    '''
    def test_create_assert_equals(self):
        expected = 'assertEquals(that is what is expected, that is what is actually is,"wrong iam-a-attribute");'
        actual = create_assert_equals('that is what is expected', \
                                      'that is what is actually is', \
                                      'iam-a-attribute')
        self.assertEqual(expected, actual, WRONG_ASSERT_EQUALS)

    '''
        tests the selenium_testcase_template.get_template() function
    '''
    def test_get_template(self):
        template_content = pkg_resources.read_text(templates, ASSERT_EQUALS_TEMPLATE)
        self.assertEqual('assertEquals($expected, $actual,"wrong $attribute");', \
                         template_content, 'wrong template content')

    
if __name__ == "__main__":
    unittest.main()