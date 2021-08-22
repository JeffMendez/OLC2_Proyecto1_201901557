from Abstractos.Expresion import *
from Abstractos.Retorno import *

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

            try:
                resultado.Valor = valorIzq.Valor and valorDer.Valor

                # Operacion que no resulta en boolean
                if resultado.Valor != False and resultado.Valor != True:
                    if resultado.Valor == valorIzq.Valor:
                        resultado.Tipo = valorIzq.Tipo
                    else:
                        resultado.Tipo = valorDer.Tipo

            except:
                resultado = Retorno("ERROR", "and")
                print(f"Error: AND invalido: {valorIzq.Tipo} con {valorDer.Tipo}")

        # OR
        elif self.Operacion == "or":

            try:
                resultado.Valor = valorIzq.Valor or valorDer.Valor

                # Operacion que no resulta en boolean
                if resultado.Valor != False and resultado.Valor != True:
                    if resultado.Valor == valorIzq.Valor:
                        resultado.Tipo = valorIzq.Tipo
                    else:
                        resultado.Tipo = valorDer.Tipo
                        
            except:
                resultado = Retorno("ERROR", "or")
                print(f"Error: OR invalido: {valorIzq.Tipo} con {valorDer.Tipo}")

        # NOT
        elif self.Operacion == "not":

            try:
                resultado.Valor = not valorIzq.Valor 
            except:
                resultado = Retorno("ERROR", "or")
                print(f"Error: NOT invalido: {valorIzq.Tipo} con {valorDer.Tipo}")

        return resultado