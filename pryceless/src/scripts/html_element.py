'''
Created on 30.06.2020

@author: mthoma
'''
from orca.scripts import self_voicing

class HTMLElement(object):
    '''
    classdocs
    '''


    def __init__(self, element_name, element_id):
        '''
        Constructor
        '''
        self._element_name = element_name
        self._element_id = element_id
        self._parent_id
        self._predecessor_id
        self._successor_id
        self._css_rules = {}
        self._attributes = {}
    
    @property
    def element_id(self):
        return self._element_id
        
    @element_id.setter
    def element_id(self, value):
        self._element_id = value
    
    @element_id.deleter
    def element_id(self):
        del self._element_id
        
    @property
    def element_name(self):
        return self._element_name
        
    @element_name.setter
    def element_name(self, value):
        self._element_name = value
    
    @element_name.deleter
    def element_name(self):
        del self._element_name
        
    @property
    def parent_id(self):
        return self._parent_id
        
    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    
    @parent_id.deleter
    def parent_id(self):
        del self._parent_id
        
    @property
    def predecessor_id(self):
        return self._predecessor_id
        
    @predecessor_id.setter
    def predecessor_id(self, value):
        self._predecessor_id = value
    
    @predecessor_id.deleter
    def predecessor_id(self):
        del self._predecessor_id

    @property
    def successor_id(self):
        return self._successor_id
        
    @successor_id.setter
    def successor_id(self, value):
        self._successor_id = value
    
    @successor_id.deleter
    def successor_id(self):
        del self._successor_id
    
    @property
    def css_rules(self):
        return self._css_rules
        
    @css_rules.setter
    def css_rules(self, value):
        self._css_rules = value
    
    def add_css_rule(self, property_name, property_value):
        self._css_rules[property_name] = property_value
    
    @property
    def attributes(self):
        return self._attributes
        
    @attributes.setter
    def attributes(self, value):
        self._attributes = value
    
    def add_attribute(self, attribute_name, attribute_value):
        self._attributes[attribute_name] = attribute_value    