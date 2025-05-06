from abc import ABC, abstractmethod


class IAction(ABC):
    """
    An abstract base class defining the interface for soren actions(set attribitues and call methods).
    """
    @abstractmethod
    def run(self):
        """run action"""
        pass

    @abstractmethod
    def getParams(self):
        """Returns action parameters as soren protocol."""
        pass
    
    @abstractmethod
    def whoami(self):
        """Returns action name and description."""
        pass