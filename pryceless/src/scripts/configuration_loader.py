'''
Created on 20.07.2020

@author: mthoma
'''
import os
import io
import collections as coll

HTML_TAG_CONF = None
ATTRIBUTES_CONF = None
LOADED_HTML_TAGS = {}
LOADED_HTML_ATTRIBUTES = {}
CSS_PROPERTIES = {}

def get_css_shorthand(property_name):
    
    print('configuration_loader.get_css_shorthand    property_name=' + property_name)
    
    __property = CSS_PROPERTIES[property_name]
    
    print('configuration_loader.get_css_shorthand    __property=' + str(__property))
    
    shorthand = __property.get('shorthand', '')
    
    print('configuration_loader.get_css_shorthand    leave:' + shorthand)
    
    return shorthand
    

def get_css_properties():
    '''
    Returns the names of all css properties.
    '''
    
    print('configuration_loader.get_css_properties')
    
    load_css_properties_conf()
    
    return CSS_PROPERTIES.keys()

def load_css_properties_conf():
    '''
    Loads the css properties from the css_properties file.
    The data will be written into CSS_PROPERTIES dict:
    CSS_PROPERTIES = {
        'font':{
            'default': 'normal'
            'shorthand':
        }
    }
    '''
    print('configuration_loader.load_css_properties_conf')
    
    global CSS_PROPERTIES
    
    if len(CSS_PROPERTIES) > 0:
        return 
    
    conf_file = io.StringIO(load_conf_files('css_properties.conf'))
    
    for line in conf_file:
        
        line = line.strip()
        
        print('configuration_loader.load_css_properties_conf    load=' + line)
        
        split_line = line.split(']::')
        
        css_property = split_line[0][1:]
        
        print('configuration_loader.load_css_properties_conf    css_property=' + css_property)
        
        css_property_attr = split_line[1].split(';')
        
        css_property_dict = {
            'default_value': css_property_attr[0],
            'shorthand': css_property_attr[1]
            }
        print('configuration_loader.load_css_properties_conf    css_property_dict=' + str(css_property_dict))
        
        CSS_PROPERTIES[css_property] = css_property_dict
        
    conf_file.close()
    
    print('configuration_loader.load_css_properties_conf    leave')
    


def load_attribute(attribute_name):
    '''
    Loads the attribute with the given name from the attributes.conf file.
    If found the conf will be returned as dictionary:
    attribute = {
        'name': <attribute name>,
        'description': <attribute description>
    }
    '''
    
    global LOADED_HTML_ATTRIBUTES
    
    if attribute_name in LOADED_HTML_ATTRIBUTES:
        return LOADED_HTML_ATTRIBUTES[attribute_name]
    
    attribute = {
        'name': attribute_name,
        'description': load_from_attributes_conf(attribute_name)
        }
    
    LOADED_HTML_ATTRIBUTES[attribute_name] = attribute
    
    return attribute

def load_from_attributes_conf(what):
    '''
    Returns the line of the attributes.conf file
    which starts with: 
    '''
    global ATTRIBUTES_CONF
    
    if ATTRIBUTES_CONF is None:
        ATTRIBUTES_CONF = load_conf_files('attributes.conf')
        
    return load_from_conf(ATTRIBUTES_CONF, what)

def load_from_html_conf(what):
    '''
    Returns the line of the html_tag.conf file
    which starts with: [what]::.
    The key is removed form the line.
    '''    
    
    global HTML_TAG_CONF
    
    if HTML_TAG_CONF is None:
        HTML_TAG_CONF = load_conf_files('html_tag.conf')
        
    return load_from_conf(HTML_TAG_CONF, what)

def load_from_conf(conf, what):
    '''
    Returns the line in conf, which starts with:
    [what]::...
    The key is removed form the line.    
    '''
    what = '[%s]::' %(what)
    
    conf_lines = io.StringIO(conf)
        
    for line in conf_lines:
        if line.startswith(what):
            conf_lines.close()
            return line[len(what):].rstrip()

def load_conf_files(conf_file_name):
    '''
    Loads the conf-file with the given conf_file_name
    and returns it as string
    '''
    print('configuration_loader.load_conf_files    conf_file_name=' + conf_file_name)
    path_to_templates = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                     '../conf/' + conf_file_name)
    
    
    print('configuration_loader.load_conf_files    path_to_templates=' + path_to_templates)
    
    with open(path_to_templates, 'r') as file:
        return file.read()

def load_html_tag(tag_name):
    '''
    '''
    
    global LOADED_HTML_TAGS
    
    if tag_name in LOADED_HTML_TAGS:
        return LOADED_HTML_TAGS[tag_name]
    
    tag_conf = load_from_html_conf(tag_name)
    tag_conf_split = tag_conf.split(';')
    
    attr_conf = tag_conf_split[0]
    event_conf =  tag_conf_split[1]
    children_conf =  tag_conf_split[2]
    parent_conf =  tag_conf_split[3]
    has_end_tag_conf =  tag_conf_split[4]
        
    result = {
            'tag': tag_name,
            'events': __load_html_tag_events(event_conf),
            'attributes': __load_html_tag_attr(attr_conf),
            'parents': __load_html_tag_rel_tag(parent_conf),
            'children': __load_html_tag_rel_tag(children_conf),
            'has_end_tag': has_end_tag_conf == 'true'
        }
    
    LOADED_HTML_TAGS[tag_name] = result
    
    return result

def __load_html_tag_rel_tag(tag_conf):
    
    rel = []
    
    if len(tag_conf) > 0:
        if 'FLOW_CONTENT' in tag_conf:
            rel += load_flow_content()
        if 'PHRASING_CONTENT' in tag_conf:
            rel += load_phrasing_content()
        if 'HEADING_CONTENT' in tag_conf:
            rel += load_heading_content()
        if 'METADATA_CONTENT' in tag_conf:
            rel += load_metadata_content()
        if 'EMBEDDED_CONTENT' in tag_conf:
            rel += load_embedded_content()
        if 'INTERACTIVE_CONTENT' in tag_conf:
            rel += load_interactive_content()
        if 'PALPABLE_CONTENT' in tag_conf:
            rel += load_palpable_content()
        if 'SECTIONING_CONTENT' in tag_conf:
            rel += load_sectioning_content()
        if 'SCRIPT_SUPPORTING_ELEMENTS' in tag_conf:
            rel += load_script_supporting_elements()
            
        for s in tag_conf.split(','):
            if not s.startswith('['):
                rel.append(s)

    return rel

def __load_html_tag_events(event_conf):  # @DontTrace
    '''
    
    :param event_conf:
    '''
    
    events = []
    
    if len(event_conf) > 0:
        
        if event_conf == '[ALL_EVENTS]':
            return load_all_events()
    
        if 'WINDOW_EVENTS' in event_conf:
            events += load_window_events()
        
        if 'FORM_EVENTS' in event_conf:
            events += load_form_events()
        
        if 'KEYBOARD_EVENTS' in event_conf:
            events += load_keyboard_events()
            
        if 'MOUSE_EVENTS' in event_conf:
            events += load_mouse_events()
            
        if 'DRAG_EVENTS' in event_conf:
            events += load_drag_events()
            
        if 'CLIPBOARD_EVENTS' in event_conf:
            events += load_clipboard_events()
        
        if 'MEDIA_EVENTS' in event_conf:
            events += load_media_events()
    
        if 'MISC_EVENTS' in event_conf:
            events += load_misc_events()
            
        for s in event_conf.split(','):
            if not s.startswith('['):
                events.append(s)
    
    return events
    
def __load_html_tag_attr(attr_conf):
    '''
    
    :param attr_conf:
    '''
    
    attributes = []
    
    if len(attr_conf) > 0:
        attr_conf_split = attr_conf.split(',')        
        if attr_conf_split[0] == '[GLOBAL_ATTRIBUTES]':
            attributes += load_global_attributes()
        
        if len(attr_conf_split) > 1:
            idx = 1
            while idx < len(attr_conf_split):
                attributes.append(attr_conf_split[idx])
                idx += 1
    return attributes
    
def load_global_attributes():
    '''
    Loads from the html_tag.conf the [GLOBAL_ATTRIBUTES] attributes
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('GLOBAL_ATTRIBUTES')
    return attr_as_string.split(',')

def load_heading_content():
    '''
    Loads from the html_tag.conf the [HEADING_CONTENT] tags
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('HEADING_CONTENT')
    return attr_as_string.split(',')
 
def load_phrasing_content():
    '''
    Loads from the html_tag.conf the [PHRASING_CONTENT] tags
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('PHRASING_CONTENT')
    return attr_as_string.split(',')

def load_flow_content():
    '''
    Loads from the html_tag.conf the [FLOW_CONTENT] tags
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('FLOW_CONTENT')
    return attr_as_string.split(',')

def load_metadata_content():
    '''
    Loads from the html_tag.conf the [METADATA_CONTENT] tags
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('METADATA_CONTENT')
    return attr_as_string.split(',')

def load_embedded_content():
    '''
    Loads from the html_tag.conf the [EMBEDDED_CONTENT] tags
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('EMBEDDED_CONTENT')
    return attr_as_string.split(',')

def load_interactive_content():
    '''
    Loads from the html_tag.conf the [INTERACTIVE_CONTENT] tags
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('INTERACTIVE_CONTENT')
    return attr_as_string.split(',')

def load_palpable_content():
    '''
    Loads from the html_tag.conf the [PALPABLE_CONTENT] tags
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('PALPABLE_CONTENT')
    return attr_as_string.split(',')

def load_sectioning_content():
    '''
    Loads from the html_tag.conf the [SECTIONING_CONTENT] tags
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('SECTIONING_CONTENT')
    return attr_as_string.split(',')

def load_script_supporting_elements():
    '''
    Loads from the html_tag.conf the [SCRIPT_SUPPORTING_ELEMENTS] tags
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('SCRIPT_SUPPORTING_ELEMENTS')
    return attr_as_string.split(',')

def load_all_events():
    '''
    Loads from the html_tag.conf all events
    and returns it as array.
    '''
    all_events = []
    all_events += load_window_events()
    all_events += load_form_events()
    all_events += load_keyboard_events()
    all_events += load_mouse_events()
    all_events += load_misc_events()
    all_events += load_media_events()
    all_events += load_clipboard_events()
    all_events += load_drag_events()
    
    return all_events

def load_window_events():
    '''
    Loads from the html_tag.conf the [WINDOW_EVENTS] events
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('WINDOW_EVENTS')
    return attr_as_string.split(',')

def load_form_events():
    '''
    Loads from the html_tag.conf the [FORM_EVENTS] events
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('FORM_EVENTS')
    return attr_as_string.split(',')

def load_keyboard_events():
    '''
    Loads from the html_tag.conf the [KEYBOARD_EVENTS] events
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('KEYBOARD_EVENTS')
    return attr_as_string.split(',')

def load_mouse_events():
    '''
    Loads from the html_tag.conf the [MOUSE_EVENTS] events
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('MOUSE_EVENTS')
    return attr_as_string.split(',')

def load_drag_events():
    '''
    Loads from the html_tag.conf the [DRAG_EVENTS] events
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('DRAG_EVENTS')
    return attr_as_string.split(',')

def load_clipboard_events():
    '''
    Loads from the html_tag.conf the [CLIPBOARD_EVENTS] events
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('CLIPBOARD_EVENTS')
    return attr_as_string.split(',')

def load_media_events():
    '''
    Loads from the html_tag.conf the [MEDIA_EVENTS] events
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('MEDIA_EVENTS')
    return attr_as_string.split(',')

def load_misc_events():
    '''
    Loads from the html_tag.conf the [MISC_EVENTS] events
    and returns it as array.
    '''
    attr_as_string = load_from_html_conf('MISC_EVENTS')
    return attr_as_string.split(',')

def load_html_description():
    '''
    Loads from html_tag_description.conf the tag descriptions
    and returns it as dictionary.
    '''
    descriptions = load_conf_files('html_tag_description.conf')
    
    io_desc = io.StringIO(descriptions)
    
    html_desc = {}
    
    for line in io_desc:
        line_splitted = line.split('::')
        desc = line_splitted[1]
        desc = desc.replace('\\n', os.linesep)
        html_desc[line_splitted[0]] = desc
    
    io_desc.close()
     
    return coll.OrderedDict(sorted(html_desc.items(), key=lambda t: t[0]))
