'''
Created on 30.06.2020

@author: mthoma
'''

class HTMLPage(object):
    '''
    classdocs
    '''

    def __init__(self, page_name, url):
        '''
        Constructor
        '''
        self._page_name = page_name
        self._url = url
        self._html_elements = []    
    
    @property
    def page_name(self):
        self._page_name
        
    @page_name.setter
    def page_name(self, value):
        self._page_name = value
        
    @page_name.deleter
    def page_name(self):
        del self._page_name
        
    @property
    def url(self):
        self._url
        
    @url.setter
    def url(self, value):
        self._url = value
        
    @url.deleter
    def url(self):
        del self._url
    
    @property
    def html_elements(self):
        self._html_elements
        
    @html_element.setter
    def html_element(self, value):
        self._html_elements = value
        
    def add_html_elements(self, html_element):
        self.html_elements.append(html_element)
