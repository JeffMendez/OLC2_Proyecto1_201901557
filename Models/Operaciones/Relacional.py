from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class Relacional(Expresion):

    def __init__(self, opIzq, opDer, operacion, fila, columna):
        self.OpIzq = opIzq
        self.OpDer = opDer
        self.Operacion = operacion
        self.Fila = fila
        self.Columna = columna

    def execute(self, entorno):
        valorIzq = self.OpIzq.execute(entorno)
        valorDer = self.OpDer.execute(entorno)

        resultado = Retorno(False, "Bool")

        # Error en operacion anterior
        if valorIzq.Valor == "ERROR" or valorDer.Valor == "ERROR":
            return Retorno("ERROR", "Expresion") 

        # MAYOR
        if self.Operacion == ">":

            try:
                resultado.Valor = valorIzq.Valor > valorDer.Valor
            except:
                resultado = Retorno("ERROR", ">")
                Errores.tablaErrores.append(Error(f"Mayor '>' invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # MENOR
        elif self.Operacion == "<":

            try:
                resultado.Valor = valorIzq.Valor < valorDer.Valor
            except:
                resultado = Retorno("ERROR", "<")
                Errores.tablaErrores.append(Error(f"Menor '<' invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # MAYOR IGUAL
        elif self.Operacion == ">=":

            try:
                resultado.Valor = valorIzq.Valor >= valorDer.Valor
            except:
                resultado = Retorno("ERROR", ">=")
                Errores.tablaErrores.append(Error(f"Mayor igual '>=' invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # MENOR IGUAL
        elif self.Operacion == "<=":
        
            try:
                resultado.Valor = valorIzq.Valor <= valorDer.Valor
            except:
                resultado = Retorno("ERROR", "<=")
                Errores.tablaErrores.append(Error(f"Menor igual '<=' invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # IGUALDAD
        elif self.Operacion == "==":
            
            try:
                resultado.Valor = valorIzq.Valor == valorDer.Valor
            except:
                resultado = Retorno("ERROR", "==")
                Errores.tablaErrores.append(Error(f"Igualdad '==' invalida: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # DISTINTO
        elif self.Operacion == "!=":
            
            try:
                resultado.Valor = valorIzq.Valor != valorDer.Valor
            except:
                resultado = Retorno("ERROR", "!=")
                Errores.tablaErrores.append(Error(f"Igualdad '!=' invalida: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))
        
        return resultado