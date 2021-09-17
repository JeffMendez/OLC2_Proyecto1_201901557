from ...Abstractos.Expresion import *
from ...Abstractos.Retorno import *
from ...Abstractos.Error import *
from ...Abstractos import Globales

import random
import graphviz

class Aritmetica(Expresion):

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


        resultado = Retorno(0, "")

        # SUMA
        if self.Operacion == "+":

            try:
                resultado.Valor = valorIzq.Valor + valorDer.Valor
            except:
                pass

            if (valorIzq.Tipo != "Int64" and valorIzq.Tipo != "Float64") or (valorDer.Tipo != "Int64" and valorDer.Tipo != "Float64"):
                resultado = Retorno("ERROR", "+")
                Globales.tablaErrores.append(Error(f"Suma invalida: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))
            else:
                if valorIzq.Tipo == "Float64" or valorDer.Tipo == "Float64":
                    resultado.Tipo = "Float64"
                else:
                    resultado.Tipo = "Int64"

        # RESTA
        elif self.Operacion == "-":
    
            try:
                resultado.Valor = valorIzq.Valor - valorDer.Valor
            except:
                pass

            if (valorIzq.Tipo != "Int64" and valorIzq.Tipo != "Float64") or (valorDer.Tipo != "Int64" and valorDer.Tipo != "Float64"):
                resultado = Retorno("ERROR", "-")
                Globales.tablaErrores.append(Error(f"Resta invalida: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))
            else:
                if valorIzq.Tipo == "Float64" or valorDer.Tipo == "Float64":
                    resultado.Tipo = "Float64"
                else:
                    resultado.Tipo = "Int64"

        # MULTIPLICACION
        elif self.Operacion == "*":

            # Para string
            if valorIzq.Tipo == "String" and valorDer.Tipo == "String":
                resultado.Valor = valorIzq.Valor + valorDer.Valor
                resultado.Tipo = "String"
            else:
                # Para numeros
                try:
                    resultado.Valor = valorIzq.Valor * valorDer.Valor
                except:
                    pass

                if (valorIzq.Tipo != "Int64" and valorIzq.Tipo != "Float64") or (valorDer.Tipo != "Int64" and valorDer.Tipo != "Float64"):
                    resultado = Retorno("ERROR", "*")
                    Globales.tablaErrores.append(Error(f"Multiplicacion invalida: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))
                else:
                    if valorIzq.Tipo == "Float64" or valorDer.Tipo == "Float64":
                        resultado.Tipo = "Float64"
                    else:
                        resultado.Tipo = "Int64"

        # DIVISION
        elif self.Operacion == "/":

            try:
                resultado.Valor = valorIzq.Valor / valorDer.Valor
                resultado.Tipo = "Float64"
            except:
                pass

            if (valorIzq.Tipo != "Int64" and valorIzq.Tipo != "Float64") or (valorDer.Tipo != "Int64" and valorDer.Tipo != "Float64"):
                resultado = Retorno("ERROR", "/")
                Globales.tablaErrores.append(Error(f"Division invalida: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))

        # UMENOS
        elif self.Operacion == "umenos":

            try:
                resultado.Valor = valorIzq.Valor * -1
                resultado.Tipo = valorIzq.Tipo
            except:
                pass

            if valorIzq.Tipo != "Int64" and valorIzq.Tipo != "Float64":
                resultado = Retorno("ERROR", "umenos")
                Globales.tablaErrores.append(Error(f"Negacion numerica invalida: {valorIzq.Tipo}", self.Fila, self.Columna))

        # POTENCIA
        elif self.Operacion == "^":
            
            # Para string
            if valorIzq.Tipo == "String" and valorDer.Tipo == "Int64":
                resultado.Valor = ""
                resultado.Tipo = "String"
                for x in range(int(valorDer.Valor)):
                    resultado.Valor += valorIzq.Valor
            else:
                # Para numeros
                try:
                    resultado.Valor = valorIzq.Valor ** valorDer.Valor
                except:
                    pass

                if (valorIzq.Tipo != "Int64" and valorIzq.Tipo != "Float64") or (valorDer.Tipo != "Int64" and valorDer.Tipo != "Float64"):
                    resultado = Retorno("ERROR", "^")
                    Globales.tablaErrores.append(Error(f"Potencia invalida: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))
                else:
                    if valorIzq.Tipo == "Float64" or valorDer.Tipo == "Float64":
                        resultado.Tipo = "Float64"
                    else:
                        resultado.Tipo = "Int64"

        # MODULO
        elif self.Operacion == "%":

            try:
                resultado.Valor = valorIzq.Valor % valorDer.Valor
            except:
                pass

            if (valorIzq.Tipo != "Int64" and valorIzq.Tipo != "Float64") or (valorDer.Tipo != "Int64" and valorDer.Tipo != "Float64"):
                resultado = Retorno("ERROR", "%")
                Globales.tablaErrores.append(Error(f"Modulo invalido: {valorIzq.Tipo} con {valorDer.Tipo}", self.Fila, self.Columna))
            else:
                if valorIzq.Tipo == "Float64" or valorDer.Tipo == "Float64":
                    resultado.Tipo = "Float64"
                else:
                    resultado.Tipo = "Int64"

        return resultado

    def getAST(self, dot):
        idAritmetica = str(random.randint(1, 1000000000))
        idOperacion = str(random.randint(1, 1000000000))
 
        dot.node(idAritmetica, "aritmetica")
        
        dot, IDDotIzq = self.OpIzq.getAST(dot)
        dot.edge(idAritmetica, IDDotIzq)

        dot.node(idOperacion, self.Operacion)
        dot.edge(idAritmetica, idOperacion)

        if self.OpDer:
            dot, IDDotDer = self.OpDer.getAST(dot)
            dot.edge(idAritmetica, IDDotDer)

        return dot, idAritmetica