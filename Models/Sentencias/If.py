from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class If(Expresion):

    def __init__(self, condicion, instrucciones, elseInst, fila, columna):
        self.Condicion = condicion
        self.Instrucciones = instrucciones
        self.ElseInst = elseInst
        self.Fila = fila
        self.Columna = columna

    def execute(self, entorno):
        valorCondicion = self.Condicion.execute(entorno)

        if valorCondicion.Tipo != "Bool":
            Errores.tablaErrores.append(Error(f"La condicion no resulta en boolean: {valorCondicion.Tipo}", self.Fila, self.Columna))
            return
        
        if valorCondicion.Valor:
            return self.Instrucciones.execute(entorno)
        elif self.ElseInst != None:
            return self.ElseInst.execute(entorno)
