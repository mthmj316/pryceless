'''
Created on 30.06.2020

@author: mthoma
'''

class HTMLPage:
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
        '''
            page_name getter
        '''
        return self._page_name
    
    @page_name.setter
    def page_name(self, value):
        '''
            page_name setter
        '''
        self._page_name = value
    
    @page_name.deleter
    def page_name(self):
        '''
            page_name deleter
        '''
        del self._page_name
    
    @property
    def url(self):
        '''
            url getter
        '''
        return self._url
    
    @url.setter
    def url(self, value):
        '''
            url setter
        '''
        self._url = value
    
    @url.deleter
    def url(self):
        '''
            url deleter
        '''
        del self._url
    
    @property
    def html_elements(self):
        '''
            html_elements getter
        '''
        return self._html_elements

    @html_elements.setter
    def html_element(self, value):
        '''
            html_elements setter
        '''
        self._html_elements = value
    
    def add_html_elements(self, html_element):
        '''
            adds the given html_element
        '''
        self.html_elements.append(html_element)
    