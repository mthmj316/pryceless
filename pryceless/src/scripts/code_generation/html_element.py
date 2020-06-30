'''
Created on 30.06.2020

@author: mthoma
'''

class HTMLElement(object):
    '''
    classdocs
    '''


    def __init__(self, element_name, element_id):
        '''
        Constructor
        '''
        self.element_name = element_name
        self.element_id = element_id
        self.parent_id
        self.predecessor_id
        self.successor_id
        self.css_directory = {}
        self.attribute_directory = {}
        
    def add_css_property(self, property_name, property_value):
        self.css_directory[property_name] = property_value
    
    def add_attribute(self, attribute_name, attribute_value):
        self.attribute_directory[attribute_name] = attribute_value    