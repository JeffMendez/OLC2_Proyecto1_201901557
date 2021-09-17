from abc import ABC, abstractmethod

class Expresion(ABC):

    @abstractmethod
    def execute(self, entornos):
        pass

    @abstractmethod
    def getAST(self, dot):
        pass