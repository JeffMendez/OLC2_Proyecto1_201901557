from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class ParamDecl(Expresion):

    def __init__(self, idParam, idTipo, fila, columna):
        self.IDParam = idParam
        self.IDTipo = idTipo
        self.Fila = fila
        self.Columna = columna

    def execute(self, entorno):
        return self