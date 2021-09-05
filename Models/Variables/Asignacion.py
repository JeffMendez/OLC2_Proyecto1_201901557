from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class Asignacion(Expresion):

    def __init__(self, id, expresion, tipo, fila, columna):
        self.ID = id
        self.Expresion = expresion
        self.Tipo = tipo
        self.Fila = fila
        self.Columna = columna
    
    def execute(self, entorno):
        valorExp = self.Expresion.execute(entorno)

        if valorExp.Valor != "ERROR":

            # Para variables, arreglos - Verificar tipo si viene
            if self.Tipo != None:
                if valorExp.Tipo != self.Tipo:
                    Errores.tablaErrores.append(Error(f"Asignacion invalida: {self.Tipo} con {valorExp.Tipo}", self.Fila, self.Columna))
                    return

            # Agregar a la tabla de simbolos
            entorno.setSimbolo(self.ID, valorExp, valorExp.Tipo)

            
                

            

