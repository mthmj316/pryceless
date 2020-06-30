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
        self.page_name = page_name
        self.url = url
        self.html_elements = []
        
    def add_html_elements(self, html_element):
        self.html_elements.append(html_element)
