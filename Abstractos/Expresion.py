from abc import ABC, abstractmethod

class Expresion(ABC):

    @abstractmethod
    def execute(self, entorno):
        pass