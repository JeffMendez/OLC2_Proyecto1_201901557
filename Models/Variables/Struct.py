from Abstractos.Expresion import *
from Abstractos.Retorno import *

class Struct(Expresion):

    def __init__(self, id, mutable, atributos, fila = None, columna = None):
        self.ID = id
        self.Mutable = mutable
        self.Atributos = atributos
        self.Fila = fila
        self.Columna = columna

    def execute(self, entorno):   
        entorno.setStruct(self.ID, self, self.Fila, self.Columna)