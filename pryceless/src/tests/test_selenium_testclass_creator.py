'''
Created on 07.07.2020

@author: mthoma
'''
import unittest
import os
from scripts.selenium_testclass_creator import SeleniumTestClassCreator
from scripts.html_page import HTMLPage
from scripts.html_element import HTMLElement

SELENIUM_TEST_CLASS_2_TESTCASE = 'selenium_class.2.expected'

class Test(unittest.TestCase):


    def test_create_html_tag_unittest(self):
        '''
        Test only test cases for HTML tag is created: selenium_class.2.expected
        '''
        path_to_templates = os.path.join(os.path.dirname(os.path.abspath(__file__)), SELENIUM_TEST_CLASS_2_TESTCASE)
            
        with open(path_to_templates, 'r') as file:
            expected = file.read()
        
        
        html_element = HTMLElement('html', 'html_id')
        html_element.add_attribute('lang', 'en')
        
        page = HTMLPage('main_page', 'https://some.super.webpage:8080')
        page.add_html_elements(html_element)
        
        tccreator =  SeleniumTestClassCreator(page)
        
        self.maxDiff = None
        self.assertEqual(expected, tccreator.create())


if __name__ == "__main__":
    unittest.main()