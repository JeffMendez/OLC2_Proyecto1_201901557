from Abstractos.Expresion import *
from Abstractos.Retorno import *

class Atributo(Expresion):

    def __init__(self, id, tipo):
        self.ID = id
        self.Tipo = tipo
        self.Valor = None

    def execute(self, entorno):
        return Retorno(self.Valor, self.Tipo)