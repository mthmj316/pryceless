'''
Created on 07.07.2020

@author: mthoma
'''
import unittest
import os
from scripts.selenium_testclass_creator import SeleniumTestClassCreator
from scripts.html_page import HTMLPage
from scripts.html_element import HTMLElement
from re import RegexFlag
import re

SELENIUM_TEST_CLASS_2_TESTCASE = 'selenium_class.2.expected'
SELENIUM_TEST_CLASS_3_TESTCASE = 'selenium_class.3.expected'
SELENIUM_TEST_CLASS_4_TESTCASE = 'selenium_class.4.expected'
SELENIUM_TEST_CLASS_5_TESTCASE = 'selenium_class.5.expected'

REMOVE_LINE_PRECEING_TABS_AND_WS = r'(^[ \t]+|[ \t]+(?=:))'
TEST_URL = 'https://some.super.webpage:8080'

class Test(unittest.TestCase):
    
    def test_create_some_tag_unittest_noval_att(self):
        '''
        Test some tag is created: selenium_class.5.expected
        '''
        path_to_templates = os.path.join(os.path.dirname(os.path.abspath(__file__)), SELENIUM_TEST_CLASS_5_TESTCASE)
            
        with open(path_to_templates, 'r') as file:
            expected = file.read()
        
        expected = re.sub(REMOVE_LINE_PRECEING_TABS_AND_WS, '', expected, flags=RegexFlag.M)
        
        html_element = HTMLElement('div', 'some_div_id')
        html_element.parent_id = 'body_id'
        html_element.predecessor_id = 'some_pre_div_id'
        html_element.successor_id = 'some_other_div_id'
        
        html_element.add_attribute('class', 'some_class')
        html_element.add_attribute('value', 'some_value')
        html_element.add_attribute('placeholder', 'some_placeholder')
        html_element.add_attribute('required', '')
        
        html_element.add_css_rule('border', 'fat')
        html_element.add_css_rule('font', 'cool font')
        html_element.add_css_rule('color', 'dark black')
        
        page = HTMLPage('main_page', TEST_URL)
        page.add_html_elements(html_element)
        
        tccreator =  SeleniumTestClassCreator(page)
        
        self.maxDiff = None
        
        actual = tccreator.create()
        actual = re.sub(REMOVE_LINE_PRECEING_TABS_AND_WS, '', actual, flags=RegexFlag.M)
        
        self.assertEqual(expected, actual)
    
    def test_create_some_tag_unittest(self):
        '''
        Test only test cases for some tag is created: selenium_class.4.expected
        '''
        path_to_templates = os.path.join(os.path.dirname(os.path.abspath(__file__)), SELENIUM_TEST_CLASS_4_TESTCASE)
            
        with open(path_to_templates, 'r') as file:
            expected = file.read()
        
        expected = re.sub(REMOVE_LINE_PRECEING_TABS_AND_WS, '', expected, flags=RegexFlag.M)
        
        html_element = HTMLElement('div', 'some_div_id')
        html_element.parent_id = 'body_id'
        html_element.predecessor_id = 'some_pre_div_id'
        html_element.successor_id = 'some_other_div_id'
        
        html_element.add_attribute('class', 'some_class')
        html_element.add_attribute('value', 'some_value')
        html_element.add_attribute('placeholder', 'some_placeholder')
        
        html_element.add_css_rule('border', 'fat')
        html_element.add_css_rule('font', 'cool font')
        html_element.add_css_rule('color', 'dark black')
        
        page = HTMLPage('main_page', TEST_URL)
        page.add_html_elements(html_element)
        
        tccreator =  SeleniumTestClassCreator(page)
        
        self.maxDiff = None
        
        actual = tccreator.create()
        actual = re.sub(REMOVE_LINE_PRECEING_TABS_AND_WS, '', actual, flags=RegexFlag.M)
        
        self.assertEqual(expected, actual)
   
    def test_create_head_tag_unittest(self):
        '''
        Test only test cases for head tag is created: selenium_class.3.expected
        '''
        path_to_templates = os.path.join(os.path.dirname(os.path.abspath(__file__)), SELENIUM_TEST_CLASS_3_TESTCASE)
            
        with open(path_to_templates, 'r') as file:
            expected = file.read()
        
        expected = re.sub(REMOVE_LINE_PRECEING_TABS_AND_WS, '', expected, flags=RegexFlag.M)
        
        html_element = HTMLElement('head', 'head_id')
        html_element.parent_id = 'html_id'
        html_element.successor_id = 'body_id'
        
        page = HTMLPage('main_page', TEST_URL)
        page.add_html_elements(html_element)
        
        tccreator =  SeleniumTestClassCreator(page)
        
        self.maxDiff = None
        
        actual = tccreator.create()
        actual = re.sub(REMOVE_LINE_PRECEING_TABS_AND_WS, '', actual, flags=RegexFlag.M)
        
        self.assertEqual(expected, actual)

    def test_create_html_tag_unittest(self):
        '''
        Test only test cases for HTML tag is created: selenium_class.2.expected
        '''
        path_to_templates = os.path.join(os.path.dirname(os.path.abspath(__file__)), SELENIUM_TEST_CLASS_2_TESTCASE)
            
        with open(path_to_templates, 'r') as file:
            expected = file.read()
        
        expected = re.sub(REMOVE_LINE_PRECEING_TABS_AND_WS, '', expected, flags=RegexFlag.M)
        
        html_element = HTMLElement('html', 'html_id')
        html_element.add_attribute('lang', 'en')
        
        page = HTMLPage('main_page', TEST_URL)
        page.add_html_elements(html_element)
        
        tccreator =  SeleniumTestClassCreator(page)
        
        self.maxDiff = None
        
        actual = tccreator.create()
        actual = re.sub(REMOVE_LINE_PRECEING_TABS_AND_WS, '', actual, flags=RegexFlag.M)
        
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()