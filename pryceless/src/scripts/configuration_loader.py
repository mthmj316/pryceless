'''
Created on 20.07.2020

@author: mthoma
'''
import os
import io
import collections as coll
from attr import attr

HTML_TAG_CONF = None

def load_from_html_conf(what):
    '''
    Returns the line of the html_tag.conf file
    which starts with: [what]::.
    The key is removed form the line.
    '''    
    what = '[%s]::' %(what)
    
    global HTML_TAG_CONF
    
    if HTML_TAG_CONF is None:
        HTML_TAG_CONF = load_conf_files('html_tag.conf')
        
    conf_lines = io.StringIO(HTML_TAG_CONF)
        
    for line in conf_lines:
        if line.startswith(what):
            conf_lines.close()
            return line[len(what):].rstrip()


def load_conf_files(conf_file_name):
    '''
    Loads the conf-file with the given conf_file_name
    and returns it as string
    '''
    path_to_templates = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                     '../conf/' + conf_file_name)
    
    with open(path_to_templates, 'r') as file:
        return file.read()

def load_html_tag(tag_name):
    '''
    '''
    tag_conf = load_from_html_conf(tag_name)
    tag_conf_split = tag_conf.split(';')
    
    attr_conf = tag_conf_split[0]
    event_conf =  tag_conf_split[1]
    parent_conf =  tag_conf_split[2]
    children_conf =  tag_conf_split[3]
    has_end_tag_conf =  tag_conf_split[4]
        
    result = {
            'tag': tag_name,
            'events': __load_html_tag_events(event_conf),
            'attributes': __load_html_tag_attr(attr_conf),
            'parents': __load_html_tag_parents(parent_conf),
            'children': __load_html_tag_children(children_conf),
            'has_end_tag': has_end_tag_conf == 'true'
        }
    
    return result

def __load_html_tag_children(children_conf):
    pass

def __load_html_tag_parents(parent_conf):
    pass

def __load_html_tag_events(event_conf):
    pass
    
def __load_html_tag_attr(attr_conf):
    
    attributes = []
    
    if len(attr_conf) > 0:
        attr_conf_split = attr_conf.split(',')
        if attr_conf_split[0] == '[GLOBAL_ATTRIBUTES]':
            attributes.append(load_global_attributes())
        
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
    all_events.append(load_window_events())
    all_events.append(load_form_events())
    all_events.append(load_keyboard_events())
    all_events.append(load_mouse_events())
    all_events.append(load_misc_events())
    all_events.append(load_media_events())
    all_events.append(load_clipboard_events())
    all_events.append(load_drag_events())
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
