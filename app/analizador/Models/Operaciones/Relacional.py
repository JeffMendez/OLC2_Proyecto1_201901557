from ...Abstractos.Expresion import *
from ...Abstractos.Retorno import *
from ...Abstractos.Error import *
from ...Abstractos import Globales

import random
import graphviz

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
                #if valorIzq.Tipo == "Nulo": valorIzq.Valor = 0
                resultado.Valor = valorIzq.Valor > valorDer.Valor
            except:
                resultado = Retorno("ERROR", ">")
                print(valorIzq.Valor, valorDer.Valor)
                Globales.tablaErrores.append(Error(f"Mayor '>' invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # MENOR
        elif self.Operacion == "<":

            try:
                resultado.Valor = valorIzq.Valor < valorDer.Valor
            except:
                resultado = Retorno("ERROR", "<")
                Globales.tablaErrores.append(Error(f"Menor '<' invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # MAYOR IGUAL
        elif self.Operacion == ">=":

            try:
                resultado.Valor = valorIzq.Valor >= valorDer.Valor
            except:
                resultado = Retorno("ERROR", ">=")
                Globales.tablaErrores.append(Error(f"Mayor igual '>=' invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # MENOR IGUAL
        elif self.Operacion == "<=":
        
            try:
                resultado.Valor = valorIzq.Valor <= valorDer.Valor
            except:
                resultado = Retorno("ERROR", "<=")
                Globales.tablaErrores.append(Error(f"Menor igual '<=' invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # IGUALDAD
        elif self.Operacion == "==":
            
            try:
                resultado.Valor = valorIzq.Valor == valorDer.Valor
            except:
                resultado = Retorno("ERROR", "==")
                Globales.tablaErrores.append(Error(f"Igualdad '==' invalida: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # DISTINTO
        elif self.Operacion == "!=":
            
            try:
                resultado.Valor = valorIzq.Valor != valorDer.Valor
            except:
                resultado = Retorno("ERROR", "!=")
                Globales.tablaErrores.append(Error(f"Igualdad '!=' invalida: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))
        
        return resultado

    def getAST(self, dot):
        idRelacional = str(random.randint(1, 1000000000))
        idOperacion = str(random.randint(1, 1000000000))
 
        dot.node(idRelacional, "relacional")
        
        dot, IDDotIzq = self.OpIzq.getAST(dot)
        dot.edge(idRelacional, IDDotIzq)

        dot.node(idOperacion, self.Operacion)
        dot.edge(idRelacional, idOperacion)

        if self.OpDer:
            dot, IDDotDer = self.OpDer.getAST(dot)
            dot.edge(idRelacional, IDDotDer)

        return dot, idRelacional