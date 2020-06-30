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
        self._css_rule = {}
        self._attribute = {}
    
    @property
    def element_id(self):
        self._element_id
        
    @element_id.setter
    def element_id(self, value):
        self._element_id = value
    
    @element_id.deleter
    def element_id(self):
        del self._element_id
        
    @property
    def element_name(self):
        self._element_name
        
    @element_name.setter
    def element_name(self, value):
        self._element_name = value
    
    @element_name.deleter
    def element_name(self):
        del self._element_name
        
    @property
    def parent_id(self):
        self._parent_id
        
    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    
    @parent_id.deleter
    def parent_id(self):
        del self._parent_id
        
    @property
    def predecessor_id(self):
        self._predecessor_id
        
    @predecessor_id.setter
    def predecessor_id(self, value):
        self._predecessor_id = value
    
    @predecessor_id.deleter
    def predecessor_id(self):
        del self._predecessor_id

    @property
    def successor_id(self):
        self._successor_id
        
    @successor_id.setter
    def successor_id(self, value):
        self._successor_id = value
    
    @successor_id.deleter
    def successor_id(self):
        del self._successor_id
    
    @property
    def css_rule(self):
        self._css_rule
        
    @css_rule.setter
    def css_rule(self, value):
        self._css_rule = value
    
    def add_css_rule(self, property_name, property_value):
        self._css_rule[property_name] = property_value
    
    @property
    def attribute(self):
        self._attribute
        
    @attribute.setter
    def attribute(self, value):
        self._attribute = value
    
    def add_attribute(self, attribute_name, attribute_value):
        self._attribute[attribute_name] = attribute_value    