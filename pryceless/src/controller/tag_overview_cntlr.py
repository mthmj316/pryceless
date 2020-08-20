'''
Created on 04.08.2020

@author: mthoma
'''
from gui.tag_overview_ui import TagOverviewUI
from interfaces.abs_tag_overview import ABSTagOverviewUI

class TagOverviewCNTLR(object):
    '''
    classdocs
    '''
    __gui: ABSTagOverviewUI = None

    def __init__(self, master):
        '''
        Constructor
        '''
        self.__gui = TagOverviewUI(master)
        
        