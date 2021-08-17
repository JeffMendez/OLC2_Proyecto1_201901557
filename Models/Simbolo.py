from Abstractos.Expresion import *
from Abstractos.Retorno import *

class Simbolo(Expresion):

    # Tipo -> int, string, etc
    # Clase -> variable, arreglo, struct

    def __init__(self, valor, tipo, clase):
        self.Valor = valor
        self.Tipo = tipo
        self.Clase = clase

    def execute(self, entorno):
        return Retorno(self.Valor, self.Tipo)

