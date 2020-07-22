'''
Created on 20.07.2020

@author: mthoma
'''
import os
import io
import collections as coll

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
    pass

def load_global_attributes():
    '''
    Loads from the html_tag.conf the [GLOBAL_ATTRIBUTES] attributes
    and returns it as array.
    '''
    pass

def load_heading_contents():
    '''
    Loads from the html_tag.conf the [HEADING_CONTENT] tags
    and returns it as array.
    '''
    pass
 
def load_phrasing_content():
    '''
    Loads from the html_tag.conf the [PHRASING_CONTENT] tags
    and returns it as array.
    '''
    pass

def load_flow_content():
    '''
    Loads from the html_tag.conf the [FLOW_CONTENT] tags
    and returns it as array.
    '''
    pass

def load_metadata_content():
    '''
    Loads from the html_tag.conf the [METADATA_CONTENT] tags
    and returns it as array.
    '''
    pass

def load_embedded_content():
    '''
    Loads from the html_tag.conf the [EMBEDDED_CONTENT] tags
    and returns it as array.
    '''
    pass

def load_interactive_content():
    '''
    Loads from the html_tag.conf the [INTERACTIVE_CONTENT] tags
    and returns it as array.
    '''
    pass

def load_palpable_content():
    '''
    Loads from the html_tag.conf the [PALPABLE_CONTENT] tags
    and returns it as array.
    '''
    pass

def load_sectioning_content():
    '''
    Loads from the html_tag.conf the [SECTIONING_CONTENT] tags
    and returns it as array.
    '''
    pass

def load_script_supporting_elements():
    '''
    Loads from the html_tag.conf the [SCRIPT_SUPPORTING_ELEMENTS] tags
    and returns it as array.
    '''
    pass

def load_all_events():
    '''
    Loads from the html_tag.conf all events
    and returns it as array.
    '''
    pass

def load_window_events():
    '''
    Loads from the html_tag.conf the [WINDOW_EVENTS] events
    and returns it as array.
    '''
    pass

def load_form_events():
    '''
    Loads from the html_tag.conf the [FORM_EVENTS] events
    and returns it as array.
    '''
    pass

def load_keyboard_events():
    '''
    Loads from the html_tag.conf the [KEYBOARD_EVENTS] events
    and returns it as array.
    '''
    pass

def load_mouse_events():
    '''
    Loads from the html_tag.conf the [MOUSE_EVENTS] events
    and returns it as array.
    '''
    pass

def load_drag_events():
    '''
    Loads from the html_tag.conf the [DRAG_EVENTS] events
    and returns it as array.
    '''
    pass

def load_clipboard_events():
    '''
    Loads from the html_tag.conf the [CLIPBOARD_EVENTS] events
    and returns it as array.
    '''
    pass

def load_media_events():
    '''
    Loads from the html_tag.conf the [MEDIA_EVENTS] events
    and returns it as array.
    '''
    pass

def load_misc_events():
    '''
    Loads from the html_tag.conf the [MISC_EVENTS] events
    and returns it as array.
    '''
    pass

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
