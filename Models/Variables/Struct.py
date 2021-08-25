from Abstractos.Expresion import *
from Abstractos.Retorno import *

class Struct(Expresion):

    def __init__(self, id, mutable, atributos):
        self.ID = id
        self.Mutable = mutable
        self.Atributos = atributos

    def execute(self, entorno):   
        entorno.setStruct(self.ID, self)