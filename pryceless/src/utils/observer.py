'''
Created on 03.08.2020

@author: mthoma
'''
from abc import ABC, abstractmethod
from utils.observable import Observable

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, observable: Observable) -> None:
        """
        Receive update from subject.
        """