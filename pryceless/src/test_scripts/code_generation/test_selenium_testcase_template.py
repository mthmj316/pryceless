'''
Created on 23.06.2020

@author: mthoma
'''
import unittest

from scripts.code_generation.selenium_testcase_template import get_template,\
    ASSERT_EQUALS_TEMPLATE

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    '''
        tests the selenium_testcase_template.get_template() function
    '''
    def test_get_template(self):
        template_content = get_template(ASSERT_EQUALS_TEMPLATE)
        self.assertEqual('assertEquals($expected, $actual,"wrong $attribute");\n', template_content, 'wrong template content')


if __name__ == "__main__":
    unittest.main()