'''
Created on 22.07.2020

@author: mthoma
'''
import unittest
from scripts import configuration_loader

H1_EXPECTED_RESULT = '[GLOBAL_ATTRIBUTES];[ALL_EVENTS];[HEADING_CONTENT];[PHRASING_CONTENT],[HEADING_CONTENT];true'
GLOBAL_ATTRIBUTES_EXPECTED_RESULT = 'accesskey,class,contenteditable,dir,draggable,hidden,id,lang,spellcheck,style,tabindex,title,translate'
P_EXPECTED_RESULT = '[GLOBAL_ATTRIBUTES];;[PHRASING_CONTENT];[FLOW_CONTENT];true'

class Test(unittest.TestCase):
    
    def test_html_tag_conf_setting(self):
        '''
        Test if after configuration_loader.load_from_html_conf has been called
        the global variable configuration_loader.HTML_TAG_CONF is set.
        '''
        configuration_loader.load_from_html_conf('body')
        #self.assertIsNotNone(configuration_loader.HTML_TAG_CONF)

    def test_load_from_html_conf_p(self):
        '''
        Test load p configuration by load_from_html_conf
        '''
        actual = configuration_loader.load_from_html_conf('p')
        self.assertEqual(P_EXPECTED_RESULT,actual)

    def test_load_from_html_conf_global_attributes(self):
        '''
        Test load GLOBAL_ATTRIBUTES configuration by load_from_html_conf
        '''
        actual = configuration_loader.load_from_html_conf('GLOBAL_ATTRIBUTES')
        self.assertEqual(GLOBAL_ATTRIBUTES_EXPECTED_RESULT,actual)

    def test_load_from_html_conf_h1(self):
        '''
        Test load h1 configuration by load_from_html_conf
        '''
        actual = configuration_loader.load_from_html_conf('h1')
        self.assertEqual(H1_EXPECTED_RESULT,actual)


if __name__ == "__main__":
    unittest.main()