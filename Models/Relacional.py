from Abstractos.Expresion import *
from Abstractos.Retorno import *

class Relacional(Expresion):

    def __init__(self, opIzq, opDer, operacion):
        self.OpIzq = opIzq
        self.OpDer = opDer
        self.Operacion = operacion

    def execute(self, entorno):
        valorIzq = self.OpIzq.execute(None)
        valorDer = self.OpDer.execute(None)

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
                print(f"Error: Operacion > invalida: {valorIzq.Tipo} con {valorDer.Tipo}")

        # MENOR
        elif self.Operacion == "<":

            try:
                resultado.Valor = valorIzq.Valor < valorDer.Valor
            except:
                resultado = Retorno("ERROR", "<")
                print(f"Error: Operacion < invalida: {valorIzq.Tipo} con {valorDer.Tipo}")

        # MAYOR IGUAL
        elif self.Operacion == ">=":

            try:
                resultado.Valor = valorIzq.Valor >= valorDer.Valor
            except:
                resultado = Retorno("ERROR", ">=")
                print(f"Error: Operacion >= invalida: {valorIzq.Tipo} con {valorDer.Tipo}")

        # MENOR IGUAL
        elif self.Operacion == "<=":
        
            try:
                resultado.Valor = valorIzq.Valor <= valorDer.Valor
            except:
                resultado = Retorno("ERROR", "<=")
                print(f"Error: Operacion <= invalida: {valorIzq.Tipo} con {valorDer.Tipo}")

        # IGUALDAD
        elif self.Operacion == "==":
            
            try:
                resultado.Valor = valorIzq.Valor == valorDer.Valor
            except:
                resultado = Retorno("ERROR", "==")
                print(f"Error: Operacion == invalida: {valorIzq.Tipo} con {valorDer.Tipo}")

        # DISTINTO
        elif self.Operacion == "!=":
            
            try:
                resultado.Valor = valorIzq.Valor != valorDer.Valor
            except:
                resultado = Retorno("ERROR", "!=")
                print(f"Error: Operacion != invalida: {valorIzq.Tipo} con {valorDer.Tipo}")
        

        return resultado