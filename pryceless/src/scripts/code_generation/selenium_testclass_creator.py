'''
Created on 30.06.2020

@author: mthoma
'''
from scripts.code_generation.selenium_testcase_template import create_selenium_test_class

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
            Starts the creation of the test class
        '''
        url = self._html_page.url()
        test_cases = ''
        
        return create_selenium_test_class(url, test_cases)
        
    
    @property
    def html_page(self):
        self._html_page
        
    @html_page.setter
    def html_page(self, value):
        self._html_page = value
        
    @html_page.deleter
    def html_page(self):
        del self._html_page