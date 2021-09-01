from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class While(Expresion):

    def __init__(self, condicion, instrucciones, fila, columna):
        self.Condicion = condicion
        self.Instrucciones = instrucciones
        self.Fila = fila
        self.Columna = columna
    
    def execute(self, entorno):
        while True:
            valorCondicion = self.Condicion.execute(entorno)
            
            if valorCondicion.Tipo != "Bool":
                Errores.tablaErrores.append(Error(f"La condicion no resulta en boolean: {valorCondicion.Tipo}", self.Fila, self.Columna))
                return
            
            if valorCondicion.Valor:
                resultCorrida = self.Instrucciones.execute(entorno)
                # Servira para sentencias de transferencia
            else:
                return