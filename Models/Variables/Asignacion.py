from Abstractos.Expresion import *
from Abstractos.Retorno import *

class Asignacion:

    def __init__(self, id, expresion, tipo):
        self.ID = id
        self.Expresion = expresion
        self.Tipo = tipo
    
    def execute(self, entorno):
        valorExp = self.Expresion.execute(entorno)

        if valorExp.Valor != "ERROR":

            # Verificar tipo si viene
            if self.Tipo != None:
                if valorExp.Tipo != self.Tipo:
                    print(f"Error: Asignacion invalida: {self.Tipo} con {valorExp.Tipo}")
                    return
            
            # Agregar a la tabla de simbolos
            entorno.setSimbolo(self.ID, valorExp, valorExp.Tipo)


