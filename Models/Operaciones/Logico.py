from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class Logico(Expresion):

    def __init__(self, opIzq, opDer, operacion, fila, columna):
        self.OpIzq = opIzq
        self.OpDer = opDer
        self.Operacion = operacion
        self.Fila = fila
        self.Columna = columna

    def execute(self, entorno):
        valorIzq = self.OpIzq.execute(entorno)
        valorDer = None
        
        # Operaciones unarias
        if self.OpDer:
            valorDer = self.OpDer.execute(entorno)
            if valorDer.Valor == "ERROR":
                return Retorno("ERROR", "Expresion") 

        # Error en operacion anterior
        if valorIzq.Valor == "ERROR":
            return Retorno("ERROR", "Expresion") 

        resultado = Retorno(False, "Bool")

        # AND
        if self.Operacion == "and":

            if valorIzq.Tipo != "Bool" or valorDer.Tipo != "Bool":
                resultado = Retorno("ERROR", "and")
                Errores.tablaErrores.append(Error(f"AND invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))
            else:
                resultado.Valor = valorIzq.Valor and valorDer.Valor

        # OR
        elif self.Operacion == "or":

            if valorIzq.Tipo != "Bool" or valorDer.Tipo != "Bool":
                resultado = Retorno("ERROR", "or")
                Errores.tablaErrores.append(Error(f"OR invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))
            else:
                resultado.Valor = valorIzq.Valor or valorDer.Valor

        # NOT
        elif self.Operacion == "not":

            if valorIzq.Tipo != "Bool":
                resultado = Retorno("ERROR", "not")
                Errores.tablaErrores.append(Error(f"NOT invalido: {valorIzq.Tipo}", self.Fila, self.Columna))
            else:
                resultado.Valor = not valorIzq.Valor

        return resultado