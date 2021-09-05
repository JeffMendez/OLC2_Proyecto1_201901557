from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class Funcion(Expresion):

    def __init__(self, idFuncion, parametros, instrucciones, fila, columna):
        self.IDFuncion = idFuncion
        self.Parametros = parametros
        self.Instrucciones = instrucciones
        self.Fila = fila
        self.Columna = columna

    def execute(self, entorno):
        entorno.setFuncion(self.IDFuncion, self, self.Fila, self.Columna)
