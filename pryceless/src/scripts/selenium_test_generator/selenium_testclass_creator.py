'''
Created on 30.06.2020

@author: mthoma
'''
from scripts.selenium_test_generator.selenium_testcase_template import create_selenium_test_class
from scripts.selenium_test_generator.selenium_testcase_creator import create_unit_test_tag_name,\
    create_unit_test_parent, create_unit_test_siblings,\
    create_unit_test_attribute, create_unit_test_css_rule

class SeleniumTestClassCreator(object):
    '''
        classdocs
    '''
    
    def __init__(self, html_page):
        '''
            constructor
            
        '''
        self._html_page = html_page
    
    def create(self):
        '''
            Starts the creation of the test class and returns the formated code.
        '''
        url = self._html_page.url()
        test_cases = []
        
        for html_element in self._html_page.html_element():
            test_cases = test_cases + self.__create_html_element(html_element)
        
        return create_selenium_test_class(url, '\n\n'.join(test_cases))
    
    def __create_html_element(self, html_element):
        '''
            Creates all test cases for the given html_element
        '''
        test_cases = []
        test_cases.append(create_unit_test_tag_name(html_element.element_id(), html_element.element_name()))
        test_cases.append(create_unit_test_parent(html_element.element_id(), html_element.parent_id()))
        test_cases.append(create_unit_test_siblings(html_element.element_id(),\
                                                    html_element.predecessor_id(),\
                                                    html_element.successor_id()))
        test_cases.append(create_unit_test_attribute(html_element.element_id(),\
                                                     html_element.attributes()))
        test_cases.append(create_unit_test_css_rule(html_element.element_id,\
                                                    html_element.css_rules()))        
        
        return test_cases
    
    @property
    def html_page(self):
        return self._html_page
        
    @html_page.setter
    def html_page(self, value):
        self._html_page = value
        
    @html_page.deleter
    def html_page(self):
        del self._html_page