'''
Created on 30.06.2020

@author: mthoma
'''

class HTMLElement:
    '''
    classdocs
    '''
    def __init__(self, element_name, element_id):
        '''
        Constructor
        '''
        self._element_name = element_name
        self._element_id = element_id
        self._parent_id = ''
        self._predecessor_id = ''
        self._successor_id = ''
        self._css_rules = {}
        self._attributes = {}

    @property
    def element_id(self):
        '''
            element_id getter
        '''
        return self._element_id

    @element_id.setter
    def element_id(self, value):
        '''
            element_id setter
        '''
        self._element_id = value

    @element_id.deleter
    def element_id(self):
        '''
            element_id deleter
        '''
        del self._element_id

    @property
    def element_name(self):
        '''
            element_name getter
        '''
        return self._element_name

    @element_name.setter
    def element_name(self, value):
        '''
            element_name setter
        '''
        self._element_name = value
    
    @element_name.deleter
    def element_name(self):
        '''
            element_name deleter
        '''
        del self._element_name

    @property
    def parent_id(self):
        '''
            parent_id getter
        '''
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        '''
            parent_id setter
        '''
        self._parent_id = value

    @parent_id.deleter
    def parent_id(self):
        '''
            parent_id deleter
        '''
        del self._parent_id

    @property
    def predecessor_id(self):
        '''
            predecessor_id getter
        '''
        return self._predecessor_id

    @predecessor_id.setter
    def predecessor_id(self, value):
        '''
            predecessor_id setter
        '''
        self._predecessor_id = value

    @predecessor_id.deleter
    def predecessor_id(self):
        '''
            predecessor_id deleter
        '''
        del self._predecessor_id

    @property
    def successor_id(self):
        '''
            successor_id getter
        '''
        return self._successor_id

    @successor_id.setter
    def successor_id(self, value):
        '''
            successor_id setter
        '''
        self._successor_id = value

    @successor_id.deleter
    def successor_id(self):
        '''
            successor_id deleter
        '''
        del self._successor_id

    @property
    def css_rules(self):
        '''
            css_rules getter
        '''
        return self._css_rules
    
    @css_rules.setter
    def css_rules(self, value):
        '''
            css_rules setter
        '''
        self._css_rules = value
    
    def add_css_rule(self, property_name, property_value):
        '''
            adds the given property to the css_rules
        '''
        self._css_rules[property_name] = property_value

    @property
    def attributes(self):
        '''
            attributes getter
        '''
        return self._attributes
    
    @attributes.setter
    def attributes(self, value):
        '''
            attributes setter
        '''
        self._attributes = value

    def add_attribute(self, attribute_name, attribute_value):
        '''
            adds the given attribute to the attributes
        '''
        self._attributes[attribute_name] = attribute_value  
        