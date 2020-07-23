'''
Created on 22.07.2020

@author: mthoma
'''
import unittest
from scripts import configuration_loader

H1_EXPECTED_RESULT = '[GLOBAL_ATTRIBUTES];[ALL_EVENTS];[HEADING_CONTENT];[PHRASING_CONTENT],[HEADING_CONTENT];true'
GLOBAL_ATTRIBUTES_EXPECTED_RESULT = 'accesskey,class,contenteditable,dir,draggable,hidden,id,lang,spellcheck,style,tabindex,title,translate'
P_EXPECTED_RESULT = '[GLOBAL_ATTRIBUTES];;[PHRASING_CONTENT];[FLOW_CONTENT];true'
GLOBAL_ATTRIBUTES = ['accesskey','class','contenteditable','dir','draggable','hidden','id','lang','spellcheck','style','tabindex','title','translate']
WINDOW_EVENTS = ['onafterprint','onbeforeprint','onbeforeunload','onerror','onhashchange','onload','onmessage','onoffline','ononline','onpagehide','onpageshow','onpopstate','onresize','onstorage','onunload']
FORM_EVENTS = ['onblur','onchange','oncontextmenu','onfocus','oninput','oninvalid','onreset','onsearch','onselect','onsubmit']
KEYBOARD_EVENTS = ['onkeydown','onkeypress','onkeyup']
MOUSE_EVENTS = ['onclick','ondblclick','onmousedown','onmousemove','onmouseout','onmouseover','onmouseup','onmousewheel','onwheel']
DRAG_EVENTS = ['ondrag','ondragend','ondragenter','ondragleave','ondragover','ondragstart','ondrop','onscroll']
CLIPBOARD_EVENTS = ['oncopy','oncut','onpaste']
MEDIA_EVENTS = ['onabort','oncanplay','oncanplaythrough','oncuechange','ondurationchange','onemptied','onended','onerror','onloadeddata','onloadedmetadata','onloadstart','onpause','onplay','onplaying','onprogress','onratechange','onseeked','onseeking','onstalled','onsuspend','ontimeupdate','onvolumechange','onwaiting']
MISC_EVENTS = ['ontoggle']
FLOW_CONTENT = ['a','abbr','address','area','article','aside','audio','b','bdi','bdo','blockquote','br','button','canvas','cite','code','data','datalist','del','details','dfn','dialog','div','dl','em','embed','fieldset','figure','footer','form','h1','h2','h3','h4','h5','h6','header','hgroup','hr','i','iframe','img','input','ins','kbd','label','link','main','map','mark','MathML math','menu','meta','meter','nav','noscript','object','ol','output','p','picture','pre','progress','q','ruby','s','samp','script','section','select','slot','small','span','strong','sub','sup','SVG svg','table','template','textarea','time','u','ul','var','video','wbr','autonomous custom elements','text']
PHRASING_CONTENT = ['a','abbr','area','audio','b','bdi','bdo','br','button','canvas','cite','code','data','datalist','del','dfn','em','embed','i','iframe','img','input','ins','kbd','label','link','map','mark','MathML math','meta','meter','noscript','object','output','picture','progress','q','ruby','s','samp','script','select','slot','small','span','strong','sub','sup','SVG svg','template','textarea','time','u','var','video','wbr','autonomous custom elements','text']
HEADING_CONTENT = ['h1','h2','h3','h4','h5','h6','hgroup']
METADATA_CONTENT = ['base','link','meta','noscript','script','style','template','title']
EMBEDDED_CONTENT = ['audio','canvas','embed','iframe','img','MathML math','object','picture','SVG svg','video']
INTERACTIVE_CONTENT = ['a','audio','button','details','embed','iframe','img','input','label','object','select','textarea','video']
PALPABLE_CONTENT = ['a','abbr','address','article','aside','audio','b','bdi','bdo','blockquote','button','canvas','cite','code','data','details','dfn','div','dl','em','embed','fieldset','figure','footer','form','h1','h2','h3','h4','h5','h6','header','hgroup','i','iframe','img','input','ins','kbd','label','main','map','mark','MathML math','menu','meter','nav','object','ol','output','p','pre','progress','q','ruby','s','samp','section','select','small','span','strong','sub','sup','SVG svg','table','textarea','time','u','ul','var','video','autonomous custom elements','text']
SECTIONING_CONTENT = ['article','aside','nav','section']
SCRIPT_SUPPORTING_ELEMENTS = ['script','template']

class Test(unittest.TestCase):
    
    def test_load_html_tag_h6(self):
        '''
        [h6]::[GLOBAL_ATTRIBUTES];[ALL_EVENTS];[HEADING_CONTENT];[PHRASING_CONTENT],[HEADING_CONTENT];true
        '''
        
        parents = []
        parents += PHRASING_CONTENT
        parents += HEADING_CONTENT
        
        all_events = []
        all_events += WINDOW_EVENTS
        all_events += FORM_EVENTS
        all_events += KEYBOARD_EVENTS
        all_events += MOUSE_EVENTS      
        all_events += DRAG_EVENTS        
        all_events += CLIPBOARD_EVENTS        
        all_events += MEDIA_EVENTS     
        all_events += MISC_EVENTS
        
        expected = {
            'tag': 'h6',
            'events': all_events,
            'attributes': GLOBAL_ATTRIBUTES,
            'parents': parents,
            'children': HEADING_CONTENT,
            'has_end_tag': True
            }
        
        self.maxDiff = None
        actual = configuration_loader.load_html_tag('h6')
        self.assertEqual(expected['tag'], actual['tag'])
        self.assertEqual(expected['has_end_tag'], actual['has_end_tag'])
        self.assertCountEqual(expected['events'], actual['events'])
        self.assertCountEqual(expected['attributes'], actual['attributes'])
        self.assertCountEqual(expected['parents'], actual['parents'])
        self.assertCountEqual(expected['children'], actual['children'])
    
    def test_load_html_tag_base(self):
        '''
        [base]::[GLOBAL_ATTRIBUTES],href,target;;;head;false
        '''
        attr_list = ['href','target']
        attr_list += GLOBAL_ATTRIBUTES
        
        expected = {
            'tag': 'base',
            'events': [],
            'attributes': attr_list,
            'parents': ['head'],
            'children': [],
            'has_end_tag': False
            }
        
        self.maxDiff = None
        actual = configuration_loader.load_html_tag('base')
        self.assertEqual(expected['tag'], actual['tag'])
        self.assertEqual(expected['has_end_tag'], actual['has_end_tag'])
        self.assertCountEqual(expected['events'], actual['events'])
        self.assertCountEqual(expected['attributes'], actual['attributes'])
        self.assertCountEqual(expected['parents'], actual['parents'])
        self.assertCountEqual(expected['children'], actual['children'])
    
    def test_load_all_events(self):
        '''
        Test: Loading from the html_tag.conf all events
        and returns it as array.
        '''
        all_events = []
        all_events += WINDOW_EVENTS
        all_events += FORM_EVENTS
        all_events += KEYBOARD_EVENTS
        all_events += MOUSE_EVENTS      
        all_events += DRAG_EVENTS        
        all_events += CLIPBOARD_EVENTS
        all_events += MEDIA_EVENTS     
        all_events += MISC_EVENTS
        
        actual = configuration_loader.load_all_events()
        self.assertCountEqual(all_events, actual)
    
    def test_load_window_events(self):
        '''
        Test: Loading from the html_tag.conf the [WINDOW_EVENTS] events
        and returns it as array.
        '''
        actual = configuration_loader.load_window_events()
        self.assertCountEqual(WINDOW_EVENTS, actual)
    
    def test_load_form_events(self):
        '''
        Test: Loading from the html_tag.conf the [FORM_EVENTS] events
        and returns it as array.
        '''
        actual = configuration_loader.load_form_events()
        self.assertCountEqual(FORM_EVENTS, actual)
    
    def test_load_keyboard_events(self):
        '''
        Test: Loading from the html_tag.conf the [KEYBOARD_EVENTS] events
        and returns it as array.
        '''
        actual = configuration_loader.load_form_events()
        self.assertCountEqual(FORM_EVENTS, actual)
    
    def test_load_mouse_events(self):
        '''
        Test: Loading from the html_tag.conf the [MOUSE_EVENTS] events
        and returns it as array.
        '''
        actual = configuration_loader.load_form_events()
        self.assertCountEqual(FORM_EVENTS, actual)
    
    def load_drag_events(self):
        '''
        Test: Loading from the html_tag.conf the [DRAG_EVENTS] events
        and returns it as array.
        '''
        actual = configuration_loader.load_drag_events()
        self.assertCountEqual(DRAG_EVENTS, actual)
    
    def test_load_clipboard_events(self):
        '''
        Test: Loading from the html_tag.conf the [CLIPBOARD_EVENTS] events
        and returns it as array.
        '''
        actual = configuration_loader.load_clipboard_events()
        self.assertCountEqual(CLIPBOARD_EVENTS, actual)
    
    def test_load_media_events(self):
        '''
        Test: Loading from the html_tag.conf the [MEDIA_EVENTS] events
        and returns it as array.
        '''
        actual = configuration_loader.load_media_events()
        self.assertCountEqual(MEDIA_EVENTS, actual)
    
    def test_load_misc_events(self):
        '''
        Test: Loading from the html_tag.conf the [MISC_EVENTS] events
        and returns it as array.
        '''
        actual = configuration_loader.load_misc_events()
        self.assertCountEqual(MISC_EVENTS, actual)
    
    def test_load_script_supporting_elements(self):
        '''
        Test the onfiguration_loader.load_script_supporting_elements() function
        '''
        actual = configuration_loader.load_script_supporting_elements()
        self.assertCountEqual(SCRIPT_SUPPORTING_ELEMENTS, actual)
    
    def test_load_sectioning_content(self):
        '''
        Test the onfiguration_loader.load_sectioning_content() function
        '''
        actual = configuration_loader.load_sectioning_content()
        self.assertCountEqual(SECTIONING_CONTENT, actual)
    
    def test_load_palpable_content(self):
        '''
        Test the onfiguration_loader.load_palpable_content() function
        '''
        actual = configuration_loader.load_palpable_content()
        self.assertCountEqual(PALPABLE_CONTENT, actual)
    
    def test_load_interactive_content(self):
        '''
        Test the onfiguration_loader.load_interactive_content() function
        '''
        actual = configuration_loader.load_interactive_content()
        self.assertCountEqual(INTERACTIVE_CONTENT, actual)
    
    def test_load_embedded_content(self):
        '''
        Test the onfiguration_loader.load_embedded_content() function
        '''
        actual = configuration_loader.load_embedded_content()
        self.assertCountEqual(EMBEDDED_CONTENT, actual)
    
    def test_load_metadata_content(self):
        '''
        Test the onfiguration_loader.load_metadata_content() function
        '''
        actual = configuration_loader.load_metadata_content()
        self.assertCountEqual(METADATA_CONTENT, actual)
    
    def test_load_flow_content(self):
        '''
        Test the onfiguration_loader.load_flow_content() function
        '''
        actual = configuration_loader.load_flow_content()
        self.assertCountEqual(FLOW_CONTENT, actual)
    
    def test_load_phrasing_content(self):
        '''
        Test the onfiguration_loader.load_phrasing_content() function
        '''
        actual = configuration_loader.load_phrasing_content()
        self.assertCountEqual(PHRASING_CONTENT, actual)
    
    def test_load_heading_content(self):
        '''
        Test the onfiguration_loader.load_heading_contents() function
        '''
        actual = configuration_loader.load_heading_content()
        self.assertCountEqual(HEADING_CONTENT, actual)
    
    def test_load_global_attributes(self):
        '''
        Test the onfiguration_loader.load_global_attributes() function
        '''
        actual = configuration_loader.load_global_attributes()
        self.assertCountEqual(GLOBAL_ATTRIBUTES, actual)
    
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